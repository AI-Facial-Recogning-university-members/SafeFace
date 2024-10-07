import os
import cv2
import numpy as np

ESC = 27

def move_img(img: str) -> None:
	# vai remover "./" do nome da imagem e só deixar "user.png"
	formated_img_name = img.strip("./")
	os.rename(img, f"faces/{formated_img_name}")

# https://note.nkmk.me/en/python-opencv-imread-imwrite/
def save_face(frame: np.array) -> None:
	user_img_name = "./user.png"
	# vai salvar o momento atual da webcam em uma foto
	cv2.imwrite(user_img_name, frame)
	# vai mover a imagem do diretório atual para o diretório "images"
	move_img(user_img_name)

def main() -> int:
	cap = cv2.VideoCapture(0)

	while(True):
		succ, frame = cap.read()

		if(not succ):
			print("Something went wrong.")
			break

		cv2.imshow("Your face", frame)

		# se o usuário sair save uma foto dele
		if((cv2.waitKey(5) & 0xFF) == ESC):
			save_face(frame)
			print("Exiting...")
			break

if(__name__ == "__main__"):
	main()
