./start_gps.py &
echo "gps started"
./start_compass.py &
echo "compass started"
sleep 1 # let the devices settle
./start_route.py &
echo "route started"
./start_talker.py  2> /dev/null &
echo "position talker started"
./start_logger.py  &
echo "logging started"
echo "starting menu"
./start_menu.py < /dev/tty1   2> /dev/null 
