import os


def create_directories():
    """ create directory if not exists """
    dir_list=["img_directory","video_directory","inference_img_directory","inference_video_directory","yolo_weight_file","pb_weight_file","detections"]

    for dir in dir_list:
        try:
            os.mkdir(dir)
        except:
            print("'{}' Directory Already Present!!!".format(dir))

create_directories()
