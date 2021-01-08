

#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import cv2
import cvlib as cv
from cvlib.object_detection import YOLO
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
yolo = YOLO("yolov3-tiny.weights", "yolov3-tiny.cfg", "yolov3_classes.txt")
while True:
	message = socket.recv()
	im = cv2.imread('in2.jpeg')
	bbox, label, conf = yolo.detect_objects(im)
	socket.send(str.encode(str(label.count('car'))))  