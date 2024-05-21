import os
import subprocess
import xml.etree.ElementTree as ET
import pkgutil
import pybullet as pb
 
 
_client_id = pb.connect(pb.DIRECT)
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
