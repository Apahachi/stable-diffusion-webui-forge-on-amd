import os
import sys
import torch
from modules import zluda_installer, rocm


_topk = torch.topk
def topk(input: torch.Tensor, *args, **kwargs): # pylint: disable=redefined-builtin
    device = tensor.device
    values, indices = _topk(input.cpu(), *args, **kwargs)
    return torch.return_types.topk((values.to(device), indices.to(device),))



def do_hijack():
    torch.version.hip = rocm.version
    torch.topk = topk
    #torch.fft.fftn = fft_fftn
    #torch.fft.ifftn = fft_ifftn
    #torch.fft.rfftn = fft_rfftn
    
    #if not zluda_installer.experimental_hipBLASLt_support:
    #    torch.jit.script = jit_script
