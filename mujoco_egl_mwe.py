import os

os.environ["MUJOCO_GL"] = "egl"

import mujoco
import numpy as np

if "MUJOCO_GL" in os.environ:
    print(os.getenv("MUJOCO_GL"))
    print(os.getenv("PYOPENGL_PLATFORM"))

xml = """
<mujoco>
  <worldbody>
    <light name="top" pos="0 0 1"/>
    <body name="box_and_sphere" euler="0 0 -30">
      <joint name="swing" type="hinge" axis="1 -1 0" pos="-.2 -.2 -.2"/>
      <geom name="red_box" type="box" size=".2 .2 .2" rgba="1 0 0 1"/>
      <geom name="green_sphere" pos=".2 .2 .2" size=".1" rgba="0 1 0 1"/>
    </body>
  </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

with mujoco.Renderer(model) as renderer:
    renderer.enable_depth_rendering()
    mujoco.mj_forward(model, data)
    renderer.update_scene(data)

    depth = renderer.render()
    depth -= depth.min()
    depth /= 2 * depth[depth <= 1].mean()
    img = 255 * np.clip(depth, 0, 1)
