# TERİMLEŞTİRCİ

This project processes an image by dividing it into smaller blocks, calculates the median color of each block, tints a placeholder image with that median color, and assembles these tinted images into a new, larger image.

## Installation

To run this project, ensure you have Python installed on your machine. You will also need to install the following Python packages: Pillow (for image processing), NumPy (for numerical operations), and tqdm (for displaying progress bars).

Install these packages using pip:
```bash
pip install Pillow numpy tqdm
 ```
## Usage

1. **Prepare Your Images**: To process different images or use different placeholders, modify the `image_path` and `placeholder` variables in the `processImage` function. Adjust the paths according to the location and names of your images.

2. **Run the Script**: Execute the script with Python:

    ```
    python main.py
    ```

    Replace `main.py` with the actual name of your Python script.

3. **Input Parameters**:
    - When prompted, enter the desired *photo clarity* (`Fotoğraf netliği`) by choosing a number between 1 and 7.
    - Next, choose the *placeholder clarity* (`Fatoş netliği`) by selecting a number between 1 and 3.

4. **Check the Downloads Folder**: After processing, the script will save the new image in your system's Downloads folder with a timestamped filename.

## Contributing

Contributions to this project are welcome. Feel free to fork the repo, make changes, and submit pull requests.
