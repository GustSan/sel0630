from picamera import PiCamera
from time import sleep
from requests import get
import json
from pprint import pprint

camera = PiCamera()

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations' # Obtém o Id da estação climática mais próxima da sua posição
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/' # Obtém os dados climáticos do ID da estação mais próxima da sua posição

weather = weather + str(966583) # Obtém os dados climáticos da sua posição

my_weather = get(weather).json()['items'] # Seleciona os dados e os atribui à variavel my_weather

camera.start_preview()
camera.start_recording('/home/sel/7652550/video_clima.h264') # a partir da camera, inicia a gravaçãp de um vídeo
camera.annotate_text = "Clima"
camera.annotate_text_size = 150
sleep(5)
camera.stop_recording()
camera.stop_preview()
pprint(my_weather) #imprime na tela os dados climáticos obtidos