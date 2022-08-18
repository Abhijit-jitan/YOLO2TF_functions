######################################################
## Batch-Inference on Images in 'img-directory' 
######################################################

import os,random,datetime
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

## Generating Image Batches
def image_batch_inference(batch_size,total_batch,weight,size=416,model="yolov4",tiny=True,count=False,show_output=False,iou=0.45,confidence=0.50):
    """ takes images dir,batch_size & returns list(images-batch) """
    dir="./img_directory"                        # image in-path
    out_path="./inference_img_directory/"        # image out-path
    weight_path="./pb_weight_file/"+weight       # weight in-path
    image_list=os.listdir(dir)                   
    
    tic=datetime.datetime.now()
    if len(image_list)>0:
        for batch_num,i in enumerate(range(total_batch)):
            random_image_batch=random.sample(image_list,batch_size)     # list(random sample of images)
            # print("Batch-{}: Image-List{}".format(batch_num+1,random_image_batch))
            print("Running Inference on batch:",batch_num+1)
            
            ## inference on each batch of images
            for img in random_image_batch:
                image=dir+"/"+img

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
        print("Image folder is empty")

    toc=datetime.datetime.now()
    print("total Time Taken:",(toc-tic).total_seconds())
######################################################################
## Parateters

# batch_size: total image in each batch
# total_batch: total batch number
# weight: .weight file name
# size: image size (416 or 512)
# model: model type ('yolov3' or 'yolov4')
# tiny: tiny model or not (True or False)
# iou: IOU threshold
# confidence: Score threshold  
# count: Show object count (True or False)
# show_output: show realtime inference or not (True or False)
#####################################################################

#modify_class_names("person")     ## object class names
image_batch_inference(batch_size=10,total_batch=5,weight="person",size=416,model="yolov4",tiny=True,count=False,show_output=False,iou=0.45,confidence=0.50)
