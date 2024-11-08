from PIL import Image

    # Open an image file
with Image.open('./images/UP.png') as img:
    # Resize image
    img = img.resize((100, 100))
    # Save it back to disk
    img.save('./images/UP_resized.png')
