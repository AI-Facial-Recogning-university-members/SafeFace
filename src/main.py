import os
import cv2
import numpy as np
from database import add_funcionario, create_table

ESC = 27

# função que vai retornar uma lista com
# - nome
# - cpf
# - data de nascimento
# nessa ordem
def get_funcionario_info() -> list:
	worker_name = input("Nome do funcionario: ")
	worker_cpf = input("Cpf do funcionario: ")
	worker_birth_date = input("Data de nascimento do funcionario: ")

	return [worker_name, worker_cpf, worker_birth_date]

def move_img(img) -> None:
	# nome do diretório para guardar as imagens
	dirname = "faces/"

	# irá verificar se o diretório que
	# está dentro de "dirname" não existe
	if(not os.path.isdir(dirname)):
		os.mkdir(dirname)

	os.rename(img, f"{dirname}/{img}")

# https://note.nkmk.me/en/python-opencv-imread-imwrite/
def save_face(wname, frame) -> None:
	# vai gerar o nome da imagem para salvar
	img_name = wname + ".png"
	# vai salvar o momento atual da webcam em uma foto
	cv2.imwrite(img_name, frame)
	# vai mover a imagem do diretório atual para o diretório das imagems
	move_img(img_name)

def main() -> int:
	create_table()

	worker = get_funcionario_info()

	add_funcionario(worker[0], worker[1], worker[2])

	cap = cv2.VideoCapture(0)

	while(True):
		succ, frame = cap.read()

		if(not succ):
			print("Something went wrong while trying to access webcam.")
			break

		cv2.imshow("Your face", frame)

		# se o usuário sair salve uma foto dele
		if((cv2.waitKey(5) & 0xFF) == ESC):
			save_face(worker[0], frame)
			print("Saindo...")
			break

if(__name__ == "__main__"):
	main()
