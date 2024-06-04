

# Stable Diffusion WebUI Forge on AMD GPU

Stable Diffusion WebUI Forge is a platform on top of [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) (based on [Gradio](https://www.gradio.app/)) to make development easier, optimize resource management, and speed up inference.

The code has forked from[ lllyasviel ]( https://github.com/lllyasviel/stable-diffusion-webui-forge ), you can find more detail from there .

The code tweaked based on  ( `git clone https://githubfast.com/lshqqytiger/stable-diffusion-webui-directml.git` ) which nativly support zluda on amd .

If you want learn what changes between them . I only touch files `cmd_args.py`,`shared_init.py`,`launch_utils.py` and add` zluda.py`, All those changes code came  from  [ lshqqytiger]( https://github.com/lshqqytiger)  , Credits should goes to lshqqytiger and lllyasviel.
INSTALL ,You can refer to [ sd.next zluda install guide]( https://github.com/vladmandic/automatic/wiki/ZLUDA) for more about information.

## 1, Installing ZLUDA for AMD GPUs in Windows.

## Compatible GPUs
A list of compatible GPUs can be found[ here](https://rocm.docs.amd.com/projects/install-on-windows/en/develop/reference/system-requirements.html). If your GPU is not on the list, then you may be need to build your own rocblas library to use ZLUDA or used builded library by others (eg,[ this ]( https://github.com/brknsoul/ROCmLibs/raw/main/ROCmLibs.zip?download=).
( Note: how to build robclas ? follow the last step)

Also a list of builded rocblas aviable [ here](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU)

Note: If you have an integrated GPU (iGPU), you may need to disable it, or use the HIP_VISIBLE_DEVICES environment variable. OR if you IGPU exactly The apu amd 780M , download this[ file ](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU)
For example , Place `rocblas.dll `into `C:\Program Files\AMD\ROCm\5.7\bin`( this fold will appear after install HIP SKD  in next step) replace the origianl one ,replace library within` rocblas\library` , the orignally library can be rename to something else , like , "origlibrary" in case for other uses.then Reboot PC

## Install HIP SDK
Download [ HIP SDK 5.7](https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html)

## Install Perl
Install [Perl]( https://strawberryperl.com/)

The hipconfig command does not work without Perl

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
## update;In the root folder 
	git pull
 if your edited any of the file, try below.

 	git stash  
	git pull origin master  
	git stash pop 

 Then apply the change in your code editor( eg VS code) ,where `git stash pop`listed.


## if you need build roclabs ,please get support by this [guide](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU/wiki) .













