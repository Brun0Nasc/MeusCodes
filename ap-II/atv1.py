while True:
    m = [] 
    n = int(input()) 

    if n == 0: 
        break

    for i in range(n): 
        l = [] 
        for c in range(n):
            l.append(1) 
        m.append(l)
    
    
    if n % 2 == 0: 
        meio = n/2 
    else: 
        meio = (n+1)/2 
    
    
    valor = 1 # Aqui é o valor que sempre será adicionado
    cima = 0 # Aqui representa a primeira linha (0)
    esq = 0 # Aqui representa a primeira coluna (0)
    direita = n-1 # Aqui representa a última coluna, que tem índice n-1
    baixo = n-1 # Aqui representa a última linha de índice n-1

# Esse laço enquanto vai rodar até a variável 'valor', que começa em 1, se igualar à variável 'meio'
    while valor <= meio:
        i = esq # Variável que recebe o valor presente navariável esquerda, e serve como contador separado
        while i <= direita: # Esse laço preenche uma linha de baixo e uma de cima equivalentes em posição
            m[cima][i] = valor # i representa a coluna que será preenchida
            m[baixo][i] = valor 
            i += 1 # i vai receber mais uma unidade sempre que preencher a coluna das duas linhas.
                    # Assim, i será usado para preencher a coluna posterior, até adquirir o valor
                    # igual ao valor 'direita', que é a última coluna a ser preenchida
        
        i = (cima + 1) # Após o preenchimento de colunas das linhas terminar, i vai agir como indicador de linha
        while i < baixo: # enquanto i(linha) for menor que baixo(última linha considerada de acordo com seu valor)
            m[i][esq] = valor # a matriz na linha i e coluna à esquerda será preenchida com a variável 'valor'
            m[i][direita] = valor # o mesmo ocorre com os valores à direita
            i += 1 # i receberá mais uma unidade para preencher a linha posterior
        
        # aqui as variáveis que receberem +1, exceto 'valor', serão utilizadas para avançar para a 
        valor += 1
        cima += 1 
        baixo -= 1 
        esq += 1 
        direita -= 1 
        
    
    
    for i in range(n):
        tx = ''
        for j in range(n):
            tx += " %3d" %m[i][j]
        print(tx[1:])
    print("")
