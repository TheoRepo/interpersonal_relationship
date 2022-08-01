#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   count.py
#@Time    :   2022/08/01 15:15:16
#@Author  :   Theo Yu

from typing import List, Tuple, Dict
import itertools

def read_data(address):
    with open(address,'r') as f:
        next(f)  # skip the first line.
        data = f.readlines()
        dataset = {}
        for line in data:
            the_date, group, names = line.strip().split('\t')
            name_list = []
            for item in names.strip().split('，'):
                name_list.append(item)
            line = {the_date + '/group' + str(group) :set(name_list)}
            dataset.update(line)
    return dataset


def count(dataset: Dict[str,set]) -> Dict[str, int]:
    """实现的功能: 次数统计
    输入是: 一个时间点, 一起吃饭的人
        数据结构: dict {'date': (people1, people2)}

    输出是: 两个人之间吃饭次数的统计
        数据结构: {名字-名字：次数}

    Parameters
    ------

    Returns
    ------

    """
    total_count = {} 
    for everyKey in dataset.keys():
        nameset = dataset[everyKey]
        pair = list(itertools.combinations(list(nameset),2))
        # 将key排序，避免key重复
        # ex. ('一行', '轩辕'), ('轩辕', '一行')
        sorted_pair = []
        for item in pair:
            sorted_pair.append(tuple(sorted(item)))
        # 统计组内，组合出现的次数
        group_count = {}
        for element in sorted_pair:
            group_count.update({element:1})
        # 统计组外，所有组合出现的次数
        for key,value in group_count.items():
            if key in total_count:
                total_count[key] += value
            else:
                total_count[key] = value
    return total_count


def plot(cal_result: Dict[str, int]):
    """实现的功能: 绘图
    输入是: 两个人之间吃饭次数的统计
        数据结构: {名字-名字：次数}

    输出是: 数据可视化
        图像

    Parameters
    ------

    Returns
    ------

    """
    pass


if __name__=='__main__':
    # # 第一条数据
    # date = '2022-08-01'
    # group = 1
    # name_set = ("轩辕", "求索", "羲和", "一行")
    # line1 = {date + '/group' + str(group) :set(name_set)}
    
    # # 第二条数据
    # date = '2022-07-30'
    # group = 1
    # name_set = ("归藏", "求索", "微光", "一行")
    # line2 = {date + '/group' + str(group) :set(name_set)}

    # # 第三条数据
    # date = '2022-07-29'
    # group = 1
    # name_set = ("蒙吉", "灵溪", "盼兮", "羲和", "轩辕")
    # line3 = {date + '/group' + str(group) :set(name_set)}

    # # 创建数据集
    # dataset = {}
    # dataset.update(line1)
    # dataset.update(line2)
    # dataset.update(line3)
    # # print(dataset)

    address = 'data.txt'
    dataset = read_data(address)

    # 计算
    result = count(dataset)
    # print(result)
    # 按照value降序排列
    # 保存为字典后，按字典的value值大小排序，这个才是本题的难点，由于dict是无序的，所以只能用list去排序，把dict的key和value保存为tuple对象
    sorted_result = sorted(result.items(), key=lambda item:item[1], reverse=True)
    print(sorted_result)