import os
import subprocess
import xml.etree.ElementTree as ET
import pkgutil
import pybullet as pb
 
 
_client_id = pb.connect(pb.DIRECT)

# These code snippet is used to force EGL to use the NVIDIA GPU
# if that is not available, avoid to set EGL_VISIBLE_DEVICES by commenting the `os.environ['EGL_VISIBLE_DEVICES'] = str(dev_id)`
# or setting use_nvidia_gpu to False
# line and the `eglRenderer` will work fine with software emulated OpenGL
use_nvidia_gpu = True

if use_nvidia_gpu:
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    assert 'CUDA_VISIBLE_DEVICES' in os.environ
    devices = os.environ.get('CUDA_VISIBLE_DEVICES', ).split(',')
    device_id = str(devices[-1])
    out = subprocess.check_output(['nvidia-smi', '--id='+device_id, '-q', '--xml-format'])
    tree = ET.fromstring(out)
    gpu = tree.findall('gpu')[0]
    dev_id = gpu.find('minor_number').text
    os.environ['EGL_VISIBLE_DEVICES'] = str(dev_id)

egl = pkgutil.get_loader('eglRenderer')
assert egl
pb.loadPlugin(egl.get_filename(), "_eglRendererPlugin", physicsClientId=_client_id) # Fails here
