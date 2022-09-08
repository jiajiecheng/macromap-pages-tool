from settings import TOTAL, CLASS
from collections import deque


class AutoPageGroup:
    def get_all_packages(self):
        packages = deque([])
        for package in range(TOTAL.get('start'), TOTAL.get('end') + 1):
            packages.append(f"P{str(package).zfill(3)}")
        return packages

    def get_pages_list(self, number, packages):
        pages = []
        for i in range(0, number):
            try:
                pages.append(packages.popleft())
            except Exception as e:
                print('总数与分类数不对应')
                break
        return pages

    def production_group(self):
        page_group_type = []
        packages = self.get_all_packages()
        for class_item in CLASS:
            page_group_type.append({
                'name': class_item.get('name'),
                'pages': self.get_pages_list(class_item.get('count'), packages)
            })
        return page_group_type
