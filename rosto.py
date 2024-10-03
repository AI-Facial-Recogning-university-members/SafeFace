import face_recognition
import cv2

carregar_imagem = face_recognition.load_image_file("biden.jpg")



ler_imagem = face_recognition.face_locations(carregar_imagem)