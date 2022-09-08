from pagesList_import import AutoImportPath
from pagesList_class import AutoPageGroup
from judge import judge


def get_packages_path_str():
    path_str = ""
    autoImport = AutoImportPath()
    paths = autoImport.production_import_path()
    for path in paths:
        # path_str.join(path.join('\n'))
        path_str += path + '\n'
    return path_str


def get_group_str():
    group_str = ""
    auto = AutoPageGroup()
    groups = auto.production_group()
    for group in groups:
        group_str += '\t' + str(group) + ',\n'
    return group_str


def get_page_list_template(packagesPath, groupList):
    return "import { DishPageGroupType } from 'macromap-library-app';\n" \
           "\n" \
           f"{packagesPath}\n" \
           f"const data: DishPageGroupType[] = [\n" \
           f"{groupList}" \
           f"]\n" \
           f"\n" \
           f"export default data;\n"


def get_page_list_content():
    return get_page_list_template(get_packages_path_str(), get_group_str())


def get_page_list_file():
    if judge.judge_total() and judge.jude_setting_is_null():
        file = open('../PageListFile/PagesList.ts', 'w', encoding='UTF-8')
        file.write(get_page_list_content())
        file.close()
