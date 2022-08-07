######################################################
## Inference on all videos present in 'video_directory' 
######################################################

import os

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


def inference_video_dir(weight="",size=416,model="yolov4",tiny=True,count=False,show_output=False,iou=0.45,confidence=0.50):
    """ Inference on all videos present in 'video-directory' """ 

    video_dir= "./video_directory"
    out_path="./inference_video_directory/"
    weight_path="./pb_weight_file/"+weight

    if len(os.listdir(video_dir))>0:
        for vid in os.listdir(video_dir):
            if vid.endswith(".avi") or vid.startswith(".mp4") or vid.startswith(".MOV")==True:
                video = video_dir + "/" + vid
                out_vid_name="inference_"+vid
                print("Running Inference on: {}".format(vid))
                print()

                ## commands
                main_command ="python detect_video.py"+" --weights "+ weight_path + " --size " + str(size)+" --model "+model+" --images " +video+" --output "+out_path+out_vid_name+" --iou "+str(iou)+" --score "+str(confidence)

                if tiny == True: 
                    main_command=main_command+" --tiny"
                if show_output==False: 
                    main_command=main_command+" --dont_show"    
                if count==True:
                    main_command=main_command+" --count"
            
                print(main_command)
                #os.system(main_command)
    else:
        print("No Video Found in 'video_directory' !!!")



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

modify_class_names("clean,deep-clean")    ## object class names
inference_video_dir(weight="new_tiny",size=416,model="yolov4",tiny=True,iou=0.40,confidence=0.50,count=True,show_output=False)
