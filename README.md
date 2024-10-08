# data_convert

coco 、voc 、yolo数据标签格式转换


YOLO(txt)和VOC(xml)之间的格式转换：YOLO转VOC运行yolo2voc.py，
                                  VOC转YOLO运行voc2yolo.py;

YOLO(txt)和COCO(json)之间的格式转换：YOLO转COCO首先运行yolo2coco_1.py,再运行yolo2coco_2.py，
                                    COCO转YOLO运行coco2yolo.py；

VOC（xml）和COCO（json）之间的格式转换：VOC转COCO运行voc2coco.py,
                                      COCO转VOC运行coco2voc.py。