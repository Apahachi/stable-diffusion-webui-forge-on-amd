

# Stable Diffusion WebUI Forge On AMD GPU

Stable Diffusion WebUI Forge is a platform on top of [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) (based on [Gradio](https://www.gradio.app/) <a href='https://github.com/gradio-app/gradio'><img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>) to make development easier, optimize resource management, speed up inference, and study experimental features.

The code has forked from[ lllyasviel ]( https://github.com/lllyasviel/stable-diffusion-webui-forge ), you can find more detail from there .

The code tweaked based on [stable-diffusion-webui-directml](https://github.com/lshqqytiger/stable-diffusion-webui-directml) which nativly support zluda on amd .

If you want learn what changes between them . I only touch files `cmd_args.py`,`shared_init.py`,`launch_utils.py` and add` zluda.py`, All those changes code came  from  [ lshqqytiger(Seunghoon Lee)]( https://github.com/lshqqytiger)  , Credits should goes to lshqqytiger and lllyasviel.

**Update**

lshqqytiger has started a new fork of Forge, available at
[https://github.com/lshqqytiger/stable-diffusion-webui-amdgpu-forge](https://github.com/lshqqytiger/stable-diffusion-webui-amdgpu-forge). This fork provides better support and advance function and is recommended to use.

Initially, the purpose of start this fork share shqqytiger'zluda approach to Forge on AMD. and all those code from Lee .Now that Lee's fork is available, it is highly recommended to use his version.This fork is keeped in order to tweak around something new without interupt local `amdgpu-forge`.


## 1, Installing ZLUDA for AMD GPUs in Windows.

## Compatible GPUs
A list of compatible GPUs can be found[ here](https://rocm.docs.amd.com/projects/install-on-windows/en/develop/reference/system-requirements.html). If your GPU is not on the list, then you may be need to build your own rocblas library to use ZLUDA or used builded library by others (eg,[ this ]( https://github.com/brknsoul/ROCmLibs/raw/main/ROCmLibs.zip?download=).
( Note: how to build robclas ? follow this [guide](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU/wiki))

Also a list of builded rocblas available [ here](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU) ( actually most of them)

Note: If you have an integrated GPU (iGPU), you may need to disable it, or use the HIP_VISIBLE_DEVICES environment variable. OR if you IGPU exactly The apu amd 780M , download this[ file ](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU)
For example , Place `rocblas.dll `into `C:\Program Files\AMD\ROCm\5.7\bin`( this fold will appear after install HIP SKD  in next step,chat the path if you are using different ROCM version ，eg 6.1.2，`C:\Program Files\AMD\ROCm\6.1\bin`) replace the origianl one ,replace library within` rocblas\library` , the orignally library can be rename to something else , like , "origlibrary" in case for other uses.

## Install HIP SDK
Download [ HIP SDK 5.7/6.1.2](https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html)


## Add folders to PATH
Add the HIP PATH 5.7/bin or 6.1/bin or 6.2/bin folder* and %HIP_PATH%bin to your [PATH.]

Skip zluda steps （ merge lee’s new zluda files ，it fully automatic now）
Download from[ here](https://github.com/lshqqytiger/ZLUDA/releases/)
Add the ZLUDA folder* and %HIP_PATH%bin to your [PATH.](https://github.com/brknsoul/ROCmLibs/wiki/Adding-folders-to-PATH)
(note, you don't need to rename zluda files `cublas.dll` to `cublas64_11.dll` ,cusparse to `cusparse64_11.dll` and replace the one in vevn folder like other tutorial because the zluda had already detecd in patch in script)

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

Close command prompt and run `webui-user.bat` again.
## SD3.5
by run :

	git checkout sd35
 
 click `webui-user.bat` to start program,if you want to Switch back to origin, by run :
 	
  	git checkout main

Tested work on limited sd3.5 large fp 8 models with Euler, SGM_Uniform . eg.[SD3.5_fp8_SS_ALL.marduk191]( https://hf-mirror.com/marduk191/SD3.5_fp8_SS_ALL.marduk191/tree/main),
The speed is almost same as flux.
If had vram or ram overload in recent update. run

	git checkout 2a855b3d9554fa0a2ca7bd59820890063bd9bde9

It will switch to previous proper commit ,make sure to swithc back to `main` before update.

## expertimental teacache with a 2x speed in flux .
( [sd-forge-teacache extension](https://github.com/likelovewant/sd-forge-teacache) and/or[DenOfEquity/sd-forge-blockcache](https://github.com/DenOfEquity/sd-forge-blockcache))


Default at `0.4 for 1.8x speedup`,if you want to change the speed by mannuly change  ,rel_l1_thresh=0.8 , 0.6 # `0.25 for 1.5x` speedup, `0.4 for 1.8x` speedup, `0.6 for 2.0x` speedup, `0.8 for 2.25x` speedup

Note：For some old cards ,eg rx580 (gfx803),need to downgrad to pytorch to 2.2.1 . by run 
```
python -m venv venv
 .\venv\Scripts\activate
pip install torch==2.2.1 torchvision --index-url https://download.pytorch.org/whl/cu118

```
if want do update default pytorch to torch 2.4 or 2.5 ...

by build from ROCm official's hipblaslt windows branch or download hipblaslt from [hipblaslt-rocmlibs](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU/releases/download/v0.6.2.4/hipblaslt-rocmlibs-for-gfx1100-gfx1101-gfx1102-gfx1103-gfx1150-for.hip6.2.7z), currently only support gfx110x series on windows .
 Place `hipblaslt.dll `into `C:\Program Files\AMD\ROCm\6.2\bin`( `C:\Program Files\AMD\ROCm\6.2\bin`),creat a `hipblaslt` directory replace library within` hipblaslt\library` , download the [ZLUDA-nightly-windows-rocm6-amd64.zip](https://github.com/lshqqytiger/ZLUDA/releases/download/rel.c4994b3093e02231339d22e12be08418b2af781f/ZLUDA-nightly-windows-rocm6-amd64.zip) mannuly ,unzip and place in the .zluda directory in default AMD FORGE directory .doing nothing .

 ```
python -m venv venv
 .\venv\Scripts\activate
pip install torch==2.4.1 torchvision --index-url https://download.pytorch.org/whl/cu118

```
then click the `webui-user.bat` to start . 

> [!TIP]
> Flux Use on Zluda ，tested work on `Flux-dev-fp8.safetensors`, and `t5xxl_fp8_e4m3fn.safetensors` combination ,
`Flux1-dev-Q4_K_S.gguf`，`flux1-dev-Q6_K.gguf `works and others like `Q2,Q3,Q5` also should works except maybe slower than no-quantized files ,`.safetensors`.
>  A list of quantized models in GGUF file available at [FLUX.1-dev-gguf](https://huggingface.co/city96/FLUX.1-dev-gguf/tree/main) .
>  A list of quantized` T5 v1.1 XXL` encoder model in `GGUF` file available at [t5-v1_1-xxl-encoder-gguf](https://huggingface.co/city96/t5-v1_1-xxl-encoder-gguf/tree/main).
>  Flux loras use need set `Automatic (fp16 LoRA)` in `Diffusion in Low Bits`. Test works for many loras now ,however there are some lora still failed to work.）

if there is not enough vram , you may increase your virtual memory or use quantized models like Q4 or less .

Below content from  [ lllyasviel's upstream main  ]( https://github.com/lllyasviel/stable-diffusion-webui-forge )

Forge is currently based on SD-WebUI 1.10.1 at [this commit](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/82a973c04367123ae98bd9abdf80d9eda9b910e2). (Because original SD-WebUI is almost static now, Forge will sync with original WebUI every 90 days, or when important fixes.)

News are moved to this link: [Click here to see the News section](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/main/NEWS.md)

# Quick List

[Gradio 4 UI Must Read (TLDR: You need to use RIGHT MOUSE BUTTON to move canvas!)](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/853)

[Flux Tutorial (BitsandBytes Models, NF4, "GPU Weight", "Offload Location", "Offload Method", etc)](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/981)

[Flux Tutorial 2 (Seperated Full Models, GGUF, Technically Correct Comparison between GGUF and NF4, etc)](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1050)

[Forge Extension List and Extension Replacement List (Temporary)](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1754)

[How to make LoRAs more precise on low-bit models; How to Skip" Patching LoRAs"; How to only load LoRA one time rather than each generation; How to report LoRAs that do not work](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1038)

[Report Flux Performance Problems (TLDR: DO NOT set "GPU Weight" too high! Lower "GPU Weight" solves 99% problems!)](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1181)

[How to solve "Connection errored out" / "Press anykey to continue ..." / etc](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1474)

[(Save Flux BitsandBytes UNet/Checkpoint)](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1224#discussioncomment-10384104)

[LayerDiffuse Transparent Image Editing](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/854)

[Tell us what is missing in ControlNet Integrated](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/932)

[(Policy) Soft Advertisement Removal Policy](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1286)

(Flux BNB NF4 / GGUF Q8_0/Q5_0/Q5_1/Q4_0/Q4_1 are all natively supported with GPU weight slider and Quene/Async Swap toggle and swap location toggle. All Flux BNB NF4 / GGUF Q8_0/Q5_0/Q4_0 have LoRA support.)

# Installing Forge

**Just use this one-click installation package (with git and python included).**

[>>> Click Here to Download One-Click Package (CUDA 12.1 + Pytorch 2.3.1) <<<](https://github.com/lllyasviel/stable-diffusion-webui-forge/releases/download/latest/webui_forge_cu121_torch231.7z)

Some other CUDA/Torch Versions:

[Forge with CUDA 12.1 + Pytorch 2.3.1](https://github.com/lllyasviel/stable-diffusion-webui-forge/releases/download/latest/webui_forge_cu121_torch231.7z) <- **Recommended**

[Forge with CUDA 12.4 + Pytorch 2.4](https://github.com/lllyasviel/stable-diffusion-webui-forge/releases/download/latest/webui_forge_cu124_torch24.7z) <- **Fastest**, but MSVC may be broken, xformers may not work

[Forge with CUDA 12.1 + Pytorch 2.1](https://github.com/lllyasviel/stable-diffusion-webui-forge/releases/download/latest/webui_forge_cu121_torch21.7z) <- the previously used old environments

After you download, you uncompress, use `update.bat` to update, and use `run.bat` to run.

Note that running `update.bat` is important, otherwise you may be using a previous version with potential bugs unfixed.

![image](https://github.com/lllyasviel/stable-diffusion-webui-forge/assets/19834515/c49bd60d-82bd-4086-9859-88d472582b94)

### Advanced Install

If you are proficient in Git and you want to install Forge as another branch of SD-WebUI, please see [here](https://github.com/continue-revolution/sd-webui-animatediff/blob/forge/master/docs/how-to-use.md#you-have-a1111-and-you-know-git). In this way, you can reuse all SD checkpoints and all extensions you installed previously in your OG SD-WebUI, but you should know what you are doing.

If you know what you are doing, you can also install Forge using same method as SD-WebUI. (Install Git, Python, Git Clone the forge repo `https://github.com/lllyasviel/stable-diffusion-webui-forge.git` and then run webui-user.bat).

### Previous Versions

You can download previous versions [here](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/849).

# Forge Status

Based on manual test one-by-one:

| Component                                           | Status                                      | Last Test    |
|-----------------------------------------------------|---------------------------------------------|--------------|
| Basic Diffusion                                     | Normal                                      | 2024 Aug 26  |
| GPU Memory Management System                        | Normal                                      | 2024 Aug 26  |
| LoRAs                                               | Normal                                      | 2024 Aug 26  |
| All Preprocessors                                   | Normal                                      | 2024 Aug 26  |
| All ControlNets                                     | Normal                                      | 2024 Aug 26  |
| All IP-Adapters                                     | Normal                                      | 2024 Aug 26  |
| All Instant-IDs                                     | Normal                                      | 2024 July 27 |
| All Reference-only Methods                          | Normal                                      | 2024 July 27 |
| All Integrated Extensions                           | Normal                                      | 2024 July 27 |
| Popular Extensions (Adetailer, etc)                 | Normal                                      | 2024 July 27 |
| Gradio 4 UIs                                        | Normal                                      | 2024 July 27 |
| Gradio 4 Forge Canvas                               | Normal                                      | 2024 Aug 26  |
| LoRA/Checkpoint Selection UI for Gradio 4           | Normal                                      | 2024 July 27 |
| Photopea/OpenposeEditor/etc for ControlNet          | Normal                                      | 2024 July 27 |
| Wacom 128 level touch pressure support for Canvas   | Normal                                      | 2024 July 15 |
| Microsoft Surface touch pressure support for Canvas | Broken, pending fix                         | 2024 July 29 |
| ControlNets (Union)                                 | Not implemented yet, pending implementation | 2024 Aug 26  |
| ControlNets (Flux)                                  | Not implemented yet, pending implementation | 2024 Aug 26  |
| API endpoints (txt2img, img2img, etc)               | Normal, but pending improved Flux support   | 2024 Aug 29  |
| OFT LoRAs                                           | Broken, pending fix                         | 2024 Sep 9   |

Feel free to open issue if anything is broken and I will take a look every several days. If I do not update this "Forge Status" then it means I cannot reproduce any problem. In that case, fresh re-install should help most.

# UnetPatcher

Below are self-supported **single file** of all codes to implement FreeU V2.

See also `extension-builtin/sd_forge_freeu/scripts/forge_freeu.py`:

```python
import torch
import gradio as gr

from modules import scripts


def Fourier_filter(x, threshold, scale):
    # FFT
    x_freq = torch.fft.fftn(x.float(), dim=(-2, -1))
    x_freq = torch.fft.fftshift(x_freq, dim=(-2, -1))

    B, C, H, W = x_freq.shape
    mask = torch.ones((B, C, H, W), device=x.device)

    crow, ccol = H // 2, W // 2
    mask[..., crow - threshold:crow + threshold, ccol - threshold:ccol + threshold] = scale
    x_freq = x_freq * mask

    # IFFT
    x_freq = torch.fft.ifftshift(x_freq, dim=(-2, -1))
    x_filtered = torch.fft.ifftn(x_freq, dim=(-2, -1)).real

    return x_filtered.to(x.dtype)


def patch_freeu_v2(unet_patcher, b1, b2, s1, s2):
    model_channels = unet_patcher.model.diffusion_model.config["model_channels"]
    scale_dict = {model_channels * 4: (b1, s1), model_channels * 2: (b2, s2)}
    on_cpu_devices = {}

    def output_block_patch(h, hsp, transformer_options):
        scale = scale_dict.get(h.shape[1], None)
        if scale is not None:
            hidden_mean = h.mean(1).unsqueeze(1)
            B = hidden_mean.shape[0]
            hidden_max, _ = torch.max(hidden_mean.view(B, -1), dim=-1, keepdim=True)
            hidden_min, _ = torch.min(hidden_mean.view(B, -1), dim=-1, keepdim=True)
            hidden_mean = (hidden_mean - hidden_min.unsqueeze(2).unsqueeze(3)) / (hidden_max - hidden_min).unsqueeze(2).unsqueeze(3)

            h[:, :h.shape[1] // 2] = h[:, :h.shape[1] // 2] * ((scale[0] - 1) * hidden_mean + 1)

            if hsp.device not in on_cpu_devices:
                try:
                    hsp = Fourier_filter(hsp, threshold=1, scale=scale[1])
                except:
                    print("Device", hsp.device, "does not support the torch.fft.")
                    on_cpu_devices[hsp.device] = True
                    hsp = Fourier_filter(hsp.cpu(), threshold=1, scale=scale[1]).to(hsp.device)
            else:
                hsp = Fourier_filter(hsp.cpu(), threshold=1, scale=scale[1]).to(hsp.device)

        return h, hsp

    m = unet_patcher.clone()
    m.set_model_output_block_patch(output_block_patch)
    return m


class FreeUForForge(scripts.Script):
    sorting_priority = 12  # It will be the 12th item on UI.

    def title(self):
        return "FreeU Integrated"

    def show(self, is_img2img):
        # make this extension visible in both txt2img and img2img tab.
        return scripts.AlwaysVisible

    def ui(self, *args, **kwargs):
        with gr.Accordion(open=False, label=self.title()):
            freeu_enabled = gr.Checkbox(label='Enabled', value=False)
            freeu_b1 = gr.Slider(label='B1', minimum=0, maximum=2, step=0.01, value=1.01)
            freeu_b2 = gr.Slider(label='B2', minimum=0, maximum=2, step=0.01, value=1.02)
            freeu_s1 = gr.Slider(label='S1', minimum=0, maximum=4, step=0.01, value=0.99)
            freeu_s2 = gr.Slider(label='S2', minimum=0, maximum=4, step=0.01, value=0.95)

        return freeu_enabled, freeu_b1, freeu_b2, freeu_s1, freeu_s2

    def process_before_every_sampling(self, p, *script_args, **kwargs):
        # This will be called before every sampling.
        # If you use highres fix, this will be called twice.

        freeu_enabled, freeu_b1, freeu_b2, freeu_s1, freeu_s2 = script_args

        if not freeu_enabled:
            return

        unet = p.sd_model.forge_objects.unet

        unet = patch_freeu_v2(unet, freeu_b1, freeu_b2, freeu_s1, freeu_s2)

        p.sd_model.forge_objects.unet = unet

        # Below codes will add some logs to the texts below the image outputs on UI.
        # The extra_generation_params does not influence results.
        p.extra_generation_params.update(dict(
            freeu_enabled=freeu_enabled,
            freeu_b1=freeu_b1,
            freeu_b2=freeu_b2,
            freeu_s1=freeu_s1,
            freeu_s2=freeu_s2,
        ))

        return
```

See also [Forge's Unet Implementation](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/main/backend/nn/unet.py).

# Under Construction

WebUI Forge is now under some constructions, and docs / UI / functionality may change with updates.
