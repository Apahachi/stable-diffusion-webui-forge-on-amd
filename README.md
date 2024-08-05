# Under Construction

WebUI Forge is under a week of major revision right now between 2024 Aug 1 and Aug 7. To join the test, just update to the latest unstable version.

**Current Progress (2024 Aug 3):** Backend Rewrite is 85% finished - remaining 30 hours to begin making it stable; remaining 48 hours to begin supporting many new things.

For downloading previous versions, see [Previous Versions](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/849).

# Stable Diffusion WebUI Forge

Stable Diffusion WebUI Forge is a platform on top of [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) (based on [Gradio](https://www.gradio.app/)) to make development easier, optimize resource management, speed up inference, and study experimental features.

The code has forked from[ lllyasviel ]( https://github.com/lllyasviel/stable-diffusion-webui-forge ), you can find more detail from there .

The code tweaked based on [stable-diffusion-webui-directml](https://github.com/lshqqytiger/stable-diffusion-webui-directml) which nativly support zluda on amd .

If you want learn what changes between them . I only touch files `cmd_args.py`,`shared_init.py`,`launch_utils.py` and add` zluda.py`, All those changes code came  from  [ lshqqytiger]( https://github.com/lshqqytiger)  , Credits should goes to lshqqytiger and lllyasviel.

**Update**

lshqqytiger has started a new fork of Forge, available at
[https://github.com/lshqqytiger/stable-diffusion-webui-amdgpu-forge](https://github.com/lshqqytiger/stable-diffusion-webui-amdgpu-forge). This fork provides better support and is recommended to use.

Initially, the purpose of creating a fork was to make Forge compatible with AMD before lshqqytiger's new fork. Now
that Lee's fork is available, it is highly recommended to use his version for both HIP SDK 5.7 and 6.1.2.

Please note that this repository currently only supports HIP SDK 5.7.

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

Close command prompt and run webui-user.bat again.

### if you need build roclabs ,please get support by this [guide](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU/wiki) .













### Previous Versions

You can download previous versions [here](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/849).

# Forge Status

Based on manual test one-by-one:

| Component                                         | Status  | Last Test    |
|---------------------------------------------------|---------|--------------|
| Basic Diffusion                                   | Normal  | 2024 July 27 |
| GPU Memory Management System                      | Normal  | 2024 July 27 |
| LoRAs                                             | Normal  | 2024 July 27 |
| All Preprocessors                                 | Normal  | 2024 July 27 |
| All ControlNets                                   | Normal  | 2024 July 27 |
| All IP-Adapters                                   | Normal  | 2024 July 27 |
| All Instant-IDs                                   | Normal  | 2024 July 27 |
| All Reference-only Methods                        | Normal  | 2024 July 27 |
| All Integrated Extensions                         | Normal  | 2024 July 27 |
| Popular Extensions (Adetailer, etc)               | Normal  | 2024 July 27 |
| Gradio 4 UIs                                      | Normal  | 2024 July 27 |
| Gradio 4 Forge Canvas                             | Normal  | 2024 July 27 |
| LoRA/Checkpoint Selection UI for Gradio 4         | Normal  | 2024 July 27 |
| Photopea/OpenposeEditor/etc for ControlNet        | Normal  | 2024 July 27 |
| Wacom 128 level touch pressure support for Canvas | Normal  | 2024 July 15 |
| Microsoft Surface touch pressure support for Canvas | Broken, pending fix  | 2024 July 29 |

Feel free to open issue if anything is broken and I will take a look every several days. If I do not update this "Forge Status" then it means I cannot reproduce any problem. In that case, fresh re-install should help most.

# Under Construction

This Readme is under construction ... more docs/wiki coming soon ...
