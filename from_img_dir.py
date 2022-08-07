######################################################
## Inference on all images present in 'img-directory' 
######################################################

import os
from unicodedata import name

def modify_class_names(name_string):
    """ Takes class-names as string and modifies the custom.names file"""
    try:
        with open(r"data\classes\custom.names","w+") as f:
            for name in name_string.split(","):
                f.write(name) 
                f.write("\n") 
    except:
        print("custom.names File Not Found !!!\n")
        
    print("Class-Names Modified Successfully !!!\n")
####
#modify_class_names("clean,deep-clean")


def inference_img_dir(weight="",size=416,model="yolov4",tiny=True,count=False,show_output=False,iou=0.45,confidence=0.50):
    """ Inference on all images present in 'img-directory' """ 
    
    img_dir= "./img_directory"
    out_path="./inference_img_directory/"
    weight_path="./pb_weight_file/"+weight

    if len(os.listdir(img_dir))>0:
        for img in os.listdir(img_dir):
            if img.endswith(".jpg") or img.startswith(".jpeg") or img.startswith(".png")==True:
                image = img_dir + "/" + img
                print("Running Inference on: {}".format(img))
                print()

                ## commands
                main_command ="python detect.py"+" --weights "+ weight_path + " --size " + str(size)+" --model "+model+" --images " +image+" --output "+out_path+" --iou "+str(iou)+" --score "+str(confidence)

                if tiny == True: 
                    main_command=main_command+" --tiny"
                if show_output==False: 
                    main_command=main_command+" --dont_show"    
                if count==True:
                    main_command=main_command+" --count"
            
                #print(main_command)
                os.system(main_command)
    else:
        print("No Image Found in 'Img_directory' !!!")


######################################################################
## Parateters

# weight: .weight file name
# size: image size (416 or 512)
# model: model type ('yolov3' or 'yolov4')
# tiny: tiny model or not (True or False)
# iou: IOU threshold
# confidence: Score threshold  
# count: Show object count (True or False)
# show_output: show realtime inference or not (True or False)
#####################################################################

modify_class_names("clean,deep-clean")     ## object class names
inference_img_dir(weight="m2_512",size=512,model="yolov4",tiny=True,iou=0.40,confidence=0.50,count=True,show_output=True)