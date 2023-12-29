from PIL import Image, ImageDraw, ImageOps
from tqdm import tqdm
import numpy as np
import  os
import datetime


def calculate_median_color(block):
    pixels = np.array(block)
    median_color = np.median(pixels.reshape(-1,4), axis=0)
    return tuple(np.intp(median_color))

def tint_image(src, color):
    src = ImageOps.colorize(src.convert('L'), black="black", white=color)
    return src

def processImage():
    fp = int(input("Fotoğraf netliği seçin : 1 2 3 4 5 6 7: "))
    ff = int(input("Fatoş netliği seçin : 1 2 3: "))
    ##TODO: add your own path !!!
    image_path = 'inception.png'
    image = Image.open(image_path)

    block_width, block_height = int(2**(8-fp)),int(2**(8-fp))
    placeholder_size = ( int(2**(ff+5)) , int(2**(ff+5)))

    placeholder = Image.open("./fatos/fatos"+str(int(2**(ff+5)))+".png")

    new_image_size = (image.width * placeholder_size[0] // block_width, image.height * placeholder_size[1] // block_height)
    new_image = Image.new('RGB', new_image_size)

    total_blocks = (image.width // block_width) * (image.height // block_height)
    print("Processing started...")

    with tqdm(total=total_blocks, desc="Processing Image") as pbar:
        for y in range(0, image.height, block_height):
            for x in range(0, image.width, block_width):
                block = image.crop((x, y, x + block_width, y + block_height))

                color = calculate_median_color(block)

                tinted_placeholder = tint_image(placeholder, color)

                new_x = x // block_width * placeholder_size[0]
                new_y = y // block_height * placeholder_size[1]

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
