import os
import shutil

def move_all_mp4_recursively(source_folder, destination_folder):
    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)
    # Walk through all folders and subfolders
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith('.mp4'):
                source_path = os.path.join(root, file)
                dest_path = os.path.join(destination_folder, file)
                # Handle duplicate file names
                base, ext = os.path.splitext(file)
                count = 1
                while os.path.exists(dest_path):
                    dest_path = os.path.join(destination_folder, f"{base}_{count}{ext}")
                    count += 1
                # Move (cut) the file
                shutil.move(source_path, dest_path)
                print(f"Moved: {file} → {destination_folder}")

source_folder = r"E:\CSE Repository\Udemy - Complete MLOps Bootcamp With 10+ End To End ML Projects 2024-10" #you can replace this source folder with your file location
destination_folder = r"E:\CSE Repository\All_Videos"
move_all_mp4_recursively(source_folder, destination_folder)
