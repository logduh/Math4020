#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import scipy
from tensorflow.keras import models, layers, utils, Backend as K
import matplotlib.pyplot as plt
import shap
import tensorflow as tf
import os

def get_images(foldername):
    images = []
    for filename in os.listdir(foldername):
        img = cv2.imread(os.path.join(foldername,filename))
        if img is not None:
            images.append(img)
            re


# In[ ]:




