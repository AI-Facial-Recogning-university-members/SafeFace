import face_recognition
import numpy

imagem = face_recognition.load_image_file("biden.jpg")#Lê imagem

carregar_imagem = face_recognition.face_locations(imagem)#Detecta rosto na imagem

rosto = face_recognition.face_landmarks(imagem)#Faz um Delineado ao redor do rosto

#Nota: Achar uma forma de fazer a imagem aparecer, matplotlib talvez?

