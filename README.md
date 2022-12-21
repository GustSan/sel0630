# sel0630
 Primeiro, tiramos uma foto utilizando câmera, alterando sua resolução e imprimindo na tela, o texto escrito entre aspas (neste caso foi o número USP).
 
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
camera.annotate_text = "7652550"
camera.annotate_text_size = 150
sleep(3)
camera.capture('/home/sel/7652550/foto.jpg')
camera.stop_preview()

Depois, o criamos um código para obter as informações climáticas de uma estação de medição próxima à São Carlos e gravar um vídeo de 5 segundos. Depois que o vídeo
fosse gravado, o código iria imprimir na tela as informações climáticas obtidas. 

from picamera import PiCamera
from time import sleep
from requests import get
import json
from pprint import pprint

camera = PiCamera()

tations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

weather = weather + str(966583)

my_weather = get(weather).json()['items']

camera.start_preview()
camera.start_recording('/home/sel/7652550/video_clima.h264')
camera.annotate_text = "Clima"
camera.annotate_text_size = 150
sleep(5)
camera.stop_recording()
camera.stop_preview()
pprint(my_weather)
