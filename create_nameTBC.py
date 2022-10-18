# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 9:20
# @Author  : Saiterlz from lanzhou
# @Email   : kinekok@163.com
# @File    : create_nameTBC.py
# @Software: PyCharm
def replaceFomat(text: str, word: str, n: int, reverse=False):
    """
    对文本中的指定单词进行格式化的替换/替回
    :param text: 要替换的文本
    :param word: 目标单词
    :param n: 目标单词的序号
    :param reverse: 是否进行替回
    :return: 替换后的文本
    """
    # 构造【中间变量】
    new_text = text[:]
    fmt = "<{}>".format(n)
    # 替换
    if reverse is False:
        new_text = new_text.replace(word, fmt)  # 格式化替换
        return new_text
    # 替回
    elif reverse is True:
        new_text = new_text.replace(fmt, word)  # 去格式化替换
        return new_text
    # 要求非法，引发异常
    else:
        raise TypeError


def replaceMulti(text: str, olds: list, news: list):
    """
    一次替换多组字符串
    :param text: 要替换的文本
    :param olds: 旧字符串列表
    :param news: 新字符串列表
    :return: 替换后的文本
    """
    if len(olds) != len(news):
        raise IndexError
    else:
        new_text = text[:]
        # 格式化替换
        i = 0  # 单词计数器
        for word in olds:
            i += 1
            new_text = replaceFomat(new_text, word, i)
        # 去格式化替回
        i = 0  # 归零
        for word in news:
            i += 1
            new_text = replaceFomat(new_text, word, i, True)
        # 返回替换好的文本
        return new_text


def test2(strtext):
    temp = strtext.strip()
    olds = ['"', ",", "[", "]"]
    news = ["", "", "", ""]
    result = replaceMulti(temp, olds, news)
    strfull = result.split('=')
    print(strfull)
    strFormat = strfull[1].strip() + ':' + strfull[0].strip() +'\n'
    return strFormat


add_txt = []
with open('nameTBCold.txt', mode='r', encoding='utf-8') as f:
    for i in f.readlines():
        print(i)
        with open('nameTBC2.txt', mode='a+', encoding='utf-8')  as h:
            h.write(test2(i))
