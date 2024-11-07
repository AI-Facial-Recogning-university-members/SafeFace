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

def carregar_imagem(nome_arquivo, nome):
    imagem = face_recognition.load_image_file(nome_arquivo)
    encoding = face_recognition.face_encodings(imagem)[0]
    conhecidos_encodings.append(encoding)
    nomes.append(nome)

# Adicione suas imagens aqui
# carregar_imagem("./img/gustavo.jpg", "Gustavo")
# carregar_imagem("./img/leoo.jpg", "Leonardo")

while webcam.isOpened():
    validacao, frame = webcam.read()
    if not validacao:
        break
    imagem_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    lista_rostos = reconhecedor_rosto.process(imagem_rgb)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            # Desenhando o rosto detectado
            desenho.draw_detection(frame, rosto)
            
            # Obtendo localizações dos rostos no frame atual
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)
            
            for face_encoding, face_location in zip(face_encodings, face_locations):
                # Comparando rostos detectados com rostos conhecidos
                matches = face_recognition.compare_faces(conhecidos_encodings, face_encoding)
                name = "Desconhecido"
                
                face_distances = face_recognition.face_distance(conhecidos_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = nomes[best_match_index]

                # Desenhando o retângulo ao redor do rosto e o nome
                top, right, bottom, left = face_location
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Rostos na sua webcam", frame)
    if cv2.waitKey(5) == 27:  # ESC
        break

webcam.release()
cv2.destroyAllWindows()
