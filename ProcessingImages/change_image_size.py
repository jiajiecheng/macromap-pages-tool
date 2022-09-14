from PIL import Image
from PIL.ImageFile import ImageFile

import settings

ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None


def change_image_size(file_in, file_out, width, height):
    img = Image.open(file_in)

    out = img.resize((width, height))
    # 最新版本抗锯齿已经被弃用,所以尽量不要使用此参数
    # out = img.resize((width, height), Image.ANTIALIAS)
    # 保存为jpg格式才需要
    out = out.convert('RGB')
    out.save(file_out, 'JPEG', quality=settings.IMAGE_QUALITY)


def save_image():
    for index in range(settings.TOTAL.get('start'), settings.TOTAL.get('end') + 1):
        change_image_size(f'./Image/{settings.IMAGE_FIRST_NAME}{index}.{settings.IMAGE_FILE_SUFFIX}',
                          f'./Change_Image/{settings.CHANGE_IMAGE_FIRST_NAME}_{index}.{settings.IMAGE_FILE_SUFFIX}',
                          settings.IMAGE_SIZE.get('w', 1000),
                          settings.IMAGE_SIZE.get('h', 1000))


if __name__ == '__main__':
    save_image()
