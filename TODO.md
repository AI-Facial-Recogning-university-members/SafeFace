# Todo

- Criar interface gráfica
- Finalizar reconhecimento facial
- Melhorar código

## App desktop -> Programação ( marcar um x na frente se ja foi feito ) 
    - Page 1 -> Principal:
        botoes: 
            Cadastrar
            Excluir
            Executar (execução do programa principal) -> "Linkar main.py"
    
    - Page 2 -> Cadastro:
        Formulario: -> { Todas as informações sendo linkadas diretamente ao database } 
            label :     x
                nome    x
                cpf     x
            botoes:     
                Cadastrar
                Adicionar foto do funcioanrio -> foto vai ser capturada e enviada à pasta ./img -> (um dos botoes principais)
                Voltar ->(Voltar à pagina principal)   -> "page inside page" 

    - Page 3 -> Editar/Excluir (NECESSARIO REVISAO PARA MELHOR APRIMORAMENTO DA PAGINA)
        - Ligação "page inside page":
            Page 1
        - Tabela:
            - Todos os usuarios cadastrados
            - podendo ser selecionado dados por dados
        - Botoes:
            - Editar
            - Excluir   
            - Voltar ->(Voltar à pagina principal)   -> "page inside page"  

    - Page 4 -> Execução do programa principal -> (NECESSARIO REVISAO PARA MELHOR APRIMORAMENTO DA PAGINA)
        {AINDA NAO PENSEI EXATAMENTE COMO VAI SER ESSA PAGINA}





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