import os

example = 3
xml = "render/viscosity.xml"

for i in range(0, 240):
    try:
        obj = "level_set_liquid_sim_demo%02d/frame_%06d.obj" % (example, i)
        png = "level_set_liquid_sim_demo%02d/frame_%06d.png" % (example, i)
        cmd = "python scripts/render_level_set_liquid_sim.py -i %s -o %s -t %s" % (obj, png, xml)
        ret = os.system(cmd)
        if ret != 0:
            quit(-1)
    except Exception as e:
        quit(-1)
