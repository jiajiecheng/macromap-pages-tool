import settings
import os

image_path = os.path.join(os.getcwd(), 'Image')
change_image_path = os.path.join(os.getcwd(), 'Change_Image')
image_first_name = settings.IMAGE_FIRST_NAME
image_file_suffix = settings.IMAGE_FILE_SUFFIX
change_image_first_name = settings.CHANGE_IMAGE_FIRST_NAME


def change_image_file_name():
    for index in range(settings.TOTAL.get('start'), settings.TOTAL.get('end') + 1):
        try:
            os.rename(os.path.join(image_path, f'{image_first_name}{index}.{image_file_suffix}'),
                      os.path.join(change_image_path, f'{change_image_first_name}_{index}.{image_file_suffix}'))
        except Exception as e:
            print(e)
            print('修改文件名称失败')
        else:
            print('修改文件名称成功')


if __name__ == '__main__':
    change_image_file_name()
