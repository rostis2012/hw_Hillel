from PIL import Image
import os

directory = 'files'
flag = True
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and filename.endswith((".jpg", ".jpeg")):
        if flag:
            os.mkdir(directory + '/cropped')
            flag = False
        img = Image.open(f)
        w, h = img.size
        count = w // h
        indent = int((w % h) / 2)
        index = 0
        while count:
            crop_img = img.crop((indent + h * index, 0, indent + h * index + h, h))
            crop_img.save(
                directory + '/cropped/' + 'crop_' + str(filename).split('.')[0] + '_part_' + str(
                    index) + '.jpg')
            index += 1
            count -= 1
        img.close()
