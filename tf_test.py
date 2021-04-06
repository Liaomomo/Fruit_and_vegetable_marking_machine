#!/usr/bin/env python
# coding: utf-8

# # Imports
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import time
import Get_Weight
import threading


from distutils.version import StrictVersion
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
# This is needed since the notebook is stored in the object_detection folder.

import cv2

from utils import label_map_util

from utils import visualization_utils as vis_util

#声明全局变量返回检测到的类别
Class='';


def jisu():
    while 1:
        print(2)

#实时视频检测
def kk():
    global Class
    sys.path.append("..")
    if StrictVersion(tf.__version__) < StrictVersion('1.9.0'):
        raise ImportError('Please upgrade your TensorFlow installation to v1.9.* or later!')
    cap = cv2.VideoCapture(1)

    MODEL_NAME = 'detection_model'
    PATH_TO_FROZEN_GRAPH = MODEL_NAME + '/frozen_inference_graph.pb'
    PATH_TO_LABELS = os.path.join('data', 'model_label.pbtxt')
    detection_graph = tf.Graph()

    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)

    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            while True:
                ret, image_np = cap.read()

                image_np_expanded = np.expand_dims(image_np, axis=0)
                image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

                boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

                scores = detection_graph.get_tensor_by_name('detection_scores:0')
                classes = detection_graph.get_tensor_by_name('detection_classes:0')
                num_detections = detection_graph.get_tensor_by_name('num_detections:0')

                (boxes, scores, classes, num_detections) = sess.run(
                    [boxes, scores, classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})
                # boxes=boxes[scores>0.7]
                vis_util.visualize_boxes_and_labels_on_image_array(
                    image_np, np.squeeze(boxes),
                    np.squeeze(classes).astype(np.int32),
                    np.squeeze(scores), category_index,
                    use_normalized_coordinates=True,
                    line_thickness=8)
                cv2.imshow('object detection', cv2.resize(image_np, (1080, 800)) )
                # Obj_class=dir[int(classes[0][0])], scores[0][0])
                dir = {1: "红富士", 2: "红蛇果", 3:"上海青"}

                if scores[0][0] >= 0.6 :

                    if(scores[0][0]>=0.7 ):
                        Class = dir[int(classes[0][0])]


                else:
                    Class=''

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break
    cap.release()
    cv2.destroyAllWindows()




# 获得重量
def get_weight():
    Class_secone=''
    weight_secone=''
    while True:
       weight = Get_Weight.get_weight()
       #价格检索
       dir_price={"红富士":"8.0元/500g","红蛇果":"16.9元/500g","上海青":"2.4元/500g"}
       #判断用户什么时候离开
       if Class!=''and Class_secone!=Class and weight_secone!=weight:
           # f = open("./data\\1.txt",'w',encoding="utf-8")
           # f.write("类别：{}\n单价：8元/500g\n重量：{}\n总价：{}元".format(Class,weight,int(weight[1:-3])/500*8))
           # f.close()

           try:
               print("<------------------------------------------>")
               print("类别：{}\n单价：{}\n重量：{}\n总价：{:.2f}元".format(Class,dir_price[Class],weight,int(weight[1:-3])/500*float(dir_price[Class].split("元")[0])))
               print("<------------------------------------------>")

           except:
               print()
           weight_secone=weight
           Class_secone = Class

       #判断物体是否离开称重机
       if  weight_secone!=weight:
           Class_secone = Class


if __name__ == '__main__':
    threading.Thread(target=kk).start()
    threading.Thread(target=get_weight).start()















