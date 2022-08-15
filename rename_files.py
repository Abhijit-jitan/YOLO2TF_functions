import os

def rename_files(in_dir,out_dir,new_name,ext):
    
    
    for file_count,file in enumerate(os.listdir(in_dir)):
        in_name=file
        out_name=new_name+"_"+str(file_count)+"."+ext
        os.rename(os.path.join(in_dir,in_name),os.path.join(out_dir,out_name))


    print("Renamed All files Successfully !!!")


####
in_dir=r"E:\projects\Automated YOLO custom-functions\img_directory"
out_dir=r"E:\projects\Automated YOLO custom-functions\img_directory"
new_name="pipe_test"
ext="jpg"
rename_files(in_dir,out_dir,new_name,ext)
