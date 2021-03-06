import requests,json, os
from time import sleep

class Movie:
    
    def busca_filme(self):

        lista = list()

        chave = '7db9f6c4'
        status = 'Pendente'
        
        while True:

            os.system('clear') 
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t         BUSCA DE FILMES E SÉRIES                   |')
            print('|___________________________________________________________|')
            sleep(1)
            
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('| 1-Filmes                                                  |')
            print('| 2-Series                                                  |')
            print('| 3-Menu                                                    |')
            print('|___________________________________________________________|')
            print('|                                                           |')
            escolha = input('| >>> ').lower().strip()
            print('|___________________________________________________________|')


            if escolha == '1':

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('| Digite o nome do filme que deseja buscar                  |')
                print('|___________________________________________________________|')
                print('|                                                           |')
                pesquisa = input('| >>> ').lower().strip()
                print('|___________________________________________________________|')

                response1 = requests.get("http://www.omdbapi.com/?apikey={}&s={}&type=movie&plot=full".format(chave,pesquisa)).json()

                if response1['Response'] == 'False':
                    
                    response = requests.get("http://www.omdbapi.com/?apikey={}&t={}&type=movie&plot=full".format(chave,pesquisa)).json()

                    if response['Response'] == 'False':
                        
                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('| \t\t   O FILME NÃO EXISTE!                      |')
                        print('|___________________________________________________________|')
                        sleep(1)

                    else:
                        
                        os.system('clear')
                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t\t    DETALHES DO FILME                       |')
                        print('|___________________________________________________________|')
                        sleep(1)
                        
                        print()

                        print('--' * 110)
                        print()
                        print(' Título: ', response['Title'])      
                        print(' Ano: ', response['Year'])
                        print(' Tempo: ', response['Runtime'])
                        print(' Genero: ', response['Genre'])
                        print(' Diretor: ', response['Director'])
                        print(' Escritor: ', response['Writer'])
                        print(' Atores: ', response['Actors'])
                        print(' País: ', response['Country'])
                        print(' Tipo: ', response['Type'].title())
                        print()
                        print('--' * 110)

                        if response['Plot'] == 'N/A':

                            sleep(1.5)
                            print(' ___________________________________________________________')
                            print('|                                                           |')
                            print('|\t       ESTE FILME NÃO CONTÉM SINOPSE                |')
                            print('|___________________________________________________________|')
                            sleep(1.5)

                            break

                        else:

                            sleep(1.5)

                            print(' ___________________________________________________________')
                            print('|                                                           |')
                            print('|\t       ESTE FILME CONTÉM SINOPSE                    |')
                            print('|___________________________________________________________|')
                            sleep(1)

                            print(' ___________________________________________________________')
                            print('|                                                           |')
                            print('| Deseja ver a sinopse do filme?                            |')
                            print('|                                                           |')
                            print('| 1-Sim                                                     |')
                            print('| 2-Não                                                     |')
                            print('|___________________________________________________________|')
                            print(' ___________________________________________________________')
                            print('|                                                           |')
                            resumo = input('| >>> ').strip()
                            print('|___________________________________________________________|')

                            if resumo == '1':

                                print(' ___________________________________________________________')
                                print('|                                                           |')
                                print('|\t\t        SINOPSE                             |')
                                print('|___________________________________________________________|')
                                sleep(1)

                                print()
                                print('-' * 229)
                                print()
                                print('', response['Plot'])
                                print()
                                print('-' * 229)
                                sleep(1)

                                break

                            elif resumo == '2':

                                break

                            else:
                                print(' ___________________________________________________________')
                                print('|                                                           |')
                                print('|\t\t      OPÇÃO INVÁLIDA                        |')
                                print('|___________________________________________________________|')
                                sleep(1)

                else:
                
                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|       SUGESTÕES DE FILMES RELACIONADAS COM O NOME!        |')
                    print('|___________________________________________________________|')
                    sleep(1)
                    
                    print()
                    print('--' * 110)

                    for tamanho in range(0, len(response1['Search'])):

                        print()
                        print(' Titulo: ', response1['Search'][tamanho]['Title'])
                        print(' Ano: ', response1['Search'][tamanho]['Year'])
                        print(' Tipo: ', response1['Search'][tamanho]['Type'])
                        print()
                        print('--' * 110)
                        sleep(1)

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('| Escolha um dos filmes acima                               |')
                    print('|___________________________________________________________|')
                    print('|                                                           |')
                    titulo = input('| >>> ').strip()
                    print('|___________________________________________________________|')
                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('| Digite o ano do filme escolhido                           |')
                    print('|___________________________________________________________|')
                    print('|                                                           |')
                    ano = input('| >>> ').strip()

                    try:

                        for tamanho in range(0, len(response1['Search'])):

                            if titulo == response1['Search'][tamanho]['Title'] or ano == response1['Search'][tamanho]['Year']:

                                response = requests.get("http://www.omdbapi.com/?apikey={}&t={}&y={}&type=movie&plot=full".format(chave,titulo, ano)).json()
                                
                                os.system('clear')
                                print(' ___________________________________________________________')
                                print('|                                                           |')
                                print('|\t\t    DETALHES DO FILME                       |')
                                print('|___________________________________________________________|')

                                sleep(1)
                                print()
                                
                                print('--' * 110)
                                print()
                                print(' Título: ', response['Title'])
                                print(' Ano: ', response['Year'])
                                print(' Tempo: ', response['Runtime'])
                                print(' Genero: ', response['Genre'])
                                print(' Diretor: ', response['Director'])
                                print(' Escritor: ', response['Writer'])
                                print(' Atores: ', response['Actors'])
                                print(' País: ', response['Country'])
                                print(' Tipo: ', response['Type'].title())
                                print()
                                print('--' * 110)

                                sleep(1.5)

                                if response['Plot'] == 'N/A':

                                    sleep(1.5)
                                    print(' ___________________________________________________________')
                                    print('|                                                           |')
                                    print('|\t       ESTE FILME NÃO CONTÉM SINOPSE                |')
                                    print('|___________________________________________________________|')

                                    sleep(1.5)

                                    break

                                else:

                                    sleep(1.5)

                                    print(' ___________________________________________________________')
                                    print('|                                                           |')
                                    print('|\t       ESTE FILME CONTÉM SINOPSE                    |')
                                    print('|___________________________________________________________|')

                                    sleep(1)

                                    print(' ___________________________________________________________')
                                    print('|                                                           |')
                                    print('| Deseja ver a sinopse do filme?                            |')
                                    print('|                                                           |')
                                    print('| 1-Sim                                                     |')
                                    print('| 2-Não                                                     |')
                                    print('|___________________________________________________________|')
                                    print(' ___________________________________________________________')
                                    print('|                                                           |')
                                    resumo = input('| >>> ')
                                    print('|___________________________________________________________|')

                                    if resumo == '1':

                                        print(' ___________________________________________________________')
                                        print('|                                                           |')
                                        print('|\t\t        SINOPSE                             |')
                                        print('|___________________________________________________________|')
                                        sleep(1)

                                        print()
                                        print('-' * 229)
                                        print()
                                        print('', response['Plot'])
                                        print()
                                        print('-' * 229)
                                        sleep(1)


                                    elif resumo == '2':

                                        break

                                    else:

                                        print(' ___________________________________________________________')
                                        print('|                                                           |')
                                        print('|\t\t      OPÇÃO INVÁLIDA                        |')
                                        print('|___________________________________________________________|')
                                        sleep(1)
                                    
                                break
                                            
                            else:
                                            
                                tamanho += 1

                            if tamanho == len(response1['Search']):
                                
                                os.system('clear')
                                print(' ___________________________________________________________')
                                print('|                                                           |')
                                print('|      ESTE FILME NÃO ESTÁ NA SUGESTÃO LISTADA ACIMA!       |')
                                print('|___________________________________________________________|')
                                sleep(1.7)
                                os.system('clear')
                                 
                            else:
                                pass

                        break

                    except KeyError:
                        
                        os.system('clear')
                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|         ESTA SUGESTÃO NÃO ESTÁ LISTADA ACIMA!             |')
                        print('|___________________________________________________________|')
                        sleep(1.7)
                        os.system('clear')
                                

            elif escolha == '2':

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('| Digite o nome da série que desejada buscar                |')
                print('|___________________________________________________________|')
                print('|                                                           |')
                pesquisa = input('| >>> ').lower().strip()
                print('|___________________________________________________________|')

                response1 = requests.get("http://www.omdbapi.com/?apikey={}&s={}&type=series&plot=full".format(chave,pesquisa)).json()
                
                if response1['Response'] == 'False':
                    
                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('| \t\t   ESTA SÉRIE NÃO EXISTE                    |')
                    print('|___________________________________________________________|')
                    sleep(1)

                else:

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|       SUGESTÕES DE SÉRIES RELACIONADAS COM O NOME!        |')
                    print('|___________________________________________________________|')
                    sleep(1)
                    
                    print('--' * 110)

                    for tamanho in range(0, len(response1['Search'])):

                        print()
                        print(' Titulo: ', response1['Search'][tamanho]['Title'])
                        print(' Ano: ', response1['Search'][tamanho]['Year'])
                        print(' Tipo: ', response1['Search'][tamanho]['Type'])
                        print()
                        print('--' * 110)
                        sleep(1)

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('| Escolha uma das series acima                              |')
                    print('|___________________________________________________________|')
                    print('|                                                           |')
                    titulo = input('| >>> ')
                    print('|___________________________________________________________|')
                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('| Digite o ano da serie escolhida                           |')
                    print('|___________________________________________________________|')
                    print('|                                                           |')
                    ano = input('| >>> ')

                    try:

                        for tamanho in range(0, len(response1['Search'])):

                            if titulo == response1['Search'][tamanho]['Title'] or ano == response1['Search'][tamanho]['Year']:

                                response = requests.get("http://www.omdbapi.com/?apikey={}&t={}&y={}&type=series&plot=full".format(chave,titulo, ano)).json()
                                
                                os.system('clear')
                                print(' ___________________________________________________________')
                                print('|                                                           |')
                                print('|\t\t    DETALHES DA SÉRIE                       |')
                                print('|___________________________________________________________|')

                                sleep(1)
                                print('--' * 110)
                                print()
                                print(' Título: ', response['Title'])
                                print(' Ano: ', response['Year'])
                                print(' Tempo: ', response['Runtime'])
                                print(' Genero: ', response['Genre'])
                                print(' Diretor: ', response['Director'])
                                print(' Escritor: ', response['Writer'])
                                print(' Atores: ', response['Actors'])
                                print(' País: ', response['Country'])
                                print(' Tipo: ', response['Type'].title())
                                print()
                                print('--' * 110)

                                if response['Plot'] == 'N/A':

                                    sleep(1.5)
                                    print(' ___________________________________________________________')
                                    print('|                                                           |')
                                    print('|\t       ESTA SÉRIE NÃO CONTÉM SINOPSE                |')
                                    print('|___________________________________________________________|')

                                    sleep(1.5)

                                    break

                                else:

                                    sleep(1.5)

                                    print(' ___________________________________________________________')
                                    print('|                                                           |')
                                    print('|\t       ESTA SÉRIE CONTÉM SINOPSE                    |')
                                    print('|___________________________________________________________|')

                                    sleep(1)

                                    print(' ___________________________________________________________')
                                    print('|                                                           |')
                                    print('| Deseja ver a sinopse da série?                            |')
                                    print('|                                                           |')
                                    print('| 1-Sim                                                     |')
                                    print('| 2-Não                                                     |')
                                    print('|___________________________________________________________|')
                                    print(' ___________________________________________________________')
                                    print('|                                                           |')
                                    resumo = input('| >>> ')
                                    print('|___________________________________________________________|')

                                    if resumo == '1':

                                        print(' ___________________________________________________________')
                                        print('|                                                           |')
                                        print('|\t\t        SINOPSE                             |')
                                        print('|___________________________________________________________|')
                                        sleep(1)

                                        print()
                                        print('-' * 229)
                                        print()
                                        print('', response['Plot'])
                                        print()
                                        print('-' * 229)
                                        sleep(1)


                                    elif resumo == '2':

                                        break

                                    else:

                                        print(' ___________________________________________________________')
                                        print('|                                                           |')
                                        print('|\t\t      OPÇÃO INVÁLIDA                        |')
                                        print('|___________________________________________________________|')
                                        sleep(1)
                                    
                                break
                                            
                            else:
                                            
                                tamanho += 1

                            if tamanho == len(response1['Search']):
                                
                                os.system('clear')
                                print(' ___________________________________________________________')
                                print('|                                                           |')
                                print('|      ESTA SÉRIE NÃO ESTÁ NA SUGESTÃO LISTADA ACIMA!       |')
                                print('|___________________________________________________________|')
                                sleep(1.7)
                                os.system('clear')
                                
                            else:
                                pass

                        break

                    except KeyError:
                        
                        os.system('clear')
                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|         ESTA SUGESTÃO NÃO ESTÁ LISTADA ACIMA!             |')
                        print('|___________________________________________________________|')
                        sleep(1.7)
                        os.system('clear')
                                
                        return

            elif escolha == '3':

                return


            else:

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t      OPÇÃO INVÁLIDA                        |')
                print('|___________________________________________________________|')
                sleep(1)


        dicionario = {
            'Titulo': response['Title'].lower(),
            'Ano': response['Year'],
            'Tempo': response['Runtime'],
            'Genero': response['Genre'],
            'Diretor': response['Director'],
            'Escritor': response['Writer'],
            'Atores': response['Actors'],
            'Pais': response['Country'],
            'Tipo': response['Type'],
            'Status': status
        }

        lista.append(dicionario)
        sleep(1)
        print(' ___________________________________________________________')
        print('|                                                           |')
        print('|\t   Deseja adicionar a lista de desejos?             |')
        print('| 1-Sim                                                     |')
        print('| 2-Não                                                     |')
        print('|___________________________________________________________|')
        print('|                                                           |')
        escolha = input('| >>> ').strip()
        print('|___________________________________________________________|')
        

        if escolha == '1':
            
            try:

                flag = True
                
                with open('wishlist.json') as arquivo:
                    desejo = json.load(arquivo)

                for item in desejo:

                    if dicionario['Titulo'] == item['Titulo'] and dicionario['Tipo'] == item['Tipo'] and dicionario['Ano'] == item['Ano']:

                        if dicionario['Tipo'] == 'movie':

                            print(' ___________________________________________________________')
                            print('|                                                           |')
                            print('|      ESSE FILME JÁ EXISTE NA SUA LISTA DE DESEJOS!        |')
                            print('|___________________________________________________________|')

                            sleep(2)
                            flag = False
                            os.system('clear') 
                            break

                        elif dicionario['Tipo'] == 'series':

                            print(' ___________________________________________________________')
                            print('|                                                           |')
                            print('|      ESSA SÉRIE JÁ EXISTE NA SUA LISTA DE DESEJOS!        |')
                            print('|___________________________________________________________|')

                            sleep(2)
                            flag = False
                            os.system('clear') 
                            break

                        else:
                            pass
                    
                    else:

                        flag = True

                if flag:

                    desejo.append(dicionario)

                    with open('wishlist.json', 'w') as lista_desejos:
                        json.dump(desejo, lista_desejos, indent=4)

                        if dicionario['Tipo'] == 'movie':
                            
                            print(' ____________________________________________________________')
                            print('|                                                            |')
                            print('| O FILME FOI ADICIONADO A SUA LISTA DE DESEJOS COM SUCESSO! |')
                            print('|____________________________________________________________|')


                        if dicionario['Tipo'] == 'series':

                            print(' ____________________________________________________________')
                            print('|                                                            |')
                            print('| A SÉRIE FOI ADICIONADA A SUA LISTA DE DESEJOS COM SUCESSO! |')
                            print('|____________________________________________________________|')

                    sleep(2)
                    os.system('clear')

                
                else:

                    flag = False

            except FileNotFoundError:

                with open('wishlist.json', 'w') as lista_desejos:
                    json.dump(lista, lista_desejos, indent=4)

                    if dicionario['Tipo'] == 'movie':
                            
                        print(' ____________________________________________________________')
                        print('|                                                            |')
                        print('| O FILME FOI ADICIONADO A SUA LISTA DE DESEJOS COM SUCESSO! |')
                        print('|____________________________________________________________|')


                    if dicionario['Tipo'] == 'series':

                        print(' ____________________________________________________________')
                        print('|                                                            |')
                        print('| A SÉRIE FOI ADICIONADA A SUA LISTA DE DESEJOS COM SUCESSO! |')
                        print('|____________________________________________________________|')

                os.system('clear')
                sleep(1)


        elif escolha == '2':

            if dicionario['Tipo'] == 'movie':

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|              O FILME NÃO FOI ADICIONADO!                  |')
                print('|___________________________________________________________|')
                sleep(1)
                os.system('clear')

            elif dicionario['Tipo'] == 'series':

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|              A SÉRIE NÃO FOI ADICIONADA!                  |')
                print('|___________________________________________________________|')
                sleep(1)
                os.system('clear')

            else:
                pass

        else:

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t      OPÇÃO INVÁLIDA                        |')
            print('|___________________________________________________________|')
            sleep(1)


    def listar(self):

        try:

            with open('wishlist.json') as arquivo:
                printar = json.load(arquivo)

                quantidade = 0

                os.system('clear')
                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t     LISTA DE DESEJOS                       |')
                print('|___________________________________________________________|')
                sleep(1)

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t      Deseja ver...                         |')
                print('|                                                           |')
                print('| 1-Filmes e Séries                                         |')
                print('| 2-Somente Filmes                                          |')
                print('| 3-Somente Séries                                          |')
                print('| 4-Menu                                                    |')
                print('|___________________________________________________________|')
                print(' ___________________________________________________________')
                print('|                                                           |')
                tipo = input('| >>> ').strip().lower()
                print('|___________________________________________________________|')

                if tipo == '1':

                    os.system('clear')
                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|          FILMES E SÉRIES DA SUA LISTA DE DESEJOS          |')
                    print('|___________________________________________________________|')
                    sleep(1.5)
                    print()

                    print('--' * 110)

                    for item in printar:

                        print()
                        print(' Título: ', item['Titulo'].title())      
                        print(' Ano: ', item['Ano'])
                        print(' Tempo: ', item['Tempo'])
                        print(' Genero: ', item['Genero'])
                        print(' Diretor: ', item['Diretor'])
                        print(' Escritor: ', item['Escritor'])
                        print(' Atores: ', item['Atores'])
                        print(' País: ', item['Pais'])
                        print(' Status: ', item['Status'])
                        print(' Tipo: ', item['Tipo'].title())
                        print()
                        print('--' * 110)
                        sleep(1)

                    print()
                    print(' VOCÊ TEM {} CONTEÚDO(S) NA SUA LISTA'.format(len(printar)))
                    print()
                    print('--' * 110)
                    sleep(1)

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|\t\t      FIM DA LISTA                          |')
                    print('|___________________________________________________________|')
                    sleep(1)

                    return
                    

                elif tipo == '2':

                    os.system('clear')

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|             FILMES DA SUA LISTA DE DESEJOS                |')
                    print('|___________________________________________________________|')
                    sleep(1)
                    print()

                    print('--' * 110)

                    for item in printar:

                        if item['Tipo'] == 'movie':

                            print()
                            print(' Título: ', item['Titulo'].title())      
                            print(' Ano: ', item['Ano'])
                            print(' Tempo: ', item['Tempo'])
                            print(' Genero: ', item['Genero'])
                            print(' Diretor: ', item['Diretor'])
                            print(' Escritor: ', item['Escritor'])
                            print(' Atores: ', item['Atores'])
                            print(' País: ', item['Pais'])
                            print(' Status: ', item['Status'])
                            print(' Tipo: ', item['Tipo'].title())
                            print()
                            print('--' * 110)
                            
                            quantidade += 1
                            sleep(1)

                        else:
                            pass

                        if quantidade == 0:

                            print(' ___________________________________________________________')
                            print('|                                                           |')
                            print('| VOCÊ NÃO TEM NENHUMA SÉRIE SALVA NA SUA LISTA DE DESEJOS! |')
                            print('|___________________________________________________________|')
                            return
                            
                    print()
                    print(' VOCÊ TEM {} FILME(S) NA SUA LISTA'.format(quantidade))
                    print()
                    print('--' * 110)
                    sleep(1)

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|\t\t      FIM DA LISTA                          |')
                    print('|___________________________________________________________|')
                    sleep(1)
                    
                    return


                elif tipo == '3':

                    os.system('clear')

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|             SÉRIES DA SUA LISTA DE DESEJOS                |')
                    print('|___________________________________________________________|')
                    sleep(1)
                    print()

                    print('--' * 110)

                    for tamanho in range(0, len(printar)):

                        if printar[tamanho]['Tipo'] == 'series':

                            print()
                            print(' Título: ', printar[tamanho]['Titulo'].title())      
                            print(' Ano: ', printar[tamanho]['Ano'])
                            print(' Tempo: ', printar[tamanho]['Tempo'])
                            print(' Genero: ', printar[tamanho]['Genero'])
                            print(' Diretor: ', printar[tamanho]['Diretor'])
                            print(' Escritor: ', printar[tamanho]['Escritor'])
                            print(' Atores: ', printar[tamanho]['Atores'])
                            print(' País: ', printar[tamanho]['Pais'])
                            print(' Status: ', printar[tamanho]['Status'])
                            print(' Tipo: ', printar[tamanho]['Tipo'].title())
                            print()
                            print('--' * 110)

                            tamanho += 1
                            quantidade += 1
                            sleep(1)

                        else:
                            pass

                    if quantidade == 0:

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('| VOCÊ NÃO TEM NENHUMA SÉRIE SALVA NA SUA LISTA DE DESEJOS! |')
                        print('|___________________________________________________________|')
                        return

                    else:

                        print()
                        print(' VOCÊ TEM {} SÉRIE(S) NA SUA LISTA'.format(quantidade))
                        print()
                        print('--' * 110)
                        sleep(1)

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|\t\t      FIM DA LISTA                          |')
                    print('|___________________________________________________________|')
                    sleep(1)

                    return

                if tipo == '4':

                    return

                else:

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|\t\t      OPÇÃO INVÁLIDA                        |')
                    print('|___________________________________________________________|')
                    sleep(1)

        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('|     NÃO EXISTE NENHUM CONTEÚDO NA SUA LISTA DE DESEJOS!      |')
            print('|______________________________________________________________|')
            sleep(1)
            os.system('clear')
            
        
    def busca_desejos(self):
        
        quantidade = 0
        try:

            os.system('clear') 
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|       BUSCA DE FILMES E SÉRIES NA LISTA DE DESEJOS        |')
            print('|___________________________________________________________|')
            sleep(1)

            with open('wishlist.json') as arquivo:
                printar = json.load(arquivo)

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('| Digite o titulo que deseja buscar na sua lista de desejos |')
            print('|___________________________________________________________|')
            print('|                                                           |')
            titulo = input('| >>> ').lower().strip()
            print('|___________________________________________________________|')

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('| Digite o ano do título escolhido                          |')
            print('|(Caso não saiba, deixe em branco)                          |')
            print('|___________________________________________________________|')
            print('|                                                           |')
            ano = input('| >>> ').strip()
            print('|___________________________________________________________|')

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('| 1-É um Filme                                              |')
            print('|     ou                                                    |')
            print('| 2-É uma Série                                             |')
            print('|___________________________________________________________|')
            print('|                                                           |')
            tipo = input('| >>> ').strip()
            print('|___________________________________________________________|')
            
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t        BUSCANDO...                         |')
            print('|___________________________________________________________|')
            sleep(1.8)
        
            print()
            print('--' * 110)

            for tamanho in range(0, len(printar)):
                   
                if tipo == '1':

                    if titulo == printar[tamanho]['Titulo'] and printar[tamanho]['Tipo'] == 'movie' or ano == printar[tamanho]['Ano']:
                        

                        if printar[tamanho]['Tipo'] == 'movie':

                            print()
                            print(' Título: ', printar[tamanho]['Titulo'].title())      
                            print(' Ano: ', printar[tamanho]['Ano'])
                            print(' Tempo: ', printar[tamanho]['Tempo'])
                            print(' Genero: ', printar[tamanho]['Genero'])
                            print(' Diretor: ', printar[tamanho]['Diretor'])
                            print(' Escritor: ', printar[tamanho]['Escritor'])
                            print(' Atores: ', printar[tamanho]['Atores'])
                            print(' País: ', printar[tamanho]['Pais'])
                            print(' Status: ', printar[tamanho]['Status'])
                            print(' Tipo: ', printar[tamanho]['Tipo'].title())
                            print()
                            print('--' * 110)
                            sleep(2)
                            
                        else:
                            break


                    if titulo != printar[tamanho]['Titulo'] or printar[tamanho]['Tipo'] != 'movie':
                        
                        tamanho += 1
                        quantidade += 1

                        if quantidade == len(printar):

                            print(' ___________________________________________________________')
                            print('|                                                           |')
                            print('| \t\t   FILME NÃO ENCONTRADO                     |')
                            print('|___________________________________________________________|')
                            return
                    

                elif tipo == '2':

                    if titulo == printar[tamanho]['Titulo'] and printar[tamanho]['Tipo'] == 'series' or ano == printar[tamanho]['Ano']:

                        if printar[tamanho]['Tipo'] == 'series':

                            print()
                            print(' Título: ', printar[tamanho]['Titulo'].title())
                            print(' Ano: ', printar[tamanho]['Ano'])
                            print(' Tempo: ', printar[tamanho]['Tempo'])
                            print(' Genero: ', printar[tamanho]['Genero'])
                            print(' Diretor: ', printar[tamanho]['Diretor'])
                            print(' Escritor: ', printar[tamanho]['Escritor'])
                            print(' Atores: ', printar[tamanho]['Atores'])
                            print(' País: ', printar[tamanho]['Pais'])
                            print(' Status: ', printar[tamanho]['Status'])
                            print(' Tipo: ', printar[tamanho]['Tipo'].title())
                            print()
                            print('--' * 110)
                            sleep(2)
                            

                        else:
                            break

                    if titulo != printar[tamanho]['Titulo'] or printar[tamanho]['Tipo'] != 'series':
                                    
                        tamanho += 1
                        quantidade += 1

                        if quantidade == len(printar):

                            print(' ___________________________________________________________')
                            print('|                                                           |')
                            print('| \t\t   SÉRIE NÃO ENCONTRADA                     |')
                            print('|___________________________________________________________|')
                            return

      
                else:

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|\t\t      OPÇÃO INVÁLIDA                        |')
                    print('|___________________________________________________________|')
                    sleep(1)

                    break


        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('|     NÃO EXISTE NENHUM CONTEÚDO NA SUA LISTA DE DESEJOS!      |')
            print('|______________________________________________________________|')
            sleep(1)
            os.system('clear')


    def mudar(self):

        try:

            os.system('clear') 
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|   ALTERAR STATUS DE FILMES E SÉRIES NA LISTA DE DESEJOS   |')
            print('|___________________________________________________________|')
            sleep(1)

            with open('wishlist.json') as arquivo:
                altera = json.load(arquivo)

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t   SUA LISTA DE DESEJOS                     |')
                print('|___________________________________________________________|')
                sleep(1)
                
                print('--' * 110)

                for item in altera:

                    print()
                    print(' Título: ', item['Titulo'].title())      
                    print(' Ano: ', item['Ano'])
                    print(' Tempo: ', item['Tempo'])
                    print(' Genero: ', item['Genero'])
                    print(' Diretor: ', item['Diretor'])
                    print(' Escritor: ', item['Escritor'])
                    print(' Atores: ', item['Atores'])
                    print(' País: ', item['Pais'])
                    print(' Status: ', item['Status'])
                    print(' Tipo: ', item['Tipo'].title())
                    print()
                    print('--' * 110)
                    sleep(1)

            print(' ________________________________________________________________')
            print('|                                                                |')
            print('| Digite o título que deseja alterar o status                    |')
            print('|________________________________________________________________|')
            print('|                                                                |')
            mudanca = input('| >>> ').lower().strip()
            print('|________________________________________________________________|')

            print(' ________________________________________________________________')
            print('|                                                                |')
            print('| Digite o ano do título escolhido                               |')
            print('|________________________________________________________________|')
            print('|                                                                |')
            ano = input('| >>> ').strip()
            print('|________________________________________________________________|')


            print(' ________________________________________________________________')
            print('|                                                                |')
            print('| 1-Filme                                                        |')
            print('| 2-Série                                                        |')
            print('|________________________________________________________________|')
            print('|                                                                |')
            tipo = input('| >>> ').strip()
            print('|________________________________________________________________|')

            flag = False

            for item in altera:

                if tipo == '1':
                    

                    if mudanca == item['Titulo'] and item['Tipo'] == 'movie' or ano == item['Ano']:

                        flag = True
                        break

                elif tipo == '2':

                    if mudanca == item['Titulo'] and item['Tipo'] == 'series' or ano == item['Ano']:

                        flag = True
                        break

                else:

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|\t\t       OPÇÃO INVÁLIDA                       |')
                    print('|___________________________________________________________|')
                    sleep(1)

                        
            if flag:

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t    Deseja marcar como...                   |')
                print('|                                                           |')
                print('| 1-Assistido                                               |')
                print('| 2-Assistir mais tarde                                     |')
                print('| 3-Continuar assisitindo                                   |')
                print('| 4-Não assistido                                           |')
                print('|___________________________________________________________|')
                print('|                                                           |')
                alterar = input('| >>> ').strip()
                print('|___________________________________________________________|')
                
                if alterar == '1':

                    item['Status'] = 'Assistido'

                    with open('wishlist.json', 'w') as arquivo:
                        json.dump(altera, arquivo, indent=4)

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t\t  MARCADO COMO "Assistido"                  |')
                        print('|___________________________________________________________|')
                    
                    sleep(1)
                        
                elif alterar == '2':

                    item['Status'] = 'Assistir mais tarde'

                    with open('wishlist.json', 'w') as arquivo:
                        json.dump(altera, arquivo, indent=4)

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t     MARCADO COMO "Assistir mais tarde"             |')
                        print('|___________________________________________________________|')
                    
                    sleep(1)
                        
                elif alterar == '3':

                    item['Status'] = 'Continuar assistindo'

                    with open('wishlist.json', 'w') as arquivo:
                        json.dump(altera, arquivo, indent=4)

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t      MARCADO COMO "Continuar assistindo"           |')
                        print('|___________________________________________________________|')

                    sleep(1)

                elif alterar == '4':
                    
                    item['Status'] = 'Nao assistido'

                    with open('wishlist.json', 'w') as arquivo:
                        json.dump(altera, arquivo, indent=4)

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|\t\tMARCADO COMO "Não assistido"                |')
                        print('|___________________________________________________________|')

                    sleep(1)
                        
                else:

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|\t\t      OPÇÃO INVÁLIDA                        |')
                    print('|___________________________________________________________|')

                sleep(1)
                    
            else:

                if tipo == '1':

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|       O FILME NÃO EXISTE NA SUA LISTA DE DESEJOS!         |')
                    print('|___________________________________________________________|')

                elif tipo == '2':

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|       A SÉRIE NÃO EXISTE NA SUA LISTA DE DESEJOS!         |')
                    print('|___________________________________________________________|')

                else:

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|\t\t      OPÇÃO INVÁLIDA                        |')
                    print('|___________________________________________________________|')

            sleep(2)               

        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('|     NÃO EXISTE NENHUM CONTEÚDO NA SUA LISTA DE DESEJOS!      |')
            print('|______________________________________________________________|')

            sleep(2)
                    

    def deletar_filme(self):

        try:

            os.system('clear') 
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|      REMOVER FILMES E SÉRIES DA SUA LISTA DE DESEJOS      |')
            print('|___________________________________________________________|')
            sleep(1)

            
            with open('wishlist.json') as arquivo:
                delete = json.load(arquivo)

                print(' ___________________________________________________________')
                print('|                                                           |')
                print('|\t\t   SUA LISTA DE DESEJOS                     |')
                print('|___________________________________________________________|')
                sleep(1)
            
            print()
            print('--' * 110)

            for item in delete:
                
                print()
                print(' Título: ', item['Titulo'].title())      
                print(' Ano: ', item['Ano'])
                print(' Tempo: ', item['Tempo'])
                print(' Genero: ', item['Genero'])
                print(' Diretor: ', item['Diretor'])
                print(' Escritor: ', item['Escritor'])
                print(' Atores: ', item['Atores'])
                print(' País: ', item['Pais'])
                print(' Status: ', item['Status'])
                print(' Tipo: ', item['Tipo'].title())
                print()
                print('--' * 110)
                sleep(1)

            print(' ___________________________________________________________________________')
            print('|                                                                           |')
            print('| Digite o título que deseja excluir da sua lista de desejos                |')    
            print('|___________________________________________________________________________|')
            print('|                                                                           |')
            excluir = input('| >>> ').lower().strip()
            print('|___________________________________________________________________________|')

            print(' ___________________________________________________________________________')
            print('|                                                                           |')
            print('| Digite o ano do título escolhido                                          |')    
            print('|___________________________________________________________________________|')
            print('|                                                                           |')
            ano = input('| >>> ').strip()
            print('|___________________________________________________________________________|')

            print(' ___________________________________________________________________________')
            print('|                                                                           |')
            print('| 1-Filme                                                                   |')
            print('| 2-Série                                                                   |')
            print('|___________________________________________________________________________|')
            print('|                                                                           |')
            tipo = input('| >>> ').strip()
            print('|___________________________________________________________________________|')

            flag = False
            lista = list()
                    
            for item in delete:

                if tipo == '1':

                    if excluir == item['Titulo'] and ano == item['Ano'] and item['Tipo'] == 'movie':

                        flag = True
                        break

                    else:
                        pass

                if tipo == '2':

                    if excluir == item['Titulo'] and ano == item['Ano'] and item['Tipo'] == 'series':

                        flag = True
                        break

                    else:
                        pass

            if flag:

                for item in delete:

                    if tipo == '1':

                        if excluir != item['Titulo']  or ano != item['Ano'] or item['Tipo'] == 'series':

                            lista.append(item)

                        else:
                            pass

                    if tipo == '2':

                        if excluir != item['Titulo']  or ano != item['Ano'] or item['Tipo'] == 'movie':

                            lista.append(item)

                        else:
                            pass

                
                with open('wishlist.json', 'w') as arquivo:
                    json.dump(lista, arquivo, indent=4)

                    if tipo == '1':

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|    FILME REMOVIDO DA SUA LISTA DE DESEJOS COM SUCESSO!    |')
                        print('|___________________________________________________________|')

                    elif tipo == '2':

                        print(' ___________________________________________________________')
                        print('|                                                           |')
                        print('|    SÉRIE REMOVIDA DA SUA LISTA DE DESEJOS COM SUCESSO!    |')
                        print('|___________________________________________________________|')

                    else:
                        pass

                sleep(2)
                os.system('clear') 
            
            else:

                if tipo == '1':

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|       O FILME NÃO EXISTE NA SUA LISTA DE DESEJOS!         |')
                    print('|___________________________________________________________|')
                    sleep(2)
                    os.system('clear')

                elif tipo == '2':

                    print(' ___________________________________________________________')
                    print('|                                                           |')
                    print('|       A SÉRIE NÃO EXISTE NA SUA LISTA DE DESEJOS!         |')
                    print('|___________________________________________________________|')
                    sleep(2)
                    os.system('clear')

                else:
                    pass

                
        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('|     NÃO EXISTE NENHUM CONTEÚDO NA SUA LISTA DE DESEJOS!      |')
            print('|______________________________________________________________|')
            sleep(1)
            


    def sugestao_ultimo(self):

        lista = list()

        with open('sugestao.json') as arquivo:
            sugestao = json.load(arquivo)

        try:

            os.system('clear') 
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|    SUGESTÕES DE FILMES E SÉRIES PELO ÚLTIMO ADICIONADO    |')
            print('|___________________________________________________________|')
            sleep(1)

            with open('wishlist.json') as arquivo:
                desejo = json.load(arquivo)

                for conteudo in range(-1, len(desejo)):

                    lista_desejos = desejo[conteudo]['Genero']
                    lista_desejos = lista_desejos.split()

                    for item in sugestao:

                        repositorio = item['Genero']
                        repositorio = repositorio.split()

                        if lista_desejos[0] == repositorio[0]:

                            dicionario = {
                            'Titulo': item['Titulo'].lower(),
                            'Ano': item['Ano'],
                            'Tempo': item['Tempo'],
                            'Genero': item['Genero'],
                            'Diretor': item['Diretor'],
                            'Escritor': item['Escritor'],
                            'Atores': item['Atores'],
                            'Pais': item['Pais'],
                            'Tipo': item['Tipo'],
                            }

                            lista.append(dicionario)

                        else:
                            pass

                    break

                for item in lista:
                    
                    print('--' * 110)
                    print()
                    print('Titulo: ', item['Titulo'].title())
                    print('Ano: ', item['Ano'])
                    print('Tempo: ', item['Tempo'])
                    print('Genero: ', item['Genero'])
                    print('Diretor: ',  item['Diretor'])
                    print('Escritor: ', item['Escritor'])
                    print('Atores: ', item['Atores'])
                    print('Pais: ', item['Pais'])
                    print('Tipo: ', item['Tipo'])
                    print()
                    print('--' * 110)
                    sleep(1)

            print('--' * 110)
            print()
        
            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t     FIM DAS SUGESTÕES                      |')
            print('|___________________________________________________________|')

            return


                # print(' Titulo: ', desejo[tamanho]['Titulo'])
                # print(' Ano: ', desejo[tamanho]['Ano'])
                # print(' Tempo: ', desejo[tamanho]['Tempo'])
                # print(' Genero: ', desejo[tamanho]['Genero'])
                # print(' Diretor: ', desejo[tamanho]['Diretor'])
                # print(' Escritor: ', desejo[tamanho]['Escritor'])
                # print(' Atores: ', desejo[tamanho]['Atores'])
                # print(' País: ', desejo[tamanho]['Pais'])
                # print(' Status: ', desejo[tamanho]['Status'])
                # print(' Tipo: '), desejo[tamaho]['Tipo]
                # print('--' * 110)
                # sleep(1)
            

        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('|     NÃO EXISTE NENHUM CONTEÚDO NA SUA LISTA DE DESEJOS!      |')
            print('|______________________________________________________________|')
            sleep(2)


    def sugestao_historico(self):

        os.system('clear') 
        print(' ___________________________________________________________')
        print('|                                                           |')
        print('|        SUGESTÕES DE FILMES E SÉRIES PELO  HISTÓRICO       |')
        print('|___________________________________________________________|')
        sleep(1)

        print()

        with open('sugestao.json') as arquivo:
            sugestao = json.load(arquivo)

        try:

            lista = list()

            with open('wishlist.json') as arquivo:
                desejo = json.load(arquivo)


            for item in desejo:

                lista_desejos = item['Genero']
                lista_desejos = lista_desejos.split()

                for conteudo in sugestao:

                    repositorio = conteudo['Genero']
                    repositorio = repositorio.split()

                    if lista_desejos[0] == repositorio[0]:

                        dicionario = {
                            'Titulo': conteudo['Titulo'].lower(),
                            'Ano': conteudo['Ano'],
                            'Tempo': conteudo['Tempo'],
                            'Genero': conteudo['Genero'],
                            'Diretor': conteudo['Diretor'],
                            'Escritor': conteudo['Escritor'],
                            'Atores': conteudo['Atores'],
                            'Pais': conteudo['Pais'],
                            'Tipo': conteudo['Tipo'],
                        }

                        lista.append(dicionario)

                    if lista_desejos[0] == 'Comedy' and repositorio[0] == 'Comdedy' and lista_desejos[0] == repositorio[0]:


                        dicionario = {
                            'Titulo': conteudo['Titulo'].lower(),
                            'Ano': conteudo['Ano'],
                            'Tempo': conteudo['Tempo'],
                            'Genero': conteudo['Genero'],
                            'Diretor': conteudo['Diretor'],
                            'Escritor': conteudo['Escritor'],
                            'Atores': conteudo['Atores'],
                            'Pais': conteudo['Pais'],
                            'Tipo': conteudo['Tipo'],
                        }

                        lista.append(dicionario)


                    else:
                        pass

            for item in lista:

                print('--' * 110)
                print()
                print('Titulo: ', item['Titulo'].title())
                print('Ano: ', item['Ano'])
                print('Tempo: ', item['Tempo'])
                print('Genero: ', item['Genero'])
                print('Diretor: ',  item['Diretor'])
                print('Escritor: ', item['Escritor'])
                print('Atores: ', item['Atores'])
                print('Pais: ', item['Pais'])
                print('Tipo: ', item['Tipo'])
                print()
                print('--' * 110)
                sleep(1)

            print('--' * 110)
            print()

            print(' ___________________________________________________________')
            print('|                                                           |')
            print('|\t\t     FIM DAS SUGESTÕES                      |')
            print('|___________________________________________________________|')

            return

        except FileNotFoundError:

            print(' ______________________________________________________________')
            print('|                                                              |')
            print('|     NÃO EXISTE NENHUM CONTEÚDO NA SUA LISTA DE DESEJOS!      |')
            print('|______________________________________________________________|')
            sleep(1)

    #print(response['Ratings'][2]['Value'])
