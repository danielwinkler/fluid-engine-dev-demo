# Bunny (high-vis)
NAME=level_set_liquid_sim_demo04
bin/obj2sdf -i resources/bunny.obj -o bunny.sdf
bin/level_set_liquid_sim -e 4 -r 150 -f 300 -o $NAME -l $NAME.log
