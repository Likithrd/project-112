import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir="C:/Users/sai_l/Downloads"
to_dir="C:/Users/sai_l/OneDrive/Desktop"

dir_tree={
"image_files":['.gif', '.png', '.jpg', '.jpeg','.jfif'],
"video_files":['.mp4','.mpg','.mp2','.mpeg','.m4v','.avi','.mov'],
"document _files":['.txt','.ppt','.pdf','.csv','.xlsx'],
"setup_files":['.exe','.bin','.cmd','.msi','.dmg']

}
class FileMovmentHandler(FileSystemEventHandler):
   def on_created(self,event):
      name,extention=os.path.splitext(event.src_path)
      time.sleep(1)

      for key,value in dir_tree.items():
         time.sleep(1)

         if extention in value:
            file_name=os.path.basename(dir_tree)
            print("Downloaded"+file_name)

            path1 = from_dir + '/' + file_name                       # Example path1 : Downloads/ImageName1.jpg        
            path2 = to_dir + '/' + "Document_Files"                     # Example path2 : D:/My Files/Image_Files      
            path3 = to_dir + '/' + "Document_Files" + '/' + file_name
            if os.path.exists(path2):
                    print("Directory exists")
                    print("Moving"+file_name+"......")
                    shutil.move(path1, path3)
                    time.sleep(1)
            else:
                    print("Making directory")
                    os.makedirs(path2)
                    print("Moving"+file_name+"......")
                    shutil.move(path1, path3)
                    time.sleep(1)
      
#initialise event handler
event_handler=FileMovmentHandler()
# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")