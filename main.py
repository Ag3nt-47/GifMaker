from PIL import Image

# Take list of paths for images
image_path_list = ['img1.jpg', 'img2.jpg', 'img3.jpg']

# Create a list of image objects
image_list = [Image.open(file) for file in image_path_list]

# Save the first image as a GIF file
image_list[0].save(
            'animation.gif',
            save_all=True,
            append_images=image_list[1:], # append rest of the images
            duration=1000, # in milliseconds
            loop=0)
