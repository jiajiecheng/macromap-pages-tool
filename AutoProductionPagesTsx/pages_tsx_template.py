from settings import TOTAL
from judge.judge import judge_total


def production_pages_tsx_template(img_package_name, img_name):
    return "import React, { useEffect } from 'react';\n" \
           "import { DishPageType, SelectorView, VideoView } from 'macromap-library-app';\n" \
           f"import {img_package_name} from './assets/{img_name}.jpg';\n" \
           f"\n" \
           "function getDishes() {\n" \
           "\treturn [\n" \
           "\t\t{\n" \
           "\t\t\tid: 1,\n" \
           "\t\t\tname: '',\n" \
           "\t\t},\n" \
           "\t];\n" \
           "}\n" \
           "\n" \
           "function PageView({ isActive }: any) {\n" \
           "\treturn (\n" \
           "\t\t<div style={{ width: '100%', height: '100%' }}>\n" \
           "\t\t\t<img style={{ width: '100%', height: '100%' }} src={" + img_package_name + "} />\n" \
                                                                                             "\t\t</div>\n" \
                                                                                             "\t);\n" \
                                                                                             "}\n" \
                                                                                             "\n" \
                                                                                             "const page: DishPageType = { dishes: getDishes, view: PageView };\n" \
                                                                                             "export default page;\n"


def production_img():
    img_info = []
    for i in range(TOTAL.get('start'), TOTAL.get('end') + 1):
        img_info.append(
            {
                'img_package_name': f"Img{str(i).zfill(2)}",
                'img_name': f"img_{i}"
            }
        )
    return img_info


def production_pages_tsx_content():
    file_content = []
    img_info = production_img()
    for item in img_info:
        file_content.append(production_pages_tsx_template(**item))
    return file_content


def production_pages_tsx_file_name():
    file_name = []
    for i in range(TOTAL.get('start'), TOTAL.get('end') + 1):
        file_name.append(f'p{str(i).zfill(3)}.tsx')
    return file_name


def production_pages_tsx_file():
    if judge_total():
        for img in zip(production_pages_tsx_file_name(), production_pages_tsx_content()):
            file = open(f'../PagesFile/{img[0]}', 'w')
            file.write(img[1])
            file.close()
