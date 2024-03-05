# This is for controlling the volume
from ctypes import cast,POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume

#for hand detection
import cv2
import mediapipe as mp
from math import hypot
import numpy as np

##Initializing the volume controller
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

volume = cast(interface,POINTER(IAudioEndpointVolume))

volume_range = volume.GetVolumeRange()
min_volume = volume_range[0]
max_volume = volume_range[1]

def changeVolume(new_volume):
    
    volume.SetMasterVolumeLevelScalar(new_volume/100,None)    

##Initializing the Handdetection model
## mp stands for mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=2,
)

Draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()

    #Flip image
    frame = cv2.flip(frame,1)

    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    Process = hands.process(frameRGB)
    
    landmarkList = []
    # if hands are present int the frame
    if Process.multi_hand_landmarks:
        #detect handmkrks
        for handlm in Process.multi_hand_landmarks:
            for _id, landmarks in enumerate(handlm.landmark):
                #store height and width of image
                heights , width ,color_changgels = frame.shape

                ##calculate and append x,y coordinates
                ##of handmarks from frame to landmarkList
                x,y = int(landmarks.x * width), int(landmarks.y * heights)
                landmarkList.append([_id,x,y])
            
            Draw.draw_landmarks(frame,handlm,mpHands.HAND_CONNECTIONS)
    if landmarkList != []:
        ## it will store the tip of thumb
        x_thumb,y_thumb = landmarkList[4][1],landmarkList[4][2]

        ## it will store the top of index finger (Tarjani)
        x_Tarjani,y_Tarjani = landmarkList[8][1],landmarkList[8][2]

        ## drawing the circle on thumb and index fingertips
        cv2.circle(frame,(x_thumb,y_thumb),7,(0,255,0),cv2.FILLED)
        cv2.circle(frame,(x_Tarjani,y_Tarjani),7,(0,255,0),cv2.FILLED)

        ## this will draw the line from thumb to tarjani
        cv2.line(frame,(x_thumb,y_thumb),(x_Tarjani,y_Tarjani),(0,255,0),3)

        ## calculating the langht of between angutha(thumb) to tarjani
        leangth = hypot(x_Tarjani-x_thumb,y_Tarjani-y_thumb)

        volume_level = np.interp(leangth,[15,165],[0,100])
        changeVolume(int(volume_level))


    cv2.imshow('Geastures',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
