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

# Fonte do Texto
fonte = cv2.FONT_HERSHEY_PLAIN

def desenhar_retangulo_rosto(frame, local_rosto, nome) -> None:
    top, right, bottom, left = local_rosto
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(frame, nome, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

def desenhar_rosto(frame, desenho, rosto) -> None:
    name = "Desconhecido"
    desenho.draw_detection(frame, rosto)
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(conhecidos_encodings, face_encoding)
        face_distances = face_recognition.face_distance(conhecidos_encodings, face_encoding)

        try:
            best_match_index = np.argmin(face_distances)
        except ValueError:
            continue

        if matches[best_match_index]:
            name = nomes[best_match_index]

        desenhar_retangulo_rosto(frame, face_location, name)

def carregar_imagem(nome_arquivo, nome):
    imagem = face_recognition.load_image_file(nome_arquivo)
    encoding = face_recognition.face_encodings(imagem)[0]
    conhecidos_encodings.append(encoding)
    nomes.append(nome)

def mostrar_atalhos(frame):
    cv2.putText(frame, "ESQ: Sair", (10, 25), fonte, 1, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, "ENTER: Tirar Foto", (10, 50), fonte, 1, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, "SPACE: Tirar Foto Novamente", (10, 75), fonte, 1, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, "P: Confirmar", (10, 100), fonte, 1, (0, 0, 255), 1, cv2.LINE_AA)

# Função para exibir a imagem capturada e confirmar seu salvamento
def tirar_foto(frame):
    cv2.imshow("Foto tirada", frame)
    cv2.waitKey(0)  # Aguarda até que o usuário pressione uma tecla pq é burro pra porra

def salvar_foto(img):
    caminho_imagem = r'.\src\img\foto_confirmada.jpg'  # Definindo uma extensão de imagem válida
    cv2.imwrite(caminho_imagem, img)
    print(f"Foto confirmada e salva como '{caminho_imagem}'")



foto_temporaria = None

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

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC
        break  
    elif key == 13:  # ENTER (tirar foto e mostrar para confirmação)
        foto_temporaria = frame.copy()
        tirar_foto(foto_temporaria)
    elif key == ord('p') and foto_temporaria is not None:  # P para confirmar e salvar
        salvar_foto(foto_temporaria)
        break
        
        foto_temporaria = None  # Reseta a foto temporária após salvar
    elif key == 32:  # SPACE para tirar foto novamente
        tirar_foto(frame)  # Exibe a nova foto capturada
        
        

webcam.release()
cv2.destroyAllWindows()
