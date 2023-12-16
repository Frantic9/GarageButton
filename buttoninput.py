from sendmessages import send_message
import RPi.GPIO as GPIO #unresolved on desktop
import sys

if __name__ == '__main__':
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(10, GPIO.RISING, callback=send_message(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    GPIO.cleanup()
