# Stable Diffusion WebUI Forge on AMD GPU

Stable Diffusion WebUI Forge is a platform on top of [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) (based on [Gradio](https://www.gradio.app/)) to make development easier, optimize resource management, and speed up inference.

The code from forked from  https://github.com/lllyasviel/stable-diffusion-webui-forge, you can find more detail from here .

The code tweaked based on git clone https://githubfast.com/lshqqytiger/stable-diffusion-webui-directml.git which nativly support zluda on amd .

If you want learn what changes between them . I only touch cmd_args.py,initialize.py,launch_utils.py and add zluda.py, All those changes code came  from https://githubfast.com/lshqqytiger , Credits should goes to lshqqytiger and lllyasviel.

INSTALL ,You can refer to https://github.com/vladmandic/automatic/wiki/ZLUDA for more about information.

## 1, Installing ZLUDA for AMD GPUs in Windows.

## Compatible GPUs
A list of compatible GPUs can be found here(https://rocm.docs.amd.com/projects/install-on-windows/en/develop/reference/system-requirements.html). If your GPU is not on the list, then you may be need to build your own rocblas library to use ZLUDA or used builded library by others (eg, https://github.com/brknsoul/ROCmLibs/raw/main/ROCmLibs.zip?download=).
(Note: how to build robclas ? follow the last step)

Note: If you have an integrated GPU (iGPU), you may need to disable it, or use the HIP_VISIBLE_DEVICES environment variable. OR if you IGPU exactly The apu amd 780M , download this file ( https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU-)
For example ,rocblas.dll into C:\Program Files\AMD\ROCm\5.7\bin( this fold will appear after install HIP SKD  IN next step) replace the origianl one ,replace library within rocblas\library , the orignally library can be rename to something else , like , "origlibrary" in case for other uses. Reboot PC

## Install HIP SDK
Install HIP SDK 5.7 from https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html

## Install Perl
Install Perl https://strawberryperl.com/

The hipconfig command does not work without Perl

## Add folders to PATH
Download from here（https://github.com/lshqqytiger/ZLUDA/releases/）
Add the ZLUDA folder* and %HIP_PATH%bin to your PATH.
https://github.com/brknsoul/ROCmLibs/wiki/Adding-folders-to-PATH
(note, you don't need to rename zluda files cublas.dll to cublas64_11.dll ,cusparse to cusparse64_11.dll and replace the one in vevn folder like other tutorial because the zluda had already detecd in patch in script)

## 2, Install ;

git clone https://github.com/likelovewant/stable-diffusion-webui-forge-on-amd.git
then

start by run : webui.bat --use-zluda



or you may try add extra --cuda-stream --pin-shared-memory  to test the speed .


## Extra: if you do need build roclabs or already have library ,please skip this .
1,Visual Studio 2022
2,Python
3.Strawberry Perl
4,CMake
5,Git
6,HIP SDK ( mentioned in first step)
7 , download https://github.com/ROCm/rocBLAS and [https://github.com/ROCm/rocBLAS](https://github.com/ROCm/Tensile) , put in same fold , eg , rocm ( more information from here https://rocmdocs.amd.com/projects/rocBLAS/en/latest/Windows_Install_Guide.html)

in the rocm/rocBLAS , run python rdeps.py ( if you encounter any mistakes , try to google and fix with it )
after done . try next step " python rmake.py -a "gfx1101;gfx1103" --lazy-library-loading --no-merge-architectures -t "C:\rocm\Tensile" the gfx1101,gfx1103 change  to your gpu or apu namber .

Note: you need to change coresponding data in Tensile/Common.py in tensile library .change data in " globalParameters["SupportedISA"]" and "CACHED_ASM_CAPS" add data of your gpu number .and choose the simliar gpu achetecture. eg RND3 , then copy and put below with gpu number and others availble gpu data . if you want more perfect , you may try to use the data availbe in rocBLAS\library\src\blas3\Tensile\Logic\asm_full , change the data in their , eg, navi32,31 , you may build a new fold there name navi 3x , copy the files in navi32 to navi 3x , then you vs code to replace the gpu number .save it . and use navi34 in your  Tensile/Common.py in terms of  "CACHED_ASM_CAPS" .
( The credits goes to wdx04 ,the original post in Chinese . you can refer it from there ([[(https://zhuanlan.zhihu.com/p/680642344)](https://zhuanlan.zhihu.com/p/680642344] )

All done . Have a good lucy and Hope enjoy it!












