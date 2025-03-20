import os
import sys
import site
import ctypes
import shutil
import zipfile
import urllib.request
from typing import Optional, Union
from modules import rocm


DLL_MAPPING = {
    'cublas.dll': 'cublas64_11.dll',
    'cusparse.dll': 'cusparse64_11.dll',
    'cufft.dll': 'cufft64_10.dll',
    'cufftw.dll': 'cufftw64_10.dll',
    'nvrtc.dll': 'nvrtc64_112_0.dll',
}
HIPSDK_TARGETS = ['rocblas.dll', 'rocsolver.dll', 'hipfft.dll']
ZLUDA_TARGETS = ('nvcuda.dll', 'nvml.dll',)
experimental_hipBLASLt_support = False
default_agent: Union[rocm.Agent, None] = None
MIOpen_available = False

#  ZLUDA 
def get_path() -> str:
    return os.path.abspath(os.environ.get('ZLUDA', '.zluda'))

#  ROCm 
def set_default_agent(agent: rocm.Agent):
    global default_agent  # pylint: disable=global-statement
    default_agent = agent

    is_nightly = False
    try:
        nvcuda = ctypes.windll.LoadLibrary(os.path.join(get_path(), 'nvcuda.dll'))
        nvcuda.zluda_get_nightly_flag.restype = ctypes.c_int
        nvcuda.zluda_get_nightly_flag.argtypes = []
        is_nightly = nvcuda.zluda_get_nightly_flag() == 1
    except Exception:
        pass

    global MIOpen_available  # pylint: disable=global-statement
    MIOpen_available = is_nightly and (skip_arch_test or agent.gfx_version in (0x908, 0x90a, 0x940, 0x941, 0x942, 0x1030, 0x1100, 0x1101, 0x1102, 0x1150,))

# ZLUDA ENV
def __initialize(zluda_path: os.PathLike):
    global experimental_hipBLASLt_support  # pylint: disable=global-statement
    experimental_hipBLASLt_support = os.path.exists(os.path.join(zluda_path, 'cublasLt.dll'))
    
    if experimental_hipBLASLt_support:
        HIPSDK_TARGETS.append('hipblaslt.dll')
        DLL_MAPPING['cublasLt.dll'] = 'cublasLt64_11.dll'
    else:
        HIPSDK_TARGETS.append(f'hiprtc{"".join([v.zfill(2) for v in rocm.version.split(".")])}.dll')

# Install ZLUDA
def install(zluda_path: os.PathLike) -> None:
    if os.path.exists(zluda_path):
        __initialize(zluda_path)
        return

    platform = "windows"
    commit = os.environ.get("ZLUDA_HASH", "4d14bf95d4c500863e240a0b1fa82793d0da789b")
    if os.environ.get("ZLUDA_NIGHTLY", "0") == "1":
        platform = "nightly-" + platform

    zluda_url = f'https://github.com/lshqqytiger/ZLUDA/releases/download/rel.{commit}/ZLUDA-{platform}-rocm{rocm.version[0]}-amd64.zip'

    try:
        urllib.request.urlretrieve(zluda_url, '_zluda')
    except Exception as e:
        print(f"Failed to download ZLUDA from {zluda_url}. Error: {e}")
        print("Please check the URL and your network connection.")
        return

    with zipfile.ZipFile('_zluda', 'r') as archive:
        infos = archive.infolist()
        for info in infos:
            if not info.is_dir():
                info.filename = os.path.basename(info.filename)
                archive.extract(info, zluda_path)
    os.remove('_zluda')
    __initialize(zluda_path)

# remove ZLUDA
def uninstall() -> None:
    zluda_path = get_path()
    if os.path.exists(zluda_path):
        shutil.rmtree(zluda_path)

# copy
def make_copy(zluda_path: os.PathLike) -> None:
    for k, v in DLL_MAPPING.items():
        if not os.path.exists(os.path.join(zluda_path, v)):
            try:
                os.link(os.path.join(zluda_path, k), os.path.join(zluda_path, v))
            except Exception:
                shutil.copyfile(os.path.join(zluda_path, k), os.path.join(zluda_path, v))

    if experimental_hipBLASLt_support and not os.path.exists(os.path.join(zluda_path, 'cublasLt64_11.dll')):
        try:
            os.link(os.path.join(zluda_path, 'cublasLt.dll'), os.path.join(zluda_path, 'cublasLt64_11.dll'))
        except Exception:
            shutil.copyfile(os.path.join(zluda_path, 'cublasLt.dll'), os.path.join(zluda_path, 'cublasLt64_11.dll'))

# load ZLUDA env
def load(zluda_path: os.PathLike) -> None:
    os.environ["ZLUDA_COMGR_LOG_LEVEL"] = "1"
    os.environ["ZLUDA_NVRTC_LIB"] = os.path.join([v for v in site.getsitepackages() if v.endswith("site-packages")][0], "torch", "lib", "nvrtc64_112_0.dll")

    for v in HIPSDK_TARGETS:
        ctypes.windll.LoadLibrary(os.path.join(rocm.path, 'bin', v))
    for v in ZLUDA_TARGETS:
        ctypes.windll.LoadLibrary(os.path.join(zluda_path, v))
    for v in DLL_MAPPING.values():
        ctypes.windll.LoadLibrary(os.path.join(zluda_path, v))

    if experimental_hipBLASLt_support:
        os.environ.setdefault("DISABLE_ADDMM_CUDA_LT", "0")
        ctypes.windll.LoadLibrary(os.path.join(rocm.path, 'bin', 'hipblaslt.dll'))
        ctypes.windll.LoadLibrary(os.path.join(zluda_path, 'cublasLt64_11.dll'))
    else:
        os.environ["DISABLE_ADDMM_CUDA_LT"] = "1"

    if MIOpen_available:
        ctypes.windll.LoadLibrary(os.path.join(rocm.path, 'bin', 'MIOpen.dll'))
        ctypes.windll.LoadLibrary(os.path.join(path, 'cudnn64_9.dll'))

    def conceal():
        import torch # noqa: F401
        platform = sys.platform
        sys.platform = ""
        from torch.utils import cpp_extension
        sys.platform = platform
        cpp_extension.IS_WINDOWS = platform == "win32"
        cpp_extension.IS_MACOS = False
        cpp_extension.IS_LINUX = platform.startswith('linux')
        def _join_rocm_home(*paths) -> str:
            return os.path.join(cpp_extension.ROCM_HOME, *paths)
        cpp_extension._join_rocm_home = _join_rocm_home # pylint: disable=protected-access
    rocm.conceal = conceal

# eg
if __name__ == "__main__":
    zluda_path = get_path()
    install(zluda_path)
    make_copy(zluda_path)
    load()