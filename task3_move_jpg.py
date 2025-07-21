import os
import shutil

# Step 1: Create folders if they don't exist
source_folder = "source_images"
destination_folder = "jpg_files_only"

os.makedirs(source_folder, exist_ok=True)
os.makedirs(destination_folder, exist_ok=True)

# Step 2: Create some dummy files (for testing)
with open(os.path.join(source_folder, "image1.jpg"), "w") as f:
    f.write("dummy jpg content")
with open(os.path.join(source_folder, "image2.jpg"), "w") as f:
    f.write("dummy jpg content")
with open(os.path.join(source_folder, "document.txt"), "w") as f:
    f.write("some text content")
with open(os.path.join(source_folder, "image3.png"), "w") as f:
    f.write("dummy png content")

# Step 3: Move only .jpg files
for file_name in os.listdir(source_folder):
    if file_name.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file_name)
        dest_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, dest_path)

print(" All .jpg files moved successfully!")
