import xml
import xml.etree.ElementTree as ET
import os
from os import getcwd

sets = [('2007', 'train')]  # 设置输出选项

classes = ["harbor"]  # 分类结果设置


def convert_annotation(year, image_id, list_file):
    in_file = open('VOCdevkit/DIOR+TGRS/Annotation/%s.xml' % image_id)
    tree = ET.parse(in_file)  # 将xml文档解析为ElementTree对象
    root = tree.getroot()  # 获取element类的树根

    for obj in root.iter('object'):  # 遍历root下面的所有object项目
        difficult = 0
        if obj.find('difficult') is not None:
            difficult = obj.find('difficult').text
        cls = obj.find('name').text  # 把这个object的‘name’中内容放入到cls中。（提出xml文件中物体的类型名）
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
             int(xmlbox.find('ymax').text))  # 输出每一个object中bndbox的四个参数
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))
        # 生成图片文件的路径+图片中所有bnbbox的参数+name参数在classes中的序号


wd = getcwd()    # 得到当前路径

for year, image_set in sets:
    if not os.path.exists('F:\\YOLO v3 data\\keras-yolo3\\VOCdevkit\\DIOR+TGRS\\label'):
        os.makedirs('F:\\YOLO v3 data\\keras-yolo3\\VOCdevkit\\DIOR+TGRS\\label\\')  # 新建一个 label 文件夹，用于存放yolo格式的标签文件：000001.txt
    image_ids = open('F:\\YOLO v3 data\\keras-yolo3\\VOCdevkit\\DIOR+TGRS\\ImageSets\\Main\\%s.txt' % image_set).read().strip().split()
    #image_ids = open('F:\\YOLO v3 data\\keras-yolo3\\Test\\ImageSets\\Main\\test.txt').read().strip().split()
    # 打开文件，read（）读取所有文件内容,strip为删除空白字符包括'\n', '\r', '\t',  ' '，split为按照字符串分割
    # 把xml文件名全部放入 image_ids列表
    list_file = open('%s_%s.txt' % (year, image_set), 'w')    # 生成2007—test，2007-train，2007-val文件
    for image_id in image_ids:
        list_file.write('%s/VOCdevkit/DIOR+TGRS/JPEGImage/%s.jpg' % (wd, image_id))     # 生成xml文件对应图片路径
        try:
            convert_annotation(year, image_id, list_file)
        except xml.etree.ElementTree.ParseError:
            print("%s读取错误" % image_id)
            continue
        list_file.write('\n')
    list_file.close()
