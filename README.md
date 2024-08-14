

# Stable Diffusion WebUI Forge On AMD GPU

Stable Diffusion WebUI Forge is a platform on top of [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) (based on [Gradio](https://www.gradio.app/) <a href='https://github.com/gradio-app/gradio'><img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>) to make development easier, optimize resource management, speed up inference, and study experimental features.

The code has forked from[ lllyasviel ]( https://github.com/lllyasviel/stable-diffusion-webui-forge ), you can find more detail from there .

The code tweaked based on [stable-diffusion-webui-directml](https://github.com/lshqqytiger/stable-diffusion-webui-directml) which nativly support zluda on amd .

If you want learn what changes between them . I only touch files `cmd_args.py`,`shared_init.py`,`launch_utils.py` and add` zluda.py`, All those changes code came  from  [ lshqqytiger(Seunghoon Lee)]( https://github.com/lshqqytiger)  , Credits should goes to lshqqytiger and lllyasviel.

**Update**

lshqqytiger has started a new fork of Forge, available at
[https://github.com/lshqqytiger/stable-diffusion-webui-amdgpu-forge](https://github.com/lshqqytiger/stable-diffusion-webui-amdgpu-forge). This fork provides better support and is recommended to use.

Initially, the purpose of creating a fork was to make Forge compatible with AMD before lshqqytiger's new fork. and the code from Lee .Now that Lee's fork is available, it is highly recommended to use his version for both HIP SDK 5.7 and 6.1.2.


## 1, Installing ZLUDA for AMD GPUs in Windows.

## Compatible GPUs
A list of compatible GPUs can be found[ here](https://rocm.docs.amd.com/projects/install-on-windows/en/develop/reference/system-requirements.html). If your GPU is not on the list, then you may be need to build your own rocblas library to use ZLUDA or used builded library by others (eg,[ this ]( https://github.com/brknsoul/ROCmLibs/raw/main/ROCmLibs.zip?download=).
( Note: how to build robclas ? follow the last step)

Also a list of builded rocblas aviable [ here](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU) ( actually most of them)

Note: If you have an integrated GPU (iGPU), you may need to disable it, or use the HIP_VISIBLE_DEVICES environment variable. OR if you IGPU exactly The apu amd 780M , download this[ file ](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU)
For example , Place `rocblas.dll `into `C:\Program Files\AMD\ROCm\5.7\bin`( this fold will appear after install HIP SKD  in next step) replace the origianl one ,replace library within` rocblas\library` , the orignally library can be rename to something else , like , "origlibrary" in case for other uses.

## Install HIP SDK
Download [ HIP SDK 5.7](https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html)


## Add folders to PATH
Add the HIP PATH 5.7/bin folder* and %HIP_PATH%bin to your [PATH.]

Skip zluda steps （ merge lee’s new zluda files ，it fully automatic now）
Download from[ here](https://github.com/lshqqytiger/ZLUDA/releases/)
Add the ZLUDA folder* and %HIP_PATH%bin to your [PATH.](https://github.com/brknsoul/ROCmLibs/wiki/Adding-folders-to-PATH)
(note, you don't need to rename zluda files cublas.dll to cublas64_11.dll ,cusparse to cusparse64_11.dll and replace the one in vevn folder like other tutorial because the zluda had already detecd in patch in script)

## 2, Install ;

	git clone https://github.com/likelovewant/stable-diffusion-webui-forge-on-amd.git

then start by run : 

	webui.bat --use-zluda

or simply click `webui-user.bat`

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

Close command prompt and run webui-user.bat again.

### if you need build roclabs ,please get support by this [guide](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU/wiki) .


Forge is currently based on SD-WebUI 1.10.1 at [this commit](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/82a973c04367123ae98bd9abdf80d9eda9b910e2). (Because original SD-WebUI is almost static now, Forge will sync with original WebUI every 90 days, or when important fixes.)

Note:FLUX use ,please refer to (here)[https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1050] NT 4 currently not support zluda. please use fp8 dev models.

# Under Construction

WebUI Forge is now under some constructions, and docs / UI / functionality may change with updates.
