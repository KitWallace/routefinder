./start_gps.py &
./start_compass.py &
./start_barometer.py &
sleep 1 # let the devices settle
./start_route.py &
./start_route_follower.py &
./start_talker.py  2> /dev/null &
./start_position_logger.py  &
./start_weather_logger.py  &
./start_book_reader.py &
./start_menu.py < /dev/tty1   2> /dev/null 
