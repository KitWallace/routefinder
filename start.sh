./start_gps.py &
./start_compass.py &
sleep 5 # let the devices settle
./start_route.py $1 &
./start_position_talker.py  2> /dev/null &
./start_logger.py $3 &
./start_menu.py $2 < /dev/tty1   2> /dev/null
