NAME=smoke_sim_demo03
bin/obj2sdf -i resources/dragon.obj -o dragon.sdf
bin/smoke_sim -e 3 -r 200 -f 300 -o $NAME -l $NAME.log
