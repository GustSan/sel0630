from picamera import PiCamera   # Importa o módulo PiCamera da biblioteca picamera
from time import sleep          # Importa o módulo sleep da biblioteca time

camera = PiCamera()             

camera.resolution = (2592, 1944) # altera a resolução da camera
camera.framerate = 15            # define qual a taxa de frames da camera
camera.start_preview()           # inicia a câmera
camera.annotate_text = "7652550" # imprime na tela da camera o texto entre aspas
camera.annotate_text_size = 150  # define o tamanho do texto
sleep(3)                         # aguarda 3 segundos após a finalização da câmera
camera.capture('/home/sel/7652550/foto.jpg') # endereço onde o arquivo capturado será salvo
camera.stop_preview()           # encerra a câmera