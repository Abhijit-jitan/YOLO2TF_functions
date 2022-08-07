####################################################
## Convert only one weight-file at once
####################################################

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


def convert_weight(weight,size=416,model="yolov4",tiny=True,theshold=0.2,framework="tf"):
    """ Convert only one weight file at once """

    weight_in=os.path.join("./yolo_weight_file/",weight)
    weight_out="./pb_weight_file/"+weight.split(".weights")[0]
    print("Converting : {}\n".format(weight))

    ## commands
    main_command ="python save_model.py"+" --weights "+ weight_in + " --input_size " + str(size)+" --model "+model+" --output "+weight_out+" --score_thres "+str(theshold)+" --framework "+framework

    if tiny == True: 
        main_command=main_command+" --tiny"
        #print(main_command)
        os.system(main_command)
    else:
        print("No Weight File Found !!!")



######################################################################
## Parateters

# weight: .weight file name
# size: image size (416 or 512)
# model: model type ('yolov3' or 'yolov4')
# tiny: tiny model or not (True or False)
# iou: IOU threshold
# framework: converted to framework ('tf' or 'trt' or 'tflite')
# theshold: score threshold
#####################################################################
modify_class_names("glove,front,full,back,box")    ## object class names
convert_weight("wi_5.weights",size=416,model="yolov4",tiny=True,theshold=0.2,framework="tf")