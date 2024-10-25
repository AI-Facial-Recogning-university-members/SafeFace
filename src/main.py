import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess

# Carregando imagens e nomes
conhecidos_encodings = []
nomes = []

def cadastrar():
    subprocess.run(["python", r'./src/page2.py'])

def exdit():
    print("Excluir botão pressionado!")

def executar():
    subprocess.run(["python", "PrintFace.py"])

def desenhar_retangulo_rosto(frame, local_rosto, nome) -> None:
	# Desenhando o retângulo ao redor do rosto e o nome
	top, right, bottom, left = local_rosto
	cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
	cv2.putText(frame, nome, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255))

def desenhar_rosto(frame, desenho, rosto) -> None:
	# Desenhando o rosto detectado
	desenho.draw_detection(frame, rosto)

	# Obtendo localizações dos rostos no frame atual
	face_locations = face_recognition.face_locations(frame)
	face_encodings = face_recognition.face_encodings(frame, face_locations)
	nome = "Desconhecido"

	for face_encoding, face_location in zip(face_encodings, face_locations):
		# Comparando rostos detectados com rostos conhecidos
		matches = face_recognition.compare_faces(conhecidos_encodings, face_encoding)

		face_distances = face_recognition.face_distance(conhecidos_encodings, face_encoding)
		best_match_index = np.argmin(face_distances)

		if matches[best_match_index]:
			nome = nomes[best_match_index]

		desenhar_retangulo_rosto(frame, face_locations, nome)

def carregar_imagem(nome_arquivo, nome):
	imagem = face_recognition.load_image_file(nome_arquivo)
	encoding = face_recognition.face_encodings(imagem)[0]
	conhecidos_encodings.append(encoding)
	nomes.append(nome)

def main() -> int:
	app = ttk.Window(themename="superhero")
	app.title("SAFEFACE")
	app.geometry("750x700")

	label = ttk.Label(app, text="SAFEFACE")
	label.grid(row=0, column=0, columnspan=3, pady=35)
	label.config(font=("Arial", 30, "bold"))
	btn_cadastrar = ttk.Button(app, text="Cadastrar", command=cadastrar)
	btn_cadastrar.grid(row=1, column=0, padx=20, pady=20, ipadx=10, ipady=10)

	btn_exdit = ttk.Button(app, text="Excluir ou Editar", command=exdit)
	btn_exdit.grid(row=1, column=1, padx=20, pady=20, ipadx=10, ipady=10)

	btn_executar = ttk.Button(app, text="Executar", command=executar)
	btn_executar.grid(row=1, column=2, padx=20, pady=20, ipadx=10, ipady=10)

	app.grid_columnconfigure(0, weight=1)
	app.grid_columnconfigure(1, weight=1)
	app.grid_columnconfigure(2, weight=1)

	app.mainloop()

	return 0

if(__name__ == "__main__"):
	main()
