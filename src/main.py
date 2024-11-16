from teste import carregar_imagens_da_pasta, analisar_rosto_em_tempo_real

def main():
    # Define o caminho para a pasta de imagens
    pasta_imagens = "img"

    # Carrega as imagens automaticamente
    carregar_imagens_da_pasta(pasta_imagens)

    # Inicia o reconhecimento facial em tempo real
    analisar_rosto_em_tempo_real()

if __name__ == "__main__":
    main()

    ''' so apertar esq pra sair'''
