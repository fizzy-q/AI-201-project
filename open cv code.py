import cv2
from cvzone.HandTrackingModule import HandDetector

class Button:    # initialization
    def __init__(self,pos,width,height,value):
        #set the arguments for the particular instances
        self.pos=pos     # whatever the user inputs
        self.width=width
        self.height=height
        self.value=value

    def draw(self,image):          # draw on the image
        # Calculator body
        # Function Name      (width, height),(position),(color in RGB),(completely filled
        # cv2.rectangle(image,(100, 100), (200, 200), (225, 225, 225), cv2.FILLED)
        cv2.rectangle(image, self.pos, (self.pos[0]+self.width, self.pos[1]+self.height), (225, 225, 225), cv2.FILLED)
        # cv2.rectangle(image,(100, 100), (200, 200), (50, 50, 50), 3)        # border
        cv2.rectangle(image, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (50, 50, 50), 3)
        # text on calculator  (text on button),(position + push position),(font),(scale),(color)
        # cv2.putText(image,"9",(100+20,100+50),cv2.FONT_ITALIC,2,(50, 50, 50),2)
        cv2.putText(image, self.value, (self.pos[0] + 40, self.pos[1] + 60), cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 2)


#Webcam
cap = cv2.VideoCapture(0)       # you can define the size as well. Defaul# t is 640 x 480
cap.set(3, 1280)                # Changing the width of the camera output, 3 means the third propid of the videcapture class
cap.set(4, 720)                 # Changing the Height of the camera output, 4 means the 4th propid of the videocapture class

#HandDetection
detector = HandDetector(detectionCon=0.8, maxHands=2)       # DetectionCon is how much sure is the program that the object is a hand. value is set to 80%.
#Change max hands value to 2 to detect both hands

# list ciontaing the text on the buttons
buttonlistvalue=[['7','8','9','*'],
                 ['4','5','6','-'],
                 ['1','2','3','+'],
                 ['0','/','.','=']]

# variables
myEquation = '10+5'


# creating buttons
buttonlist = []                            # list for all the buttons
for x in range(4):                        # 4 by 4
    for y in range(4):
        xpos = x*100 + 800                     # value of x is the value of button into the size of the button + offset
        ypos = y*100 + 150
        #button1=Button((700,150),100,100,'5')      # (position),width,height,value
        buttonlist.append(Button((xpos,ypos),100,100,buttonlistvalue[y][x]))      # dynamically put values    y into x for correct positioning

# Function to open the camera
def openCamera():
    while True:
        #Get image from the camera
        success, image = cap.read()

        #Flipping the image
        image = cv2.flip(image, 1)          # 1 will flip the image horizontally(x axis) and 0 will flip vertically (y-axis)

        #Detection of Hand
        hands, image =detector.findHands(image, flipType= False)        # Flip Type is set ot false because we have already set a flip once to not get confused in the mirror imaging of the picture.

        # draw all buttons
        cv2.rectangle(image,(800,70),(800+400,70+100),(225, 225, 225), cv2.FILLED)                  # for the calculator body
        # the result body
        cv2.rectangle(image, (800, 70), (800 + 400, 80 + 100), (50,50,50), 3)
        for button in buttonlist:
            button.draw(image)     # image on which we want to draw

        # processing

        # display result(eqation)
        cv2.putText(image, myEquation, ( 850, 130),cv2.FONT_HERSHEY_PLAIN,3, (50, 50, 50), 2)


        # Display Image
        cv2.imshow("Image", image)
        cv2.waitKey(1)          # 1 milisecond delay



print(openCamera())