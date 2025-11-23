from PIL import Image

# Open the image
image = Image.open("assets/project2.jpg")  # Replace with your filename

# Get original dimensions
original_width, original_height = image.size

# Calculate new height while keeping aspect ratio
new_width = 250
new_height = int((new_width / original_width) * original_height)

# Resize the image
resized_image = image.resize((new_width, new_height))

# Save the resized image
resized_image.save("assets/resized_image2.png")
