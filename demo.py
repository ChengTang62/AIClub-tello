from djitellopy import Tello
from time import sleep
import cv2

tello = Tello()

tello.connect()
print(tello.get_battery())

tello.streamon()

while True:
    img = tello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("img", img)
    cv2.waitKey(1)

tello.takeoff()
# sleep(2)
# tello.send_rc_control(0,50,0,0)
# sleep(2)
# tello.move_left(100)
sleep(2)
# tello.rotate_counter_clockwise(90)
# tello.move_forward(100)
# sleep(2)
tello.land()