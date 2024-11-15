import cv2
import mediapipe as mp
import face_recognition
import numpy as np
import os


# Carregando imagens e nomes conhecidos
conhecidos_encodings = []
nomes = []

def desenhar_retangulo_rosto(frame, local_rosto, nome) -> None:
    top, right, bottom, left = local_rosto
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(frame, nome, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

def desenhar_rosto(frame, desenho, rosto) -> None:
    desenho.draw_detection(frame, rosto)
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    
    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(conhecidos_encodings, face_encoding)
        nome = "Desconhecido"  # Padrão

        if True in matches:
            best_match_index = np.argmin(face_recognition.face_distance(conhecidos_encodings, face_encoding))
            nome = nomes[best_match_index] if matches[best_match_index] else nome

        desenhar_retangulo_rosto(frame, face_location, nome)

def carregar_imagem(caminho, nome):
    imagem = face_recognition.load_image_file(nome_arquivo)
    encoding = face_recognition.face_encodings(imagem)[0]
    conhecidos_encodings.append(encoding)
    nomes.append(nome)

def main() -> int:
    webcam = cv2.VideoCapture(0)
    desenho = mp.solutions.drawing_utils
    reconhecedor_rosto = mp.solutions.face_detection.FaceDetection()
    caminho = f"img/{nome}.jpg"
    os.mk(os.path.dirname(caminho), exist_ok=True)

  
    while webcam.isOpened():
        validacao, frame = webcam.read()
        if not validacao:
            break

        imagem_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        lista_rostos = reconhecedor_rosto.process(imagem_rgb)

        if lista_rostos.detections:
            for rosto in lista_rostos.detections:
                desenhar_rosto(frame, desenho, rosto)
        
        cv2.imshow("Rostos na sua webcam", frame)
        if cv2.waitKey(5) == 27:  # Tecla ESC para sair
            break

    webcam.release()
    cv2.destroyAllWindows()
    return 0

if __name__ == "__main__":
    main()