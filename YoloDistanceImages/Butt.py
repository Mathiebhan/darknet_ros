import cv2
import numpy as np

model = 'weights/yolov4-tiny.weights'
config = 'cfg/yolov4-tiny.cfg'
min_confidence=0.14

net = cv2.dnn.readNetFromDarknet(config,model)


with open("lib/obj.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
COLORS = np.random.uniform(0, 255, size=(len(layer_names), 3))

import math

# Function to calculate the distance of object from the camera lense
def dist_calculator(startX, startY, endX, endY, box_width, box_height, img_w, img_h):
 x_3, y_3 = startX, endY - (box_height / 7)  # top left of the triangle
 # assumption: camera is rasied above the ground so considering 90% of the height of the image height
 x_1, y_1 = img_w / 2, 0.9 * img_h  # bottom of the triangle
 x_2, y_2 = endX, endY - (box_height / 7)  # top right of the triangle

 # find the angle between bottom and right point
 angle_x1_x2 = math.degrees(math.atan2(x_1 - x_2, y_1 - y_2))
 # find the angle between bottom and left point
 angle_x1_x3 = math.degrees(math.atan2(x_1 - x_3, y_1 - y_3))

 angle_right = 90 + angle_x1_x2
 angle_left = 90 - angle_x1_x3

 # total angle of view for the cigarette butt from bottom center point of the image.
 total_angle = angle_right + angle_left

 # Cigarette butt length assumed to be 0.03 meters in millimeters. This value can automated, based on the type of cigarette used.
 cig_length = 30

 distance = (cig_length * (1 / total_angle) * 57) / 1000

 print(total_angle)
 print(distance)
 return total_angle,distance

def dist(dist):
    if dist > 0.3: # if distance is greater than 2 meters 
        label = "Far"
    else:
        label = "Near"
    return label

# Loading the image of cig
image = cv2.imread('images/butt.jpg')
height, width, ch = image.shape
resize_img = cv2.resize(image, (225, 225))

blob = cv2.dnn.blobFromImage(resize_img, 1.0 / 255.0, (416, 416), True, crop=False)

net.setInput(blob)
predictions = net.forward()
probability_index = 5

for i in range(predictions.shape[0]):
 prob_arr = predictions[i][probability_index:]
 class_index = prob_arr.argmax(axis=0)
 confidence = prob_arr[class_index]
 if confidence > min_confidence:
  x_center = predictions[i][0] * width
  y_center = predictions[i][1] * height
  width_box = predictions[i][2] * width
  height_box = predictions[i][3] * height

  x1 = int(x_center - width_box * 0.5)  # Start X coordinate
  y1 = int(y_center - height_box * 0.5)  # Start Y coordinate
  x2 = int(x_center + width_box * 0.5)  # End X coordinate
  y2 = int(y_center + height_box * 0.5)  # End y coordinate

  cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 225), 2)

  if class_index == 0:  # 0 is the index of cig in the LABELS list for prediction

   roi_corners = [[0.0 * width_box, 1.0 * height],  # left, down
                  [x1 + (width_box / 5), y2 - (height_box / 7)],  # left, up
                  [x1 + 4 * (width_box / 5), y2 - (height_box / 7)],  # right, up
                  [1.0 * width, 1.0 * height]]  # right, down

   image = cv2.circle(image, (int(width), int(height)), 3, (0, 0, 255), -1)
   triangle_pts = [[width / 2, 0.9 * height],  # left, down / bottom point of the traingle
                   [x1, y2 - (height_box / 7)],  # left, up
                   [x2, y2 - (height_box / 7)],  # right, up
                   [width / 2, 0.9 * height]]  # right, down / / bottom point of the traingle
   src = np.float32(triangle_pts)
   pts = np.array(src, np.int32)
   pts = pts.reshape((-1, 1, 2))

   # drawing the triangle
   cv2.polylines(image,[pts],True,(0,255,0),2)
            
   #distance calculation
   _,distance = dist_calculator(x1,y1,x2,y2,width_box,height_box,width,height)

   #label of 'far' or 'near'
   label = dist(distance)

   # distance calculation
  
   #cv2.putText(image,layer_names[class_index]+" "+"{0:.1f}".format(confidence),(x1,y1), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)
   cv2.putText(image, "Distance: {} mm".format(round(distance, 2)), (x1, y1 + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
   print(label)

cv2.imshow("Butt", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
