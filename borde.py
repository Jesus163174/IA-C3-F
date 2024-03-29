import numpy as np
import cv2
import tensorflow
import keras
#Cargar la mascara
imagen = cv2.imread('vueltaU/1.jpg',0)
 
#Crear un kernel de '1' de 3x3
kernel = np.ones((3,3),np.uint8)
 
#Se aplica la transformacion: Morphological Gradient
transformacion = cv2.dilate(imagen,kernel,iterations = 1) - cv2.erode(imagen,kernel,iterations = 1)
 
#Mostrar el resultado y salir
cv2.imshow('resultado',transformacion)
cv2.waitKey(0)
cv2.destroyAllWindows()


print('tensorflow: %s' % tensorflow.__version__)
# keras

print('keras: %s' % keras.__version__)