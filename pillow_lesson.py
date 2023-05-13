from PIL import Image, ImageDraw, ImageFont

image = Image.open('jelly.png')

# cropped_image = image.crop((0, 80, 200, 400))

# cropped_image.save('pil_result/jelly_cropper_image.png')

# image.show()


# rotated_image.save('pil_result/jelly_cropper_image.png')
#
# text_image = ImageDraw.Draw(image)
#
# text = 'This is codify property'
# font = ImageFont.truetype('arial.ttf', size=32)
# text_image.text((20, 20), text, font=font)
# image.save('pil_result/jelly_text.png')


# image.convert('RGB').save('pil_result/jelly_cropper_image.jpg', 'JPEG')
# image = image.resize((200, 200))
#
# image.save('pil_result/jelly_hard_resize.png')

# w, h = image.size
# new_width = 300
#
# new_height = int(new_width * h / w)
#
# image = image.resize((new_width, new_height))
#
# image.save(('pil_result/jelly_resize_by.png'))

# w, h = image.size
#
# new_height = 240
#
# new_width = int(w / h * new_height)
# image = image.resize((new_width, new_height))
#
# image.save(('pil_result/jelly_resize_by_height.png'))

