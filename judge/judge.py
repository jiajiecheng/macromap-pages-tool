from PageList.settings import TOTAL, CLASS


def judge_total():
    group_total = 0
    for i in CLASS:
        group_total += i['count']
    if group_total == (TOTAL.get('end') - TOTAL.get('start')) + 1:
        return True
    else:
        raise Exception('总数与分类条目数量没有对应')


def jude_setting_is_null():
    if TOTAL and CLASS:
        return True
    else:
        raise Exception('配置项目为空,或者不存在')