import os
def from_dir(weight="",size=416,model="yolov4",tiny=True,count=False):
    img_dir= "./image_directory"
    out_path="./dir_inference/"
    weight_path="./checkpoints/"+weight

    for img in os.listdir(img_dir):
        image = img_dir + "/" + img

        if tiny == True and count==True:
            command ="python detect.py"+" --weights "+ weight_path + " --size " + str(size)+" --model "+model+" --images " +image+" --output "+out_path+" --dont_show "+"--count"+" --tiny"
            os.system(command)

        elif tiny == True and count==False:
            command ="python detect.py"+" --weights "+ weight_path + " --size " + str(size)+" --model "+model+" --images " +image+" --output "+out_path+" --dont_show"+" --tiny"
            os.system(command)

        elif tiny == False and count==True:
            command = "python detect.py" + " --weights " + weight_path + " --size " + str(size) + " --model " + model + " --images " + image + " --output " + out_path + " --dont_show " + "--count"
            print("Tiny:  ", command)
        else:
            command ="python detect.py"+" --weights "+ "./checkpoints/"+ weight + " --size " + str(size)+" --model "+model+" --images " +image+" --output "+out_path+" --dont_show"
            print(":  ", command)
            os.system(command)
        
    return

from_dir(weight="clean_tiny_apr8",size=416,model="yolov4",tiny=True,count=False)

#tiny=True,count=False
# python detect.py --weights ./checkpoints/new.weights --size 416 --model yolov4 --images ./image_directory/99.jpg --output ./dir_inference/ --dont_show --count --tiny
# python detect.py --weights ./checkpoints/new.weights --size 416 --model yolov4 --images ./image_directory/99.jpg --output ./dir_inference/ --dont_show --tiny

#python detect_video.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --video ./data/video/video.mp4 
# --output ./detections/results.avi