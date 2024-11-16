import cv2
import mediapipe as mp
import face_recognition
import numpy as np
import os

# Inicializa MediaPipe
desenho = mp.solutions.drawing_utils
reconhecedor_rosto = mp.solutions.face_detection.FaceDetection()

# Listas globais de encodings e nomes conhecidos
conhecidos_encodings = []
nomes = []

def carregar_imagens_da_pasta(pasta):
    """
    Carrega todas as imagens de uma pasta e adiciona os encodings à lista de conhecidos.
    """
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".jpg") or arquivo.endswith(".png"):
            caminho_arquivo = os.path.join(pasta, arquivo)
            nome = os.path.splitext(arquivo)[0]  # Nome da pessoa baseado no nome do arquivo
            try:
                imagem = face_recognition.load_image_file(caminho_arquivo)
                encoding = face_recognition.face_encodings(imagem)[0]
                conhecidos_encodings.append(encoding)
                nomes.append(nome)
                print(f"[INFO] Carregado: {nome}")
            except IndexError:
                print(f"[WARNING] Não foi possível processar a imagem: {arquivo}")

def desenhar_retangulo_rosto(frame, local_rosto, nome):
    """
    Desenha um retângulo ao redor do rosto e exibe o nome.
    """
    top, right, bottom, left = local_rosto
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(frame, nome, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

def desenhar_rosto(frame, rosto):
    """
    Desenha os rostos detectados e identifica se são conhecidos ou desconhecidos.
    """
    desenho.draw_detection(frame, rosto)
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(conhecidos_encodings, face_encoding)
        nome = "Desconhecido"

        if True in matches:
            best_match_index = np.argmin(face_recognition.face_distance(conhecidos_encodings, face_encoding))
            nome = nomes[best_match_index] if matches[best_match_index] else nome

        desenhar_retangulo_rosto(frame, face_location, nome)

def analisar_rosto_em_tempo_real():
    """
    Captura a webcam, detecta e analisa rostos em tempo real.
    """
    webcam = cv2.VideoCapture(0)

    while webcam.isOpened():
        validacao, frame = webcam.read()
        if not validacao:
            break

        imagem_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        lista_rostos = reconhecedor_rosto.process(imagem_rgb)

        if lista_rostos.detections:
            for rosto in lista_rostos.detections:
                desenhar_rosto(frame, rosto)

        cv2.imshow("Rostos na sua webcam", frame)

        if cv2.waitKey(5) == 27:  # ESC para sair
            break

    webcam.release()
    cv2.destroyAllWindows()
