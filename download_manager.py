import os
import shutil
import time

downloads_folder = "/home/sithembiso/Downloads"

# mapping of file extensions to corresponding folder names
file_type_folders = {
    "pdf": "PDF",
    "jpg": "Images",
    "png": "Images",
    "mp4": "Videos",
    "mkv": "Videos",
    "zip": "Zipped Files",
    "torrent": "Torrents"
}


def move_to_folder(file_path, folder_name):
    destination_folder = os.path.join(downloads_folder, folder_name)
    os.makedirs(destination_folder, exist_ok=True)
    destination_path = os.path.join(destination_folder, os.path.basename(file_path))
    shutil.move(file_path, destination_path)
    print(f"Moved '{os.path.basename(file_path)}' to '{destination_folder}'")


def sort_downloads():
    for folder_name in file_type_folders.values():
        folder_path = os.path.join(downloads_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
    while True:
        for root, _, files in os.walk(downloads_folder):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = file.split(".")[-1].lower()
                if file_extension in file_type_folders:
                    move_to_folder(file_path, file_type_folders[file_extension])
        time.sleep(3600) # check every hour

if __name__ == "__main__":
    print("Starting download sorting automation...")
    sort_downloads()