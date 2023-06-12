import time
import random
import math

def copy(L):
    k=[]
    for i in range(len(L)):
        k.append([])
        for j in range(len(L[i])):
            k[i].append([])
            k[i][j]=L[i][j]
    return k
def makedescendants(L,X):
    '''fazer os filhos dum estado "L" na vez do jogador "X"'''
    K=[]
    for i in range(1,8):
        Play=jogada(L,i,X)
        if Play != L:
            K.append([0,Play])
    if K==[]:
        A=check(L,'O')[0]
        if A=='O':
            return [L[0]+512,L[1]]
        elif A=='X':
            return [L[0]-512,L[1]]
        else:
            return [[0,L]]
    else:
        return K


def makedescendants_montecarlo(L,X):
    '''fazer os filhos dum estado "L" na vez do jogador "X"'''
    K=[]
    for i in range(1,8):
        Play = jogada(L,i,X)
        if Play != L:
            K.append(Play)
    return K

def makedescendants_alpha_beta(L,X,i):
#tem que retornar a jogada se ela existir e null se nao para testar no codigo do alphabeta  
    Play=jogada(L,i,X)    
    if Play != L:
        return Play
    else:
        return "null"
def jogada(A,X,Y):
    '''colocar uma peca na coluna "X" num estado "L" do jogador "Y" '''
    L = copy(A)
    for i in range(len(L)):
        if L[-1-i][int(X)-1] == '-':
            L[-1-i][int(X)-1] = Y
            break
    return L
def find(A,B):
    '''find the element A in B (B is a list of lists and A is in the second argument of the lists inside B)'''
    for i in range(len(B)):
        if A==B[i][1]:
            return [i,B[i]]
    return False
def check(L,Y):
    '''testa e retorna o valor dum certo estado para o jogador "Y" '''
    heuristic_value = 0
    if Y == 'X':
        K='O'
    else:
        K='X'
    for i in range(len(L)):
        for j in range(4):
            H=L[-1-i][j]+L[-1-i][j+1]+L[-1-i][j+2]+L[-1-i][j+3]
            if (3*Y in H and not(K in H)):
                heuristic_value += 50
            elif (2*Y in H and not(K in H)):
                heuristic_value += 10
            elif (Y in H and not(K in H)):
                heuristic_value += 1
            if (3*K in H and not(Y in H)):
                heuristic_value += -50
            elif (2*K in H and not(Y in H)):
                heuristic_value += -10
            elif (K in H and not(Y in H)):
                heuristic_value += -1
            if H=='OOOO' or H=='XXXX':
                if Y in H:
                    heuristic_value = 512
                else:
                    heuristic_value = -512
                return [H[0],heuristic_value]
    for i in range(7):
        for j in range(3):
            V=L[j][i]+L[j+1][i]+L[j+2][i]+L[j+3][i]
            if (3*K in V and not(Y in V)):
                heuristic_value += -50
            elif (2*K in V and not(Y in V)):
                heuristic_value += -10
            elif (K in V and not(Y in V)):
                heuristic_value += -1
            if (3*Y in V and not(K in V)):
                heuristic_value += 50
            elif (2*Y in V and not(K in V)):
                heuristic_value += 10
            elif (Y in V and not(K in V)):
                heuristic_value += 1
            if V=='OOOO' or V=='XXXX':
                if Y in V:
                    heuristic_value = 512
                else:
                    heuristic_value = -512
                return [V[0],heuristic_value]
    for i in range(3):
        for j in range(4):
            D1=L[i][j]+L[i+1][j+1]+L[i+2][j+2]+L[i+3][j+3]
            D2=L[i][-1-j]+L[i+1][-2-j]+L[i+2][-3-j]+L[i+3][-4-j]
            if (3*K in D1 and not(Y in D1)):
                heuristic_value += -50
            elif (2*K in D1 and not(Y in D1)):
                heuristic_value += -10
            elif (K in D1 and not(Y in D1)):
                heuristic_value += -1
            if (3*Y in D1 and not(K in D1)):
                heuristic_value += 50
            elif (2*Y in D1 and not(K in D1)):
                heuristic_value += 10
            elif (Y in D1 and not(K in D1)):
                heuristic_value += 1
            if (3*K in D2 and not(Y in D2)):
                heuristic_value += -50
            elif (2*K in D2 and not(Y in D2)):
                heuristic_value += -10
            elif (K in D2 and not(Y in D2)):
                heuristic_value += -1
            if (3*Y in D2 and not(K in D2)):
                heuristic_value += 50
            elif (2*Y in D2 and not(K in D2)):
                heuristic_value += 10
            elif (Y in D2 and not(K in D2)):
                heuristic_value += 1
            elif D1=='OOOO' or D1=='XXXX':
                if Y in D1:
                    heuristic_value = 512
                else:
                    heuristic_value = -512
                return [D1[0],heuristic_value]
            if D2=='OOOO' or D2=='XXXX':
                if Y in D2:
                    heuristic_value = 512
                else:
                    heuristic_value = -512
                return [D2[0],heuristic_value]
    return [[],heuristic_value]

def jogo(depth):
    import time
    L=[['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-']]
    #jogadas = [1,3,7,1,5,1,1] #depth = 1
    #jogadas = [4,2,7,3,1,4,3,3,4,4,1,1,2,7,7,5,6,5] #depth = 2
    #jogadas = [4,5,2,2,2,1,1,3] #depth = 3
    #jogadas = [4,3,3,1,4,2,2,5,6,1,1,5,2] #depth = 4
    #jogadas = [4,5,2,6,4,5,7,2,2,1,1,1,2,5,6,6] #depth = 5
    First = input('Do you wish to play first?\nEnter "Y" for yes, "N" for no. ')
    jogada_n = 0
    if First == 'N' or First == 'n':
        start = time.time()
        L = minimax_3(L,'O',depth,0)[1]
        print('Execution Time: ',time.time()-start)
    while True:
        print(''.join(L[0]))
        print(''.join(L[1]))
        print(''.join(L[2]))
        print(''.join(L[3]))
        print(''.join(L[4]))
        print(''.join(L[5]),'\n')
        if check(L,'O')[0]!=[]:
            return check(L,'O')[0],'Wins'
        if not('-' in L[0]):
            return 'This game was a draw'
        print("It is now X's turn.\nMake a move by choosing the collumn on which you'd like to play.")
        #X = jogadas[jogada_n]
        #jogada_n+=1
        X = input('Column: ')
        if X == 'stop' or X== 'Stop':
            return 'The game has finished by your command.'
        elif int(X) < 1 or int(X) > 7:
            input('The value you inserted is not valid.\nPress ENTER to try again.')
        else:
            k = jogada(L,X,'X')
            if k == L:
                if ('-' in L[0]):
                    input('There is no space left in that column.\nPress ENTER to try again.')
                else:
                    return 'This game was a draw'
            else:
                L = k
                print(''.join(L[0]))
                print(''.join(L[1]))
                print(''.join(L[2]))
                print(''.join(L[3]))
                print(''.join(L[4]))
                print(''.join(L[5]),'\n')
                if check(L,'X')[0]!=[]:
                    return check(L,'X')[0],'Wins'
                print('Calculating play...\n')
                start = time.time()
                L = minimax_3(L,'O',depth,0)[1]
                print('Execution Time: ',time.time()-start)
#Definicoes para o Minimax

#Definicoes auxiliares para o minimax
def maximo(L):
    j=L[0][0]
    #print("j = ", j)
    jogada = L[0][1]
    for i in range(len(L)):
        if int(L[i][0])>j:
            j=L[i][0]
            jogada=L[i][1]
    return [j,jogada]
def minimo(L):
    j=L[0][0]
    jogada = L[0][1]
    for i in range(len(L)):
        if int(L[i][0])<j:
            j=L[i][0]
            jogada=L[i][1]
    return [j,jogada]

def minimax(L,X,max_depth,depth):
    '''jogada que se deve fazer, usando minimax, para o jogador "X" com o estado "L" '''
    count = 0
    queue=copy(L)
    if depth>=max_depth:
        while count<len(L):
            L[count][0] = check(L[count][1],'O')[1]
            count+=1
        if X == 'O':
            return maximo(L)
        return minimo(L)
    if X=='X':
        Y='O'
    elif X=='O':
        Y='X'
    while queue!=[]:
        node = queue[0][1]
        queue = queue[1:]
        win = check(node,'O')[0]
        if win!=[]:
            if win=='O':
                return [512,node]
            return [-512,node]
        heuristic_value = minimax(makedescendants(node,Y),Y,max_depth,depth+1)[0]
        L[count][0] = heuristic_value
        count+=1
    if X == 'O':
        return maximo(L)
    return minimo(L)

def minimax_2(state,X,max_depth,depth):
    check_result = check(state,'O')
    best = []
    if check_result[1] == 512 or check_result[1] == -512 or depth >= max_depth:
        return[check_result[1],state]
    if X=='X':
        v = float('inf')
        Y = 'O'
    elif X=='O':
        v = -float('inf')
        Y = 'X'
    queue = copy(makedescendants(state,X))
    while queue != []:
        d = queue[0][1]
        queue = queue[1:]
        if d != []:
            if X == 'O':
                v1 = minimax_2(d,Y,max_depth,depth + 1)[0]
                if v1 > v:
                    v = v1
                    best = d
            else:
                v1 = minimax_2(d,Y,max_depth,depth + 1)[0]
                if v1 < v:
                    v = v1
                    best = d
    if best == []:
        return [0,state]
    else:
        return [v,best]

def minimax_3(L,X,max_depth,depth):
    '''jogada que se deve fazer, usando minimax, para o jogador "X" com o estado "L" '''
    check_result = check(L,'O')
    if check_result[1] == 512 or check_result[1] == -512 or depth >= max_depth:
        return[check_result[1],L]
    descendants = makedescendants(L,X)
    queue = copy(descendants)
    count = 0
    if X=='X':
        Y='O'
    elif X=='O':
        Y='X'
    while queue!=[]:
        node = queue[0][1]
        queue = queue[1:]
        if not('-' in node[0]):
            return [0,node]
        heuristic_value = minimax_3(node,Y,max_depth,depth+1)[0]
        descendants[count][0] = heuristic_value
        count+=1
    if X == 'O':
        return maximo(descendants)
    return minimo(descendants)


#Definicoes para o Alpha Beta
def jogo_alpha_beta(max_depth):
#    import time
    L=[['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-']]
    #jogadas = [1,3,7,1,5,1,1] #depth = 1
    #jogadas = [4,2,7,3,1,4,3,3,4,4,1,1,2,7,7,5,6,5] #depth = 2
    #jogadas = [4,5,2,2,2,1,1,3] #depth = 3
    #jogadas = [4,3,3,1,4,2,2,5,6,1,1,5,2] #depth = 4
    #jogadas = [4,5,2,6,4,5,7,2,2,1,1,1,2,5,6,6] #depth = 5
    First = input('Do you wish to play first?\nEnter "Y" for yes, "N" for no. ')
    jogada_n = 0
    if First == 'N' or First == 'n':
        alpha = -float('inf')
        beta = float('inf')
        start = time.time()
        L = alphabeta(L,'O',alpha,beta,0,max_depth)[1]
        print('Execution Time: ',time.time()-start)
    while True:
        print(''.join(L[0]))
        print(''.join(L[1]))
        print(''.join(L[2]))
        print(''.join(L[3]))
        print(''.join(L[4]))
        print(''.join(L[5]),'\n')
        if check(L,'O')[0]!=[]:
            return check(L,'O')[0],'Wins'
        if not('-' in L[0]):
            return 'This game was a draw'
        print("It is now X's turn.\nMake a move by choosing the collumn on which you'd like to play.")
        X = input('Column: ')
        #X = jogadas[jogada_n]
        #jogada_n+=1
        if X == 'stop' or X== 'Stop':
            return 'The game has finished by your command.'
        elif int(X) < 1 or int(X) > 7:
            input('The value you inserted is not valid.\nPress ENTER to try again.')
        else:
            k = jogada(L,X,'X')
            if k == L:
                if ('-' in L[0]):
                    input('There is no space left in that column.\nPress ENTER to try again.')
                else:
                    return 'This game was a draw'
            else:
                L = k
                print(''.join(L[0]))
                print(''.join(L[1]))
                print(''.join(L[2]))
                print(''.join(L[3]))
                print(''.join(L[4]))
                print(''.join(L[5]),'\n')
                if check(L,'X')[0]!=[]:
                    return check(L,'X')[0],'Wins'
                print('Calculating play...\n')
                alpha = -float('inf')
                beta = float('inf')
                start = time.time()
                L = alphabeta(L,'O',alpha,beta,0,max_depth)[1]
                print('Execution Time: ',time.time()-start)

def alphabeta(state,X,alpha,beta,depth,max_depth):
    check_result = check(state,'O')
    best = []
    if check_result[1] == 512 or check_result[1] == -512 or depth == max_depth:
        return[check_result[1],state]
    if X=='X':
        v = float('inf')
        Y = 'O'
    elif X=='O':
        v = -float('inf')
        Y = 'X'
    for i in range(0,7):
        d = makedescendants_alpha_beta(state,X,i)
        if d != "null":
            if X == 'O':
                v1 = alphabeta(d,Y,alpha,beta,depth + 1,max_depth)[0]
                if v1 > v:
                    v = v1
                    best = d
#                print("type_beta = ", type(beta))
#                print("beta =", beta)
                if v >= beta:
                    return [v,best]
                alpha = max(alpha,v)
            else:
#                print("type_v = ", type(v))
#                print("v = ", v)
#                print("type_alpha = ", type(alpha))
#                print("alpha =", alpha)
                v1 = alphabeta(d,Y,alpha,beta,depth + 1,max_depth)[0]
                if v1<v:
                    v = v1
                    best = d
#                print("type_v = ", type(v))
#                print("type_alpha = ", type(alpha))
                if v <= alpha:
                    return [v,best]
                beta = min(beta,v)
    if best == []:
        return [0,state]
    else:
        return [v,best]


def jogo_monte():
#    import time
    L=[['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-']]
    #jogadas = [1,3,7,1,5,1,1] #depth = 1
    #jogadas = [4,2,7,3,1,4,3,3,4,4,1,1,2,7,7,5,6,5] #depth = 2
    #jogadas = [4,5,2,2,2,1,1,3] #depth = 3
    #jogadas = [4,3,3,1,4,2,2,5,6,1,1,5,2] #depth = 4
    #jogadas = [4,5,2,6,4,5,7,2,2,1,1,1,2,5,6,6] #depth = 5
    jogadas_n = 0
    First = input('Do you wish to play first?\nEnter "Y" for yes, "N" for no. ')
    if First == 'N' or First == 'n':
        start = time.time()
        L = monte_carlo(L,'O')
        print('Execution Time: ',time.time()-start,'\nNodes visited: ',L[1])
        L = L[0]
    while True:
        print(''.join(L[0]))
        print(''.join(L[1]))
        print(''.join(L[2]))
        print(''.join(L[3]))
        print(''.join(L[4]))
        print(''.join(L[5]),'\n')
        if check(L,'O')[0]!=[]:
            return check(L,'O')[0],'Wins'
        print("It is now X's turn.\nMake a move by choosing the collumn on which you'd like to play.")
        #X = jogadas[jogadas_n]
        #jogadas_n+=1
        X = input('Column: ')
        if X == 'stop' or X== 'Stop':
            return 'The game has finished by your command.'
        elif int(X) < 1 or int(X) > 7:
            input('The value you inserted is not valid.\nPress ENTER to try again.')
        else:
            k = jogada(L,X,'X')
            if k == L:
                if ('-' in L[0]):
                    input('There is no space left in that column.\nPress ENTER to try again.')
                else:
                    return 'This game was a draw'
            else:
                L = k
                print(''.join(L[0]))
                print(''.join(L[1]))
                print(''.join(L[2]))
                print(''.join(L[3]))
                print(''.join(L[4]))
                print(''.join(L[5]),'\n')
                if check(L,'X')[0]!=[]:
                    return check(L,'X')[0],'Wins'
                print('Calculating play...\n')
                start = time.time()
                L = monte_carlo(L,'O')
                print('Execution Time: ',time.time()-start,'\nNodes visited: ',L[1])
                L = L[0]

def rollOut(node,X):
    '''rollout do no "node" sendo a vez do jogador "X"'''
    if X=='X':
        X == ['X','X']
        Y='O'
    else:
        Y='X'
    state_check = check(node,'O')
    while state_check[0]==[]:
        if state_check[1]==0:
            break
        coluna = random.randint(1,7)
        node = jogada(node,coluna,X)
        (X,Y) = (Y,X)
        state_check = check(node,'O')
    if state_check[0] == 'O':
        return 1
    return 0

def select(nodes,visited,n,C):
    if nodes == []:
        return []
    selecao = []
    for i in visited:
        if i in nodes:
            selecao.append([ucb(visited[i][1],visited[i][2],n,C),i])
            nodes.remove(visited[i][1])
    for i in nodes:
        selecao.append([0,i])
    return escolha_probabilistica(selecao)

def escolha_probabilistica(L):
    soma_ucb = 0
    comzero = []
    semzero = []
    for i in L:
        soma_ucb += i[0]
        if i[0] == 0:
            comzero.append(i[1])
        else:
            semzero.append(i)
    aleatorio = random.randint(1,2)                 #Escolher com 50% de chance expandir um vertice novo ou selecionar usando os valores de UCB
    if (aleatorio == 1 or soma_ucb == 0) and len(comzero)!=0 :
        escolha = random.choice(comzero)
        return escolha
    prob = random.random()*soma_ucb
    count = 0
    for i in range(len(semzero)):
        count += semzero[i][0]
        if count >= prob:
            return semzero[i][1]

def ucb(wi,ni,n,C):
    '''n->numero vezes pai foi visitado,ni->numero de vezes que foi escolhido'''
    return (wi/n)+C*math.sqrt(2*math.log(n)/ni)

def list2str(L):
    A = str(L)
    return A

def monte_carlo(L,X):
    C = math.sqrt(2) #Valor da constante C em UCB
    start = time.time()
    if X=='O':
        X1 = 'O'
        Y1 = 'X'
        Y='X'
    else:
        X1 = 'X'
        Y1 = 'O'
        Y='O'
    A = list2str(L)
    visited = {A:[1,0,0]} # Se o primeiro valor da lista for 1, entao e uma folha, se for 0 e um no visitado, mas nao uma folha|| os dois ultimos elementos da lista sao, Wi e ni, respetivamente
    countt=0
    for i in range(1000):
        countt+=1
        (X,Y) = (X1,Y1)
        node = copy(L)
        visited_temp = []
        node_str = list2str(node)
        while visited.get(node_str,[1,0,0])[0] == 0:
            visited_temp.append(node_str)
            visited[node_str]=[visited[node_str][0],visited[node_str][1],visited[node_str][2]+1]
            node = select(makedescendants_montecarlo(node,X),visited,visited[node_str][1],C)
            (X,Y) = (Y,X)
            node_str = list2str(node)
        visited[node_str] = visited.get(node_str,[1,0,1])
        count = 0
        while True:
            count+=1
            if count>100:
                break
            aleatorio = random.randint(1,7)
            filho = jogada(node,aleatorio,X)
            filho_str = list2str(filho)
            if visited.get(filho_str,[0,0,0])[0] == 0:
                value = rollOut(filho,Y)
                visited[filho_str] = [1,value,1]
                visited[node_str] = [0,visited[node_str][1]+value,visited[node_str][2]]
                for i in visited_temp:
                    visited[i]=[visited[i][0],visited[i][1]+value,visited[i][2]]
                break
    k = 0
    jogo = makedescendants_montecarlo(L,X1)
    temp = jogo[0]
    for i in jogo:
        j = list2str(i)
        #print(visited[j],time.time()-start)
        if not(visited[j][2] == 0):
            UCB = visited[j][1]/visited[j][2]
            if UCB > k:
                k = UCB
                temp = i
    return [temp,len(visited)]






