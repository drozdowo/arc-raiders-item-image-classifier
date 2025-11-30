import os
import random
from PIL import Image

# Configuration
ITEMS_DIR = "./arc-raiders-items"
MARGIN = 32  # pixels added to each side
GAP = 12  # gap between tiles in pixels
NUM_AUGMENTED = 9  # number of augmented images per item

def get_all_item_paths():
    """
    Get all item folders and their 1.png paths.
    
    Returns:
        dict: Dictionary mapping item folder name to 1.png path
    """
    item_paths = {}
    
    for item_folder in os.listdir(ITEMS_DIR):
        item_path = os.path.join(ITEMS_DIR, item_folder)
        
        if not os.path.isdir(item_path):
            continue
            
        png_path = os.path.join(item_path, "1.png")
        
        if os.path.exists(png_path):
            item_paths[item_folder] = png_path
    
    return item_paths

def create_tiled_image(center_img_path, background_img_paths):
    """
    Create a 3x3 grid with center image surrounded by 8 random background images.
    
    Args:
        center_img_path: Path to the center image
        background_img_paths: List of 8 paths to background images
        
    Returns:
        PIL.Image: The composed tiled image
    """
    # Load the center image
    center_img = Image.open(center_img_path).convert("RGBA")
    center_width, center_height = center_img.size
    
    # Load all 8 background images
    bg_images = [Image.open(path).convert("RGBA") for path in background_img_paths]
    
    # Calculate canvas size
    # Center image + margins on each side + gaps between tiles
    canvas_width = center_width + 2 * MARGIN
    canvas_height = center_height + 2 * MARGIN
    
    # Create transparent canvas
    canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))
    
    # Place center image in the middle
    center_x = MARGIN
    center_y = MARGIN
    canvas.paste(center_img, (center_x, center_y), center_img)
    
    # Define positions for the 8 surrounding tiles in a 3x3 grid
    # Positions are: top-left, top-center, top-right, 
    #                middle-left, middle-right,
    #                bottom-left, bottom-center, bottom-right
    
    positions = [
        # Top row
        ("top-left", lambda img: (center_x - img.width - GAP, center_y - img.height - GAP)),
        ("top-center", lambda img: (center_x + center_width // 2 - img.width // 2, center_y - img.height - GAP)),
        ("top-right", lambda img: (center_x + center_width + GAP, center_y - img.height - GAP)),
        
        # Middle row (left and right)
        ("middle-left", lambda img: (center_x - img.width - GAP, center_y + center_height // 2 - img.height // 2)),
        ("middle-right", lambda img: (center_x + center_width + GAP, center_y + center_height // 2 - img.height // 2)),
        
        # Bottom row
        ("bottom-left", lambda img: (center_x - img.width - GAP, center_y + center_height + GAP)),
        ("bottom-center", lambda img: (center_x + center_width // 2 - img.width // 2, center_y + center_height + GAP)),
        ("bottom-right", lambda img: (center_x + center_width + GAP, center_y + center_height + GAP)),
    ]
    
    # Place each background image at its position
    for i, (position_name, position_func) in enumerate(positions):
        if i < len(bg_images):
            bg_img = bg_images[i]
            x, y = position_func(bg_img)
            canvas.paste(bg_img, (x, y), bg_img)
    
    return canvas

def augment_item_with_tiles(item_name, item_path, all_items):
    """
    Create augmented versions of an item by tiling random items around it.
    
    Args:
        item_name: Name of the item folder
        item_path: Path to the item's 1.png
        all_items: Dictionary of all available items
    """
    output_dir = os.path.join(ITEMS_DIR, item_name)
    
    # Get list of other items (exclude the current item)
    other_items = [name for name in all_items.keys() if name != item_name]
    
    if len(other_items) < 8:
        print(f"⚠ Not enough other items to create tiles for {item_name}, skipping...")
        return
    
    # Generate augmented images
    for i in range(NUM_AUGMENTED):
        # Randomly select 8 different background items
        background_items = random.sample(other_items, 8)
        background_paths = [all_items[name] for name in background_items]
        
        # Create the tiled image
        tiled_image = create_tiled_image(item_path, background_paths)
        
        # Save the augmented image
        output_path = os.path.join(output_dir, f"{item_name}_tile_aug_{i+1}.png")
        tiled_image.save(output_path, "PNG")
    
    print(f"✓ Created {NUM_AUGMENTED} tiled augmented images for {item_name}")

def process_all_items():
    """
    Process all item folders and create tiled augmented images.
    """
    # Get all available items
    all_items = get_all_item_paths()
    
    total_items = len(all_items)
    print(f"Found {total_items} items to process\n")
    
    if total_items < 9:
        print("⚠ Need at least 9 items total to create tiled augmentations!")
        return
    
    for idx, (item_name, item_path) in enumerate(all_items.items(), 1):
        print(f"[{idx}/{total_items}] Processing {item_name}...")
        augment_item_with_tiles(item_name, item_path, all_items)
    
    print(f"\n✓ All done! Processed {total_items} items.")



if __name__ == "__main__":
    process_all_items()
