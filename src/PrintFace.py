import cv2
import mediapipe as mp
import face_recognition
import numpy as np
import os





conhecidos_encodings = []
nomes = []

# Inicializa MediaPipe e OpenCV
webcam = cv2.VideoCapture(0)
reconhecimento_rosto = mp.solutions.face_detection
desenho = mp.solutions.drawing_utils
reconhecedor_rosto = reconhecimento_rosto.FaceDetection()

# Fonte text
fonte = cv2.FONT_HERSHEY_PLAIN

# Função para desenhar o retângulo e nome no rosto (ver se precisa mudar a cor para diferenciar)
def desenhar_retangulo_rosto(frame, local_rosto, nome):
    top, right, bottom, left = local_rosto
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(frame, nome, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

# Função para desenhar rostos detectados
def desenhar_rosto(frame, desenho, rosto):
    name = "Desconhecido"
    desenho.draw_detection(frame, rosto)

    # Obtendo localizações dos rostos no frame 
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Comparando rostos detectados com rostos da pasta /img
        matches = face_recognition.compare_faces(conhecidos_encodings, face_encoding)
        face_distances = face_recognition.face_distance(conhecidos_encodings, face_encoding)

        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = nomes[best_match_index]

        desenhar_retangulo_rosto(frame, face_location, name)

# Função para carregar imagem e adicionar o encoding
def carregar_imagem(nome_arquivo, nome):
    imagem = face_recognition.load_image_file(nome_arquivo)
    encoding = face_recognition.face_encodings(imagem)[0]
    conhecidos_encodings.append(encoding)
    nomes.append(nome)

# Função para mostrar atalhos
def mostrar_atalhos(frame):
    cv2.putText(frame, "ESQ: Sair", (10, 25), fonte, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "ENTER: Tirar Foto", (10, 50), fonte, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "SPACE: Tirar Foto Novamente", (10, 75), fonte, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "P: Confirmar", (10, 100), fonte, 1, (0, 0, 255), 2, cv2.LINE_AA)

# Função principal para analisar rostos
def analisar_rosto(nome):
    while webcam.isOpened():
        validacao, frame = webcam.read()
        if not validacao:
            break

        mostrar_atalhos(frame)

        imagem_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        lista_rostos = reconhecedor_rosto.process(imagem_rgb)

        if lista_rostos.detections:
            for rosto in lista_rostos.detections:
                desenhar_rosto(frame, desenho, rosto)

        cv2.imshow("Rostos na sua webcam", frame)

        # Tirar e salvar foto quando ENTER é pressionado
        if cv2.waitKey(5) == 13:  # ENTER
            caminho = f"img/{nome}.jpg"
            os.makedirs(os.path.dirname(caminho), exist_ok=True)
            cv2.imwrite(caminho, frame)
            foto = cv2.imread(caminho)
            cv2.imshow("Foto", foto)
            cv2.waitKey(0)  # Espera qualquer tecla para fechar a foto (ver se precisa ser removido)
            cv2.destroyWindow("Foto")

        # Sair com ESC
        if cv2.waitKey(5) == 27:  # ESC
            break

    webcam.release()
    cv2.destroyAllWindows()
    
