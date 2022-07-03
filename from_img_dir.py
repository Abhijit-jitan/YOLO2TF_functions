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


def inference_img_dir(weight="",size=416,model="yolov4",tiny=True,count=False,show_output=False,iou=0.45,confidence=0.50):
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

####
modify_class_names("clean,deep-clean")
inference_img_dir(weight="new_tiny",size=416,model="yolov4",tiny=True,iou=0.40,confidence=0.50,count=True,show_output=False)