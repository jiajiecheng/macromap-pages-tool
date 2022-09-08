from settings import TOTAL


# 自动生成菜单导包路径
class AutoImportPath:

    def get_template_str(self, packageName='', rootPath=''):
        template = f"import P{packageName} from './pages/p{rootPath}';"
        return template

    def production_import_path(self):
        paths = []
        for i in range(TOTAL.get('start'), TOTAL.get('end') + 1):
            number = str(i).zfill(3)
            path = self.get_template_str(number, number)
            paths.append(path)
        return paths
