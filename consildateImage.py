import os
import shutil

def consolidate_images(source_dir, dest_dir, img_extensions=[".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]):
    """
    Consolidate all image files from source_dir and its sub-directories into dest_dir.
    
    :param source_dir: Directory containing the images and sub-directories.
    :param dest_dir: Destination directory where all images will be consolidated.
    :param img_extensions: List of image file extensions to search for.
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for subdir, _, files in os.walk(source_dir):
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext.lower() in img_extensions:
                source_filepath = os.path.join(subdir, file)
                dest_filepath = os.path.join(dest_dir, file)
                
                # Handle possible filename conflict by adding a prefix
                counter = 1
                while os.path.exists(dest_filepath):
                    dest_filepath = os.path.join(dest_dir, f"{counter}_{file}")
                    counter += 1
                
                shutil.copy2(source_filepath, dest_filepath)
                print(f"Copied {source_filepath} to {dest_filepath}")

if __name__ == "__main__":
    SOURCE_DIR = "./streetviews"
    DEST_DIR = "./GeoData"
    
    consolidate_images(SOURCE_DIR, DEST_DIR)
