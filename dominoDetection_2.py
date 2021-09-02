import cv2
import numpy as np

vid = cv2.VideoCapture(0)

def findCorner(contour):
    epsilon = 0.1 * cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,epsilon,True)
    points = []
    for point in approx:
        points.append([point[0][0], point[0][1]])
    return points

# domino = cv2.imread('domino.jpg')
# hsv_domino = cv2.cvtColor(domino, cv2.COLOR_BGR2HSV)
kernel = np.ones((3, 3), np.uint8)
light_red_1 = (0, 150, 50)
dark_red_1 = (10, 255, 255)
light_red_2 = (170, 150, 50)
dark_red_2 = (180, 255, 255)
light_yellow = (15, 93, 50)
dark_yellow = (45, 255, 255)

while 1:
    # video cap
    ret, domino = vid.read()
    hsv_domino = cv2.cvtColor(domino, cv2.COLOR_BGR2HSV)

    # mask
    mask_red_1 = cv2.inRange(hsv_domino, light_red_1, dark_red_1)
    mask_red_2 = cv2.inRange(hsv_domino, light_red_2, dark_red_2)
    mask_red = mask_red_1 + mask_red_2
    mask_yellow = cv2.inRange(hsv_domino, light_yellow, dark_yellow)

    # closing
    close_mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_CLOSE, kernel)
    close_mask_yellow = cv2.morphologyEx(mask_yellow, cv2.MORPH_CLOSE, kernel)

    # contours
    yellow_contours, yellow_hier = cv2.findContours(close_mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    red_contours, red_hier = cv2.findContours(close_mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # cari contour dengan luasan tertentu
    filtered_yellow_contours = []
    for yellow_contour in yellow_contours:
        if cv2.contourArea(yellow_contour) > 3000:
            filtered_yellow_contours.append(yellow_contour)
    filtered_red_contours = []
    for red_contour in red_contours:
        if cv2.contourArea(red_contour) > 1500:
            filtered_red_contours.append(red_contour)
    
    # cari titik pojok dari kotak kuning
    if len(filtered_yellow_contours) == 2:
        yellow1_points = findCorner(filtered_yellow_contours[0])
        yellow2_points = findCorner(filtered_yellow_contours[1])

        # cari nilai y maks dan min dari masing-masing kotak kuning
        yellow1YMinMax = []
        yellow2YMinMax = []
        yellow1XMinMax = []
        yellow2XMinMax = []

        temp_y_min = yellow1_points[0][1]
        temp_y_max = yellow1_points[0][1]
        temp_x_min = yellow1_points[0][1]
        temp_x_max = yellow1_points[0][1]
        for point in yellow1_points:
            if temp_y_min > point[1]:
                temp_y_min = point[1]
            if temp_y_max < point[1]:
                temp_y_max = point[1]
            if temp_x_min > point[0]:
                temp_x_min = point[0]
            if temp_x_max < point[0]:
                temp_x_max = point[0]
        yellow1YMinMax.append(temp_y_min)
        yellow1YMinMax.append(temp_y_max)
        yellow1XMinMax.append(temp_x_min)
        yellow1XMinMax.append(temp_x_max)

        temp_y_min = yellow2_points[0][1]
        temp_y_max = yellow2_points[0][1]
        temp_x_min = yellow2_points[0][1]
        temp_x_max = yellow2_points[0][1]
        for point in yellow2_points:
            if temp_y_min > point[1]:
                temp_y_min = point[1]
            if temp_y_max < point[1]:
                temp_y_max = point[1]
            if temp_x_min > point[0]:
                temp_x_min = point[0]
            if temp_x_max < point[0]:
                temp_x_max = point[0]
        yellow2YMinMax.append(temp_y_min)
        yellow2YMinMax.append(temp_y_max)
        yellow2XMinMax.append(temp_x_min)
        yellow2XMinMax.append(temp_x_max)

        # cari koordinat titik tengah dari contour merah
        if len(filtered_red_contours):
            redContourCenterOfMass = []
            for contour in filtered_red_contours:
                M = cv2.moments(contour)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                redContourCenterOfMass.append([cx, cy])

            # cari contour merah diantara nilai y min dan y max dari kotak kuning 1
            yellow1Count = 0
            for point in redContourCenterOfMass:
                if (point[1] > yellow1YMinMax[0] and point[1] < yellow1YMinMax[1]):
                    yellow1Count += 1

            # cari contour merah diantara nilai y min dan y max dari kotak kuning 2
            yellow2Count = 0
            for point in redContourCenterOfMass:
                if (point[1] > yellow2YMinMax[0] and point[1] < yellow2YMinMax[1]):
                    yellow2Count += 1

            # tampilkan hasil
            cv2.putText(domino, str(yellow1Count), (yellow1XMinMax[0] - 30, yellow1YMinMax[0]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 5, bottomLeftOrigin=False)
            cv2.putText(domino, str(yellow2Count), (yellow1XMinMax[0] - 30, yellow2YMinMax[0]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 5, bottomLeftOrigin=False)
            cv2.drawContours(domino, filtered_red_contours, -1, (255, 120, 0), 2)
            cv2.drawContours(domino, filtered_yellow_contours, -1, (255, 255, 0), 2)
            
    cv2.imshow('result', domino)

    key = cv2.waitKey(1)
    if key == 27:
        break
