#---------------
#Created by 1702638
#---------------
import sys, numpy, cv2


def find_object(hsv_image, lower_value, upper_value):  # sear for the object and
    # return the result(contours)
    mask = cv2.inRange(hsv_image,lower_value,upper_value)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_SIMPLE)
    return contours


def convert2HSV(RGB_image):  # quickly convert RGB to HSV
    return cv2.cvtColor(RGB_image, cv2.COLOR_BGR2HSV)


def get_mid(result,image):
    # calculating the min value
    if not check_if_empty(result):
        lny, lnx, lnc = image.shape
        xhi = -1
        xlo = lnx - 1
        yhi = -1
        ylo = lny - 1
        for found in result:
            for (i,value) in enumerate(found):
                if value[0][0] < xlo: xlo = value[0][0]
                if value[0][0] > xhi: xhi = value[0][0]
                if value[0][1] < ylo: ylo = value[0][1]
                if value[0][1] > yhi: yhi = value[0][1]
        x = (xhi+xlo)//2
        y = (yhi+ylo)//2
        return x,y
    else:
        # use as temporary maek the value as non found
        return -1,-1


def get_half_image_size(image):
    # Obtain half the image size in x and y
        ny, nx, nc = image.shape
        return  nx/2


def get_distance(lx,rx,l_image,r_image):
    if lx == -1 or rx ==-1:
        return 0
    else:
        #formula distance = (Baseline * focal length)/(xL-xR)
        #xL or xR = image x location - half the image size in x
        l_centre = get_half_image_size(l_image)
        r_centre = get_half_image_size(r_image)
        distance = (3500 * 12) / (((lx - l_centre) * (10 ** (-5))) -
                                  ((rx - r_centre) * (10 ** (-5))))
        return distance


def check_if_empty(result):
    # to check if the contours is empty
    if len(result) == 0:
        return True
    else:
        return False


def calculate_slope(point_list):
    # calculate the using 2 point (X,Z)
    slope_list = []
    for i in range(len(point_list)-1):
        try:
            slope = (point_list[i+1][1]-point_list[i][1])/(point_list[i+1][0]-point_list[i][0])
            slope_list.append(slope)
        except Exception as e:
            slope_list.append(0)
    return slope_list


def check_difference(slope_list):
    #calculate the change of slope and append it to a list
    change_slope = []
    for i in range(len(slope_list)-1):
        if slope_list[i+1] > 0 and slope_list[i] >0:
            change = slope_list[i+1] - slope_list[i]
            change_slope.append(change)
    return change_of_slope


def display_result(frame,red,green,blue,yellow,orange,aqua,white):
    if frame == 0:# print the header if its the first frame
        print('Frame \t identity \t distance')
    #print distance of its not equal to 0(the object doesn't
    # appear in left or right image)
    if red != 0:
        print('\t%d \t red    \t %s' % (frame, "{:.2e}".format(red)))
    if green != 0:
        print('\t%d \t green  \t %s' % (frame, "{:.2e}".format(green)))
    if blue != 0:
        print('\t%d \t blue   \t %s' % (frame, "{:.2e}".format(blue)))
    if yellow != 0:
        print('\t%d \t yellow \t %s' % (frame, "{:.2e}".format(yellow)))
    if orange != 0:
        print('\t%d \t orange \t %s' % (frame, "{:.2e}".format(orange)))
    if aqua != 0:
        print('\t%d \t aqua   \t %s' % (frame, "{:.2e}".format(aqua)))
    if white != 0:
        print('\t%d \t white  \t %s' % (frame, "{:.2e}".format(white)))
    # print('---------------------------------------------------')


def get_X_left(xL,Z):
    return (3600-(((xL*(10**(-5)))*Z)/12))


## da main method
if __name__ == '__main__':
    ufo = []
    green_point =[]
    green_slope = []
    blue_point = []
    blue_slope = []
    aqua_point = []
    aqua_slope = []
    red_point = []
    red_slope = []
    orange_point = []
    orange_slope = []
    yellow_point = []
    yellow_slope = []
    white_point = []
    white_slope = []
    change_of_slope = []
    nframes = int(sys.argv[1])
    for frame in range(0, nframes):
        fn_left = sys.argv[2] % frame
        fn_right = sys.argv[3] % frame
        left_img = cv2.imread (fn_left)
        right_img = cv2.imread (fn_right)

# -------------------------------------------------------------------------------
# convert RGB to HSV so that the brightness will not affect the
# colour value (avoid getting strange colour)
        # convert RGB to HSV so that the brightness will not affect the colour value (avoid getting strange colour)
        left_hsv = convert2HSV(left_img)
        right_hsv = convert2HSV(right_img)
        """
        reference Hue and saturation value per coloured object (according to the
        FAQ we can assume test images used for assessment have the same colour 
        objects (meteors and perhaps UFOs) as the imagery given out 
        The approach used in this assigment is making a colour filter for each 
        object and use find counter and use find counter to identify the object
        43,100 orange  60,100 yellow  120,100 green  0,0 white
        240,100 blue  180,100 aqua 0,100 red
        -----------------------------------------------------------------------
        set colour filter for each object
        """
        lower_blue = numpy.array([120,50,50])
        upper_blue = numpy.array([120,255,255])
        lower_orange = numpy.array([20,50,50])
        upper_orange = numpy.array([23,255,255])
        lower_yellow = numpy.array([30,50,50])
        upper_yellow = numpy.array([30,255,255])
        lower_green = numpy.array([60,50,50])
        upper_green = numpy.array([60,255,255])
        lower_white = numpy.array([0,0,50])
        upper_white = numpy.array([0,0,250])
        lower_red = numpy.array([0,200,50])
        upper_red = numpy.array([0,255,255])
        lower_aqua = numpy.array([90,50,50])
        upper_aqua = numpy.array([90,255,255])
        # end of colour filter

# -------------------------------------------------------------------------------

        #extract contours result for each meteors
        left_red_result = find_object(left_hsv, lower_red, upper_red)
        right_red_result = find_object(right_hsv, lower_red, upper_red)
        left_green_result = find_object(left_hsv, lower_green, upper_green)
        right_green_result = find_object(right_hsv, lower_green, upper_green)
        left_blue_result = find_object(left_hsv, lower_blue, upper_blue)
        right_blue_result = find_object(right_hsv, lower_blue, upper_blue)
        left_yellow_result = find_object(left_hsv, lower_yellow, upper_yellow)
        right_yellow_result = find_object(right_hsv, lower_yellow, upper_yellow)
        left_orange_result = find_object(left_hsv, lower_orange, upper_orange)
        right_orange_result = find_object(right_hsv, lower_orange, upper_orange)
        left_aqua_result = find_object(left_hsv, lower_aqua, upper_aqua)
        right_aqua_result = find_object(right_hsv, lower_aqua, upper_aqua)
        left_white_result = find_object(left_hsv, lower_white, upper_white)
        right_white_result = find_object(right_hsv, lower_white, upper_white)
        # end of extracting result

# -------------------------------------------------------------------------------

        # calculate the object centre pixel
        red_lx, red_ly = get_mid(left_red_result, left_img)
        red_rx, red_ry = get_mid(right_red_result, right_img)
        green_lx, green_ly = get_mid(left_green_result, left_img)
        green_rx, green_ry = get_mid(right_green_result, right_img)
        blue_lx, blue_ly = get_mid(left_blue_result, left_img)
        blue_rx, blue_ry = get_mid(right_blue_result, right_img)
        yellow_lx, yellow_ly = get_mid(left_yellow_result, left_img)
        yellow_rx, yellow_ry = get_mid(right_yellow_result, right_img)
        orange_lx, orange_ly = get_mid(left_orange_result, left_img)
        orange_rx, orange_ry = get_mid(right_orange_result, right_img)
        aqua_lx, aqua_ly = get_mid(left_aqua_result, left_img)
        aqua_rx, aqua_ry = get_mid(right_aqua_result, right_img)
        white_lx, white_ly = get_mid(left_white_result, left_img)
        white_rx, white_ry = get_mid(right_white_result, right_img)
        # end of object centre pixel

# -------------------------------------------------------------------------------

        # calculate the distance for each object
        red_distance = get_distance(red_lx,red_rx,left_img,right_img)
        green_distance = get_distance(green_lx,green_rx,left_img,right_img)
        blue_distance = get_distance(blue_lx,blue_rx,left_img,right_img)
        yellow_distance = get_distance(yellow_lx,yellow_rx,left_img,right_img)
        orange_distance = get_distance(orange_lx,orange_rx,left_img,right_img)
        aqua_distance = get_distance(aqua_lx,aqua_rx,left_img,right_img)
        white_distance = get_distance(white_lx,white_rx,left_img,right_img)
        # end of calculating distence for each object

# -------------------------------------------------------------------------------
        # store all value for calculating the travel direction
        blue_point.append(
            [get_X_left(((blue_lx-get_half_image_size(left_img))*10**(-5)),
                        blue_distance),blue_distance])
        red_point.append(
            [get_X_left(((red_lx-get_half_image_size(left_img))*10**(-5)),
                        red_distance),red_distance])
        green_point.append(
            [get_X_left(((green_lx-get_half_image_size(left_img))*10**(-5)),
                        green_distance),green_distance])
        yellow_point.append(
            [get_X_left(((yellow_lx-get_half_image_size(left_img))*10**(-5)),
                        yellow_distance),yellow_distance])
        orange_point.append(
            [get_X_left(((orange_lx-get_half_image_size(left_img))*10**(-5)),
                        orange_distance),orange_distance])
        aqua_point.append(
            [get_X_left(((aqua_lx-get_half_image_size(left_img))*10**(-5)),
                        aqua_distance),aqua_distance])
        white_point.append(
            [get_X_left(((white_lx-get_half_image_size(left_img))*10**(-5)),
                        white_distance),white_distance])


# -------------------------------------------------------------------------------

        # Display the result (Distance) of each meteor
        display_result(frame,red_distance,green_distance,blue_distance,
                       yellow_distance,orange_distance,aqua_distance,
                       white_distance)
        # end

# -------------------------------------------------------------------------------
    # find the ufo by calculating the slope
    blue_slope = calculate_slope(blue_point)
    red_slope = calculate_slope(red_point)
    green_slope = calculate_slope(green_point)
    yellow_slope = calculate_slope(yellow_point)
    orange_slope = calculate_slope(orange_point)
    aqua_slope = calculate_slope(aqua_point)
    white_slope = calculate_slope(white_point)
    change_of_slope = check_difference(blue_slope)
    #end


