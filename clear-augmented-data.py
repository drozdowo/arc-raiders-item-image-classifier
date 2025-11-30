import os
import shutil
base_dir='./arc-raiders-items'
    
if not os.path.exists(base_dir):
    print(f"Directory {base_dir} does not exist")
    exit()

# Get all subdirectories
subdirs = [d for d in os.listdir(base_dir) 
            if os.path.isdir(os.path.join(base_dir, d))]

total_deleted = 0

for subdir in subdirs:
    subdir_path = os.path.join(base_dir, subdir)
    
    # Get all files in the subdirectory
    files = [f for f in os.listdir(subdir_path) 
            if os.path.isfile(os.path.join(subdir_path, f))]
    
    deleted_count = 0
    
    for file in files:
        # Skip 1.png, delete everything else
        if file != '1.png':
            file_path = os.path.join(subdir_path, file)
            try:
                os.remove(file_path)
                deleted_count += 1
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
    
    if deleted_count > 0:
        print(f"{subdir}: deleted {deleted_count} file(s)")
    
    total_deleted += deleted_count

print(f"\nTotal files deleted: {total_deleted}")
print(f"Processed {len(subdirs)} subdirectories")

