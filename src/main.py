import os
import cv2
import mediapipe as mp
import face_recognition
import numpy as np

PRINT_KEY = 112

# Carregando imagens e nomes
conhecidos_encodings = []
nomes = []

def mover_imagem(img) -> None:
	# vai retirar a imagem do diretorio atual e mover ela
	# para "img/"
	os.rename(img, f"../img/{img}")

def salvar_rosto(frame, nome = "Desconhecido") -> None:
	imagem = f"{nome}.jpg"

	# vai salvar o momento atual da webcam em uma foto
	# https://note.nkmk.me/en/python-opencv-imread-imwrite/
	cv2.imwrite(imagem, frame)

	# vai mover a imagem do diretório atual para o diretório "images"
	mover_imagem(imagem)

def desenhar_retangulo_rosto(frame, local_rosto, nome) -> None:
	# Desenhando o retângulo ao redor do rosto e o nome
	top, right, bottom, left = local_rosto
	cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
	cv2.putText(frame, nome, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255))

def desenhar_rosto(frame, desenho, rosto) -> None:
	# Desenhando o rosto detectado
	desenho.draw_detection(frame, rosto)

	# Obtendo localizações dos rostos no frame atual
	face_locations = face_recognition.face_locations(frame)
	face_encodings = face_recognition.face_encodings(frame, face_locations)
	nome = "Desconhecido"

	for face_encoding, face_location in zip(face_encodings, face_locations):
		# Comparando rostos detectados com rostos conhecidos
		matches = face_recognition.compare_faces(conhecidos_encodings, face_encoding)

		face_distances = face_recognition.face_distance(conhecidos_encodings, face_encoding)
		best_match_index = np.argmin(face_distances)

		if matches[best_match_index]:
			nome = nomes[best_match_index]

			desenhar_retangulo_rosto(frame, face_locations, nome)

def carregar_imagem(nome_arquivo, nome):
	imagem = face_recognition.load_image_file(nome_arquivo)
	encoding = face_recognition.face_encodings(imagem)[0]
	conhecidos_encodings.append(encoding)
	nomes.append(nome)


def main() -> int:
	# Inicializando MediaPipe e OpenCV
	webcam = cv2.VideoCapture(0)
	desenho = mp.solutions.drawing_utils
	reconhecimento_rosto = mp.solutions.face_detection
	reconhecedor_rosto = reconhecimento_rosto.FaceDetection()
	
	carregar_imagem("../img/gustavo.jpg", "Gustavo")
	carregar_imagem("../img/leoo.jpg", "Leonardo")

	while(webcam.isOpened()):
		validacao, frame = webcam.read()

		if not validacao:
			break

		imagem_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		lista_rostos = reconhecedor_rosto.process(imagem_rgb)

		if lista_rostos.detections:
			for rosto in lista_rostos.detections:
				desenhar_rosto(frame, desenho, rosto)

		cv2.imshow("Rostos na sua webcam", frame)
		
		if cv2.waitKey(5) == PRINT_KEY:
			salvar_rosto(frame)

		if cv2.waitKey(5) == 27:  # ESC
			break

	webcam.release()
	cv2.destroyAllWindows()

	return 0

if(__name__ == "__main__"):
	main()
