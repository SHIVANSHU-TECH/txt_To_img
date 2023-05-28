from PIL import Image, ImageDraw, ImageFont

# Define the text to be displayed
text = input("Enter the text:")

# Define the font properties
font_size = 30
font_color = (0, 0, 0)  # Black color
font_path = "C:/Windows/Fonts/Arial.ttf"  # Font file path

# Create a blank image with a white background
background_color =  (0, 255, 255)  # White color
image_width = 1000
image_height = 200
image = Image.new("RGB", (image_width, image_height), background_color)

# Create a drawing object
draw = ImageDraw.Draw(image)

# Load the font
font = ImageFont.truetype(font_path, font_size)

# Calculate the bounding box of the text
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Calculate the position to center the text
x = (image_width - text_width) // 2
y = (image_height - text_height) // 2

# Draw the text on the image
draw.text((x, y), text, font=font, fill=font_color)

# Save the image to a file
output_file_path = "output_image.png"
image.save(output_file_path)
print(f"Image saved as {output_file_path}")