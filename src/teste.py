import cv2
import mediapipe as mp
import face_recognition
import numpy as np
import os

# Inicializa MediaPipe
desenho = mp.solutions.drawing_utils
reconhecedor_rosto = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.5)

# Listas globais de encodings e nomes conhecidos
conhecidos_encodings = []
nomes = []

def carregar_imagens_da_pasta(pasta):
    """
    Carrega todas as imagens de uma pasta e adiciona os encodings à lista de conhecidos.
    """
    for arquivo in os.listdir(pasta):
        if arquivo.endswith((".jpg", ".png")):
            caminho_arquivo = os.path.join(pasta, arquivo)
            nome = os.path.splitext(arquivo)[0]
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
    cv2.putText(frame, nome, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

def analisar_rosto_em_tempo_real():
    """
    Captura a webcam, detecta e analisa rostos em tempo real.
    """
    webcam = cv2.VideoCapture(0)

    if not webcam.isOpened():
        print("[ERROR] Não foi possível acessar a webcam.")
        return

    try:
        while True:
            ret, frame = webcam.read()
            if not ret:
                print("[ERROR] Falha ao capturar frame da webcam.")
                break

            # Redimensiona o frame para melhorar a performance
            frame_redimensionado = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            imagem_rgb = cv2.cvtColor(frame_redimensionado, cv2.COLOR_BGR2RGB)

            # Detecção de rostos com MediaPipe
            resultado_rostos = reconhecedor_rosto.process(imagem_rgb)

            if resultado_rostos.detections:
                face_locations = face_recognition.face_locations(imagem_rgb)
                face_encodings = face_recognition.face_encodings(imagem_rgb, face_locations)

                for face_encoding, face_location in zip(face_encodings, face_locations):
                    matches = face_recognition.compare_faces(conhecidos_encodings, face_encoding)
                    nome = "Desconhecido"

                    if True in matches:
                        best_match_index = np.argmin(face_recognition.face_distance(conhecidos_encodings, face_encoding))
                        nome = nomes[best_match_index]

                    # Ajustar as coordenadas para o frame original
                    face_location = [int(coord * 2) for coord in face_location]
                    desenhar_retangulo_rosto(frame, face_location, nome)

            cv2.imshow("Rostos na sua webcam", frame)

            if cv2.waitKey(5) == 27:  # ESC para sair
                break
    except Exception as e:
        print(f"[ERROR] Erro durante a execução: {e}")
    finally:
        webcam.release()
        cv2.destroyAllWindows()

# Exemplo de uso
if __name__ == "__main__":
    carregar_imagens_da_pasta("imagens_conhecidas")
    analisar_rosto_em_tempo_real()
