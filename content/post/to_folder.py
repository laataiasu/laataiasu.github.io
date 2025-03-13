import os
import shutil

# Get the current directory
current_dir = os.getcwd()

# Loop through each file in the current directory
for filename in os.listdir(current_dir):
    # Check if the file has a .md extension
    if filename.endswith('.md'):
        # Get the base name without the .md extension
        base_name = os.path.splitext(filename)[0]
        
        # Create a new directory with the base name
        new_dir = os.path.join(current_dir, base_name)
        os.makedirs(new_dir, exist_ok=True)
        
        # Move the .md file to the new directory
        src_file = os.path.join(current_dir, filename)
        dst_file = os.path.join(new_dir, 'index.md')
        
        # Move and rename the file
        shutil.move(src_file, dst_file)
        
        print(f'Moved and renamed {src_file} to {dst_file}')
