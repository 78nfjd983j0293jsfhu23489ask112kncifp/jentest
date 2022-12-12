import sys
sys.path.append(".")

import os
from source.AI.UltraSonic import *
from source.AI.XRAY import *
from source.DatabaseUtility import *

unet=initUNETmodel()
vggnet=initVGGmodel()

def pass2AI(dID,selection):
    img_name=dID+".png"

    if(selection=="xray"):
        prediction=forwardXRAY(vggnet,img_name)
        return prediction
    if(selection=="ultrasonic"):
        forwardULTRAS(unet,img_name)
    return "None"

def make_gallery():
    images=[]
    details=[]

    for img in os.listdir(os.path.join(os.path.abspath(os.getcwd()),"static","USER_DATA","USER_INPUT")):
        # combine input and output 
        if(img in os.listdir(os.path.join(os.path.abspath(os.getcwd()),"static","USER_DATA","AI_OUTPUT"))):
            combined=np.zeros((256,512,3))
            user_input=cv2.imread(os.path.join(os.path.abspath(os.getcwd()),"static","USER_DATA","USER_INPUT",img))
            # resize 256,256 in order to match output of network
            #user_input=cv2.cvtColor(user_input,cv2.COLOR_RGB2GRAY)
            user_input=cv2.resize(user_input,(256,256))
            
            combined[:,:256,:]=user_input[:,:]
            ai_output=cv2.imread(os.path.join(os.path.abspath(os.getcwd()),"static","USER_DATA","AI_OUTPUT",img))
            #ai_output=cv2.cvtColor(ai_output,cv2.COLOR_RGB2GRAY)
            ai_output=cv2.resize(ai_output,(256,256))
            combined[:,256:512,:]=ai_output[:,:]
            cv2.imwrite(os.path.join(os.path.abspath(os.getcwd()),"static","USER_DATA","Gallery",img),combined)

            dID=img.split(".")[0]
            images.append(img)
            details.append(getDetails(dID))
    
    results=[]

    for img,det in zip(images,details):
        results.append([img,det])

    return results 
    