{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyNmFTtWJJifG94IqT+42vWM"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"id":"DHpg9_NNUtWH"},"outputs":[],"source":["import os\n","import cv2\n","from PIL import Image,ImageFilter\n","import numpy as np\n","import random\n","import imgaug.augmenters as iaa"]},{"cell_type":"code","source":["\n","class augment():\n","  def augment(image, annotation):\n","          # Augmentation img\n","          aug_img = iaa.Sequential([\n","              iaa.GaussianBlur(sigma=(0, 3.0)),\n","              iaa.AdditiveGaussianNoise(scale=(0, 0.05 * 255)),\n","              iaa.Affine(rotate=(-45, 45)),\n","              iaa.Multiply((0.8, 1.2))\n","          ])\n","          image_augmented = aug_img.augment_image(image)\n","          # Augmentation annot\n","          annot_aug= iaa.Sequential([\n","              iaa.GaussianBlur(sigma=(0, 3.0)),\n","              iaa.AdditiveGaussianNoise(scale=(0, 0.05 * 255)),\n","              iaa.Affine(rotate=(-45, 45)),\n","              iaa.Multiply((0.8, 1.2))\n","          ])\n","          \n","          annotation_augmented=annot_aug.augment_image(annotation)\n","      \n","        return image_augmented,annotation_augmented\n"],"metadata":{"id":"8o7wZEE8UxT0"},"execution_count":null,"outputs":[]}]}