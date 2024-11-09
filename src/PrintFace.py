import cv2
import mediapipe as mp
import face_recognition
import numpy as np

# Carregando imagens e nomes
conhecidos_encodings = []
nomes = []

# Inicializando MediaPipe e OpenCV
webcam = cv2.VideoCapture(0)
reconhecimento_rosto = mp.solutions.face_detection
desenho = mp.solutions.drawing_utils
reconhecedor_rosto = reconhecimento_rosto.FaceDetection()

#Fonte do Texto
fonte = cv2.FONT_HERSHEY_PLAIN

def desenhar_retangulo_rosto(frame, local_rosto, nome) -> None:
	# Desenhando o retângulo ao redor do rosto e o nome
	top, right, bottom, left = local_rosto
	cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
	cv2.putText(frame, nome, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255))

def desenhar_rosto(frame, desenho, rosto) -> None:
	name = "Desconhecido"

	# Desenhando o rosto detectado
	desenho.draw_detection(frame, rosto)

	# Obtendo localizações dos rostos no frame atual
	face_locations = face_recognition.face_locations(frame)
	face_encodings = face_recognition.face_encodings(frame, face_locations)

	for face_encoding, face_location in zip(face_encodings, face_locations):
		# Comparando rostos detectados com rostos conhecidos
		matches = face_recognition.compare_faces(conhecidos_encodings, face_encoding)

		face_distances = face_recognition.face_distance(conhecidos_encodings, face_encoding)

		try:
			best_match_index = np.argmin(face_distances)
		except ValueError:
			continue

		if matches[best_match_index]:
			name = nomes[best_match_index]

		desenhar_retangulo_rosto(frame, (128, 75, 80, 55), name)

def carregar_imagem(nome_arquivo, nome):
	imagem = face_recognition.load_image_file(nome_arquivo)
	encoding = face_recognition.face_encodings(imagem)[0]
	conhecidos_encodings.append(encoding)
	nomes.append(nome)

#Função para mostrar atalhos
def mostrar_atalhos():
    #Atalho de uma cor, função de outra
    cv2.putText(frame, "ESQ:Sair",(0, 25),fonte, 2, (0,0,255),1, cv2.LINE_8)
    cv2.putText(frame, "ENTER:Tirar Foto",(0, 50),fonte, 2, (0,0,255),1, cv2.LINE_8)#Tem que mostrar a foto dps de tirada
    cv2.putText(frame, "SPACE:Tirar Foto Novamente",(0, 75),fonte, 2, (0,0,255),1, cv2.LINE_8)
    cv2.putText(frame, "P:Confirmar",(0, 100),fonte, 2, (0,0,255),1, cv2.LINE_8)

# Adicione suas imagens aqui
# carregar_imagem("./img/gustavo.jpg", "Gustavo")
# carregar_imagem("./img/leoo.jpg", "Leonardo")

def analisar_rosto(nome):
	while webcam.isOpened():
		validacao, frame = webcam.read()
		mostrar_atalhos()

		if not validacao:
			break

		imagem_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		lista_rostos = reconhecedor_rosto.process(imagem_rgb)

		if lista_rostos.detections:
			for rosto in lista_rostos.detections:
				desenhar_rosto(frame, desenho, rosto)

		cv2.imshow("Rostos na sua webcam", frame)

		if cv2.waitKey(5) == 32:	# SPACE
				cv2.imwrite(f"img/{nome}.jpg", frame)#Aqui tem que sair o nome da pessoa +jpg
				foto = cv2.imread(f"img/{nome}.jpg")
				cv2.imshow("Foto", foto)
				cv2.waitKey(0)#Deixa a foto mostrando até QUALQUER tecla ser apertada
				cv2.destroyWindow("Foto")

		if cv2.waitKey(5) == 27:	# ESC
			break

webcam.release()
cv2.destroyAllWindows()
