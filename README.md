

# Stable Diffusion WebUI Forge on AMD GPU

Stable Diffusion WebUI Forge is a platform on top of [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) (based on [Gradio](https://www.gradio.app/)) to make development easier, optimize resource management, and speed up inference.

The code has forked from[ lllyasviel ]( https://github.com/lllyasviel/stable-diffusion-webui-forge ), you can find more detail from there .

The code tweaked based on [stable-diffusion-webui-directml](https://github.com/lshqqytiger/stable-diffusion-webui-directml) which nativly support zluda on amd .

If you want learn what changes between them . I only touch files `cmd_args.py`,`shared_init.py`,`launch_utils.py` and add` zluda.py`, All those changes code came  from  [ lshqqytiger]( https://github.com/lshqqytiger)  , Credits should goes to lshqqytiger and lllyasviel.
INSTALL ,You can refer to [ sd.next zluda install guide]( https://github.com/vladmandic/automatic/wiki/ZLUDA) for more about information.

Update ,lshqqytiger also start a new fork for [Forge](https://github.com/lshqqytiger/stable-diffusion-webui-amdgpu-forge) he has a better support for this . you may try his fork also .

## 1, Installing ZLUDA for AMD GPUs in Windows.

## Compatible GPUs
A list of compatible GPUs can be found[ here](https://rocm.docs.amd.com/projects/install-on-windows/en/develop/reference/system-requirements.html). If your GPU is not on the list, then you may be need to build your own rocblas library to use ZLUDA or used builded library by others (eg,[ this ]( https://github.com/brknsoul/ROCmLibs/raw/main/ROCmLibs.zip?download=).
( Note: how to build robclas ? follow the last step)

Also a list of builded rocblas aviable [ here](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU)

Note: If you have an integrated GPU (iGPU), you may need to disable it, or use the HIP_VISIBLE_DEVICES environment variable. OR if you IGPU exactly The apu amd 780M , download this[ file ](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU)
For example , Place `rocblas.dll `into `C:\Program Files\AMD\ROCm\5.7\bin`( this fold will appear after install HIP SKD  in next step) replace the origianl one ,replace library within` rocblas\library` , the orignally library can be rename to something else , like , "origlibrary" in case for other uses.then Reboot PC

## Install HIP SDK
Download [ HIP SDK 5.7](https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html)


## Add folders to PATH
Download from[ here](https://github.com/lshqqytiger/ZLUDA/releases/)
Add the ZLUDA folder* and %HIP_PATH%bin to your [PATH.](https://github.com/brknsoul/ROCmLibs/wiki/Adding-folders-to-PATH)
(note, you don't need to rename zluda files cublas.dll to cublas64_11.dll ,cusparse to cusparse64_11.dll and replace the one in vevn folder like other tutorial because the zluda had already detecd in patch in script)

## 2, Install ;

	git clone https://github.com/likelovewant/stable-diffusion-webui-forge-on-amd.git

then start by run : 

	webui.bat --use-zluda



or you may try add extra 

	--cuda-stream --pin-shared-memory  
 
 to test the speed .
## update; In the root directory
	git pull

 if your edited any of the file, try below.

 	git stash  
	git pull origin master  
	git stash pop 

 Then apply the change in your code editor( eg VS code) ,where `git stash pop`listed.

if you encounter error  due to the 'pydantic.fields' (.\venv\lib\site-packages\pydantic\fields.py)

This error is caused by insightface installing modules that newest.
it's happens by manually installing insightface, can be resloved by install `pydantic==1.10.15`

Open command prompt in root of this repo folder.

Run these commands one after the other;
```
venv\Scripts\activate
pip install insightface
pip install albumentations==1.4.3
pip install pydantic==1.10.15

```
Close command prompt and run webui-user.bat again.

### if you need build roclabs ,please get support by this [guide](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU/wiki) .













