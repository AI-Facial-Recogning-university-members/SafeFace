# Todo

- Criar interface gráfica
- Finalizar reconhecimento facial
- Melhorar código

##  Teste.py
    - Fazer um looping com as imagens  dentro da pag \img
        - Dentro do looping fazer uma comparação com as imagens e com o que a camera esta captando .
            - Usando a função "   os.listdir   " -> para pasta \img

## Ideia
    -Dar resize na área da mascára -> foi feito porem o desempenho nao melhorou.

## Erro
    -Printface iniciando antes do esperado quando clica em cadastro




## For developers:
### How create a struct project:
    - main.py = principal code
    - database.py = the name justifies
    - face_recognition.py = module for recognition
    - faces/ = directory for stock face images
    - funcionarios.db = Data base SQLITE3 "(Is create automatic when you run sqlite(db))"

# Como instalar as bibliotecas importadas no main.py
    mediapipe = " pip install mediapipe "
    cv2 = " pip install opencv-python "
    face_recognition = " pip install face_recognition "