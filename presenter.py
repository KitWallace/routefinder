import sys
import tty
import termios

def keypress() :
    """ decode single keypresses from either the presenter or the keyboard
        a generator
    """
    last = 0
    tty.setcbreak(sys.stdin)

    try :
      while True :
        code = ord(sys.stdin.read(1)) 
        if (code== 53 and last==91 or code==68) : 
            key = "left"
        elif (code==98 or code==66) :
            key = "down"
        elif (code==54 or code==67) :
            key = "right"
        elif (code==49 or code==65 or code==69) :
            key = "up"
        else :
            key = None
        last=code
        if not(key is None) :
            yield key

    finally :
        #turn echo back on 
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        old[3] = old[3] | termios.ECHO
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


