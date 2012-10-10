./start_gps.py &
./start_compass.py &
sleep 1 # let the devices settle
./start_route.py &
./start_position_talker.py  2> /dev/null &
./start_logger.py  &
./start_menu.py < /dev/tty1   2> /dev/null
