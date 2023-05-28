# Text-to-Image Converter

This is a Python script that converts text input into an image using the Pillow library. It allows you to generate images from text and customize the font, size, and color.

## Requirements

- Python 3.x
- Pillow library (>=8.3.2)

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running the following command in your Python environment:


## Usage

1. Open the terminal or command prompt and navigate to the project directory.
2. Run the script by executing the following command:

python index.py

3. Enter the desired text when prompted.
4. The script will generate an image with the text and save it as "output_image.png" in the same directory.
5. The path to the saved image will be displayed in the console.

## Customization

- Font: You can customize the font by providing the path to your desired TrueType font file. Update the `font_path` variable in the code.
- Font size: Adjust the `font_size` variable in the code to change the font size.
- Font color: Modify the `font_color` variable to change the color of the text. The color should be specified as an RGB tuple.

## Example

Here's an example usage:

$ python code.py
Enter the text: Hello, World!
Image saved as output_image.png


This will generate an image with the text "Hello, World!" and save it as "output_image.png" in the project directory.

## License

This project is licensed under the [MIT License](LICENSE).
