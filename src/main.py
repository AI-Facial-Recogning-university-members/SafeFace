import cv2
import numpy as np

ESC = 27

# https://note.nkmk.me/en/python-opencv-imread-imwrite/
def save_face(frame: np.array) -> None:
	# vai salvar o momento atual da webcam em uma foto
	cv2.imwrite('./user.png', frame)

def main() -> int:
	cap = cv2.VideoCapture(0)

	while(True):
		succ, frame = cap.read()

		if(not succ):
			print("Algo deu errado.")
			break

		cv2.imshow("Your face", frame)

		# se o usuário sair save uma foto dele
		if((cv2.waitKey(5) & 0xFF) == ESC):
			save_face(frame)
			print("Exiting...")
			break


if(__name__ == "__main__"):
	main()
