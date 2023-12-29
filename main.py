from PIL import Image, ImageDraw, ImageOps
from tqdm import tqdm
import numpy as np
import  os
import uuid
import datetime


# Function to calculate the median color of an image block
def calculate_median_color(block):
    pixels = np.array(block)
    median_color = np.median(pixels.reshape(-1,4), axis=0)
    return tuple(np.intp(median_color))

# Function to tint an image with a specified color
def tint_image(src, color):
    src = ImageOps.colorize(src.convert('L'), black="black", white=color)
    return src

def processImage():
    fp = int(input("Fotoğraf netliği seçin : 1 2 3 4 5 6 7: "))
    ff = int(input("Fatoş netliği seçin : 1 2 3: "))
     # Load the provided image
    image_path = 'inception.png'
    image = Image.open(image_path)

    # Dimensions of the block and placeholder image
    block_width, block_height = int(2**(8-fp)),int(2**(8-fp))
    placeholder_size = ( int(2**(ff+5)) , int(2**(ff+5)))

    # Create a placeholder 256x256 image
    placeholder = Image.open("./fatos/fatos"+str(int(2**(ff+5)))+".png")

    # Initialize a new image with the same size as the original image
    new_image_size = (image.width * placeholder_size[0] // block_width, image.height * placeholder_size[1] // block_height)
    new_image = Image.new('RGB', new_image_size)

    total_blocks = (image.width // block_width) * (image.height // block_height)
    print("Processing started...")

    # Iterate over the image in 16x16 blocks
    with tqdm(total=total_blocks, desc="Processing Image") as pbar:
        for y in range(0, image.height, block_height):
            for x in range(0, image.width, block_width):
                # Crop the block from the image
                block = image.crop((x, y, x + block_width, y + block_height))

                # Calculate the median color of the block
                color = calculate_median_color(block)

                # Tint the placeholder image with the median color
                tinted_placeholder = tint_image(placeholder, color)

                # Calculate the position where the new block will be placed
                new_x = x // block_width * placeholder_size[0]
                new_y = y // block_height * placeholder_size[1]

                # Paste the tinted placeholder image into the new image
                new_image.paste(tinted_placeholder, (new_x, new_y))
                pbar.update(1)

    return  new_image

def save_to_downloads(image):
    # Get the path to the user's Downloads directory
    downloads_path = os.path.join(os.path.expanduser("~"), 'Downloads')
    filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"  # Using datetime
    file_path = os.path.join(downloads_path, filename)
    # Save the image to the Downloads directory
    print(f"Saving image to {file_path}...")
    image.save(file_path)
    print(f"Image saved to {file_path}")

save_to_downloads(processImage())
