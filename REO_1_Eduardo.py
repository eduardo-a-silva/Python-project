print("---------------------------------------------------------------------------------------------------------------")
print("Exercicio N°1")
print("Declare os valores 43.5,150.30,17,28,35,79,20,99.07,15 como um array numpy.")
print("Letra A)")
import numpy as np
vetor= np.array([43.5,150.30,17,28,35,79,20,99.07,15])
print("O vetor =", vetor)
print("")
print("------------------------------------")
print("")
print("Letra B)")
print("Obtenha as informações de dimensão, média, máximo, mínimo e variância deste vetor.")
dim_01=len(vetor)
print("A dimesão do vetor é ", str(dim_01))
print("O máximo valor é: ", np.max(vetor))
print("O menor valor no vetor é:", np.min(vetor))
print("A média é:", np.mean(vetor))
print("A variância é:", np.var(vetor))
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra C)")
print("Obtenha um novo vetor em que cada elemento é dado pelo quadrado da diferença entre cada elemento do vetor declarado na letra a e o valor da média deste.")
vetor_np= (vetor - np.mean(vetor))**2
print("Novo vetor= ", vetor_np)
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra D)")
print("Obtenha um novo vetor que contenha todos os valores superiores a 30.")
bool_vetor= vetor>30
menor_vetor=vetor[bool_vetor]
print("Novo vetor com os valores acima de 30 =" , menor_vetor)
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra E)")
print("Identifique quais as posições do vetor original possuem valores superiores a 30")
posi_vetor = np.where(vetor>30)
print("As posições com valores mairoes que 30 são:", posi_vetor[0])
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra F)")
print("Apresente um vetor que contenha os valores da primeira, quinta e última posição.")
vetor_1=(vetor[0])
vetor_5=vetor[4]
vetor_last=vetor[-1]
new_vetor=vetor_1, vetor_5, vetor_last
print("O novo vetor com os valore da posição 1°, 5° e 9°=", new_vetor)
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra G)")
print("Crie uma estrutura de repetição usando o for para apresentar cada valor e a sua respectiva posição durante as iterações")
import time
it=0
for i in range(0,len(vetor),1):
    it = it + 1
    print('Iteração: ' + str(it))
    print('Na posição ' + str(i) + ' há o elemento: ' + str(vetor[int(i)]))
    time.sleep(0.5)

print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra H)")
print("Crie uma estrutura de repetição usando o for para fazer a soma dos quadrados de cada valor do vetor.")
it=0
SQ=0
for i in range(0,len(vetor),1):
    it = it + 1
    SQ=SQ+ vetor[int(i)] ** 2
    print('Iteração: ' + str(it))
    print('Na posição ' + str(i) + ' há o valor: ' + str(vetor[int(i)]))
    time.sleep(0.5)

print("     ")
print("A soma de quadrado dos valores é: ", SQ)

print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra I)")
print("Crie uma estrutura de repetição usando o while para apresentar todos os valores do vetor")
print("R: Abaixo são apresentados todos os valores do vetor: ")
pos = 0
while vetor[pos]!=100:
    print(vetor[pos])
    pos = pos+1
    time.sleep(0.5)
    if pos==(len(vetor)):
        print('Posição igual a: ' + str(pos)+ ' - A condição estabelecida retornou true, vamos sair do while')
        break

print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra J)")
print("Crie um sequência de valores com mesmo tamanho do vetor original e que inicie em 1 e o passo seja também 1.")
n_seq = np.array(np.arange(1,len(vetor)+1,1))

print("Novo vetor:", n_seq)

print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra K)")
print("Concatene o vetor da letra a com o vetor da letra j.")
conc = np.concatenate ((vetor,n_seq), axis=0)
print("Novo vetor concaternado = ", conc)

print("===============================================================================================================")
print("Segundo roteiro")
print("EXERCÍCIO NUMERO 2")
print("Letra A)")
print("Declare a matriz abaixo com a biblioteca numpy."
      "1 3 22"
      "2 8 18"
      "3 4 22"
      "4 1 23"
      "5 2 52"
      "6 2 18"
      "7 2 25")
import numpy as np
matriz_01 = np.array([[1,3,22],
                [2,8,18],
                [3,4,22],
                [4,1,23],
                [5,2,52],
                [6,2,18],
                [7,2,25]])
print(matriz_01)
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra B)")
print("Obtenha o número de linhas e de colunas desta matriz")
nl,nc=np.shape(matriz_01)
print("Número de linhas =", nl)
print("Número de colunas =", nc)
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra C)")
print("Obtenha as médias das colunas 2 e 3.")
med1_2=np.mean(matriz_01[0:,1])
med1_3=np.mean(matriz_01[0:,2])
print("A média da coluna 2 é: ", med1_2)
print("A média da coluna 3 é: ", med1_3)
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra D)")
print("Obtenha as médias das linhas considerando somente as colunas 2 e 3")
l1=np.mean(matriz_01[0,1:3])
l2=np.mean(matriz_01[1,1:3])
l3=np.mean(matriz_01[2,1:3])
l4=np.mean(matriz_01[3,1:3])
l5=np.mean(matriz_01[4,1:3])
l6=np.mean(matriz_01[5,1:3])
l7=np.mean(matriz_01[6,1:3])
print("Linha   Média")
print("  1     ", l1)
print("  2     ", l2)
print("  3     ", l3)
print("  4     ", l4)
print("  5     ", l5)
print("  6     ", l6)
print("  7     ", l7)
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra E)")
print("Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e"
      "e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade inferior a 5.")
menor_sev=matriz_01[:,1]<5
position = np.where(menor_sev)
matriz_sev_bool=matriz_01[position]

print("Os genótipos com severidade de doença inferior que 5 foram:", matriz_sev_bool[0:,0])
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra F)")
print("Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e"
      "a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de peso de 100 grãos superior ou igual a 22.")
maior_igual_22 = matriz_01[0:,2]>=22
print(maior_igual_22)
big_position=np.where(maior_igual_22)
maior_bool=matriz_01[big_position]
print(maior_bool)
print("")
print("Os genótipos com maior nota de peso de 100 grãos foram:", maior_bool[0:,0])
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra G)")
print("Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e")
print("a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade igual ou inferior a 3 e peso de 100")
print("grãos igual ou superior a 22.")
nota_3=maior_bool[0:,1]<=3
matriz_new=np.where(nota_3)
matrix=maior_bool[matriz_new]
print(matrix)
print("")
print("Os genótipos com nota de peso de 100 grãos maior ou igual a 22 e severidade menor que 3 foram:", matrix[0:,0])
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra H)")
print("Crie uma estrutura de repetição com uso do for (loop) para apresentar na tela cada uma das posições da matriz e o seu")
print("respectivo valor. Utilize um iterador para mostrar ao usuário quantas vezes está sendo repetido.")
print("Apresente a seguinte mensagem a cada iteração {Na linha X e na coluna Y ocorre o valor: Z}")
print("Nesta estrutura crie uma lista que armazene os genótipos com peso de 100 grãos igual ou superior a 25")
import time
contador=0
matriz_quadrados = np.zeros((nl,nc))
for i in np.arange(0,nl,1):
    for j in np.arange(0,nc,1):
        contador += 1
        print('Iteração: '+ str(contador))
        print('Na linha ' + str(i) + ' e coluna ' + str(j) + ' há o elemento: ' + str(matriz_01[int(i),int(j)]))
        time.sleep(0.5)
        matriz_quadrados[int(i),int(j)] = (matriz_01[int(i),int(j)])**2
        print("")
        print('-----------------------------------------------------------------------------------------------------------------')
        print("")
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
print(matriz_01)
print("----------")
print(matriz_quadrados)
print("")

print("===============================================================================================================")
print("Terceiro roteiro")
print("EXERCÍCIO NUMERO 3")
print("Letra A)")
print("Crie uma função em um arquivo externo (outro arquivo .py) para calcular a média e a variância amostral um vetor qualquer, baseada em um loop (for).")
print('A função esta no arquivo FUNCTION_4')
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra B)")
print("Simule três arrays com a biblioteca numpy de 10, 100, e 1000 valores e com distribuição normal com média 100 e variância 2500. Pesquise na documentação do numpy por funções de simulação.")
print("Valores aleatórios de 10, 100, e 1000 amostras")
#np.set_printoptions(precision=2)
#np.set_printoptions(suppress=True)
import numpy as np
dados_10= np.random.normal(loc=100, scale=50, size=10)
print("Vetor de 10 amostras aleatórias com media 100 e variancia de 2500: ", dados_10)
print("")
print("------------------------------------------------------------------------------")
print("")
dados_100 = np.random.normal(loc=100, scale=50, size=100)
print("Vetor 100 amostras aleatórias com media 100 e variancia de 2500: ", dados_100)
print("")
print("------------------------------------------------------------------------------")
print("")
dados_1000 = np.random.normal(loc=100, scale=50, size=1000)
print("Vetor 1000 amostras aleatórias com media 100 e variancia de 2500: ", dados_1000)
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra C)")
print("Utilize a função criada na letra a para obter as médias e variâncias dos vetores simulados na letra b.")
from function_4 import media
from function_4 import variancia
print("Conjunto de dados com 10 amostras")
print("media ", media(dados_10))
print("variancia ", variancia(dados_10))
print("------------------------------------")
print("Conjunto de dados com 100 amostras")
print("media ", media(dados_100))
print("variancia ", variancia(dados_100))
print("------------------------------------")
print("Conjunto de dados com 1000 amostras")
print("media ", media(dados_1000))
print("variancia ", variancia(dados_1000))
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra D)")
print("Crie histogramas com a biblioteca matplotlib dos vetores simulados com valores de 10, 100, 1000 e 100000.")
dados_100000 = np.random.normal(loc=100, scale=50, size=100000)
#nl1,nc1=dados_10.shape
#nl2,nc2=dados_100.shape
#nl3,nc3=dados_1000.shape
#nl4,nc4=dados_100000.shape
#fig=plt.figure("Gráfico Histograma")
#plt.hist
import matplotlib.pyplot as plt
from matplotlib import colors
#from matplotlib.ticker import PercentFormatter

#histogra_exemplo = plt.hist(dados_1000, bins=15)#para plotar com uma unica cor(azul)
#plt.hist(dados_10, bins=15)
#plt.hist(dados_100, bins=15)
#plt.hist(dados_1000, bins=15)
#plt.hist(dados_100000, bins=15)
fig, axs = plt.subplots(1, tight_layout=True)
N, bins, patches = axs.hist(dados_10, bins=5)
fracs = N / N.max()

norm = colors.Normalize(fracs.min(), fracs.max())

for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)
plt.title('Histograma 10')
plt.xlabel('Número de elementos na classe')
plt.ylabel('Valor médio da classe')


fig, axs = plt.subplots(1, tight_layout=True)
N, bins, patches = axs.hist(dados_100, bins=10)
fracs = N / N.max()

norm = colors.Normalize(fracs.min(), fracs.max())

for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)
plt.title('Histograma 100')
plt.xlabel('Número de elementos na classe')
plt.ylabel('Valor médio da classe')


fig, axs = plt.subplots(1, tight_layout=True)
N, bins, patches = axs.hist(dados_1000, bins=15)
fracs = N / N.max()

norm = colors.Normalize(fracs.min(), fracs.max())

for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)
plt.title('Histograma 1000')
plt.xlabel('Número de elementos na classe')
plt.ylabel('Valor médio da classe')


fig, axs = plt.subplots(1, tight_layout=True)

N, bins, patches = axs.hist(dados_100000, bins=70)

fracs = N / N.max()

norm = colors.Normalize(fracs.min(), fracs.max())

# Now, we'll loop through our objects and set the color of each accordingly
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)
plt.title('Histograma 100000')
plt.xlabel('Número de elementos na classe')
plt.ylabel('Valor')
plt.show()

print("===============================================================================================================")
print("Terceiro roteiro")
print("EXERCÍCIO NUMERO 4")
print("Letra A)")
print("O arquivo dados.txt contem a avaliação de genótipos (primeira coluna) em repetições (segunda coluna) quanto a quatro"
      "variáveis (terceira coluna em diante). Portanto, carregue o arquivo dados.txt com a biblioteca numpy, apresente os dados e obtenha as informações"
      "de dimensão desta matriz.")
import numpy as np
dados_ex4 =np.loadtxt('dados.txt')

nl, nc = dados_ex4.shape
print(dados_ex4)
print("")
print("N° de linhas: ", nl)
print("N° de colunas: ", nc)
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra B)")
print("Pesquise sobre as funções np.unique e np.where da biblioteca numpy")
print("As funções:")
print("np.unique= é capaz de identificar (objetos) repetidos dentro do array")
print("np.where= é capaz de retornar uma condição de um vetor booleano")
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra C")
print("Obtenha de forma automática os genótipos e quantas repetições foram avaliadas")

print("O experimento foi feito com ", len(np.unique(dados_ex4[:,1])), " repetições")
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra D)")
print("Apresente uma matriz contendo somente as colunas 1, 2 e 4")


sub_dados=dados_ex4[:,[0,1,3]]
print(sub_dados)
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra E)")
print("Obtenha uma matriz que contenha o máximo, o mínimo, a média e a variância de cada genótipo para a variavel da coluna 4. Salve esta matriz em bloco de notas.")
nl2,nc2=np.shape(sub_dados)
print(nl2)
mat=np.zeros((10,4))
it=0
genotipo= np.reshape(np.unique(dados_ex4[:,0], axis=0),(10,1))
#print(genotipo)
for num in np.arange(0,nl2,3):
    mat[it, 0] = np.max(sub_dados[num:num + 3, 2], axis=0)
    mat[it, 1] = np.min(sub_dados[num:num + 3, 2], axis=0)
    mat[it, 2] = np.mean(sub_dados[num:num + 3, 2], axis=0)
    mat[it, 3] = np.var(sub_dados[num:num + 3, 2], axis=0)
    it += 1 #incrementa + 1 no it


#print(mat)
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
print('Genótipos     Max     Min      Média    Variância')
matriz_concat = np.concatenate((genotipo, mat),axis=1)
print (matriz_concat)

#import os
#help (np.savetxt)
np.savetxt("Matriz de dados.txt", matriz_concat, fmt='%2.2f', delimiter='\t')
#np.savetxt('matriz_ex3.txt', matriz_concat, delimiter=' ')
print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra F)")
print("Obtenha os genótipos que possuem média (médias das repetições) igual ou superior a 500 da matriz gerada na letra anterior.")
print("")
print("                     Matriz ")
print("___________________________________________________")
print(" Genótipos     Max      Min      Média   Variância")
print (matriz_concat)
print("___________________________________________________")
print("")
print("")
matriz_med_maior=matriz_concat[matriz_concat[:,3]>=500]
print("Os genotipos que possuem média maior ou igual que 500 são: ",matriz_med_maior[:,0])

print("")
print("------------------------------------------------------------------------------")
print("")
print("Letra G)")
print("Apresente os seguintes graficos:")
print("- Médias dos genótipos para cada variável. Utilizando o comando plt.subplot para mostrar mais de um grafico por figura")
print("___________________________________________________")
print("   GEN    REP    Var1   Var2   Var3   Var4   Var5")
print("___________________________________________________")
print(dados_ex4)
print("___________________________________________________")
print("")

nl3,nc3= dados_ex4.shape
mat_zeros=np.zeros((10,5))

it=0
GEN= np.reshape(np.unique(dados_ex4[:,0], axis=0),(10,1))


for num in np.arange(0,nl3,3):
    mat_zeros[it, 0] = np.mean(dados_ex4[num:num + 3, 2], axis=0)
    mat_zeros[it, 1] = np.mean(dados_ex4[num:num + 3, 3], axis=0)
    mat_zeros[it, 2] = np.mean(dados_ex4[num:num + 3, 4], axis=0)
    mat_zeros[it, 3] = np.mean(dados_ex4[num:num + 3, 5], axis=0)
    mat_zeros[it, 4] = np.mean(dados_ex4[num:num + 3, 6], axis=0)

    it += 1 #incrementa + 1 no it


mat_concat = np.concatenate((GEN, mat_zeros),axis=1)
print("")
print("           Valor da Média das Variáveis")
print("   GEN    REP    Var1   Var2   Var3   Var4   Var5")
print("___________________________________________________")
print(mat_concat)
print("___________________________________________________")

from matplotlib import pyplot as plt
import os
plt.style.use('ggplot')
fig = plt.figure('Média dos Genótipos para cada variável')
plt.subplot(2,3,1)
plt.bar(mat_concat[:,0], mat_concat[:,1], width=0.8, color="tab:green")
plt.title('Variável 1')
plt.ylabel('Valor médio')
plt.xlabel('Genótipo')

plt.subplot(2,3,2)
plt.bar(mat_concat[:,0], mat_concat[:,2], width=0.8, color="tab:red")
plt.title('Variável 2')
plt.ylabel('Valor médio')
plt.xlabel('Genótipo')

plt.subplot(2,3,3)
plt.bar(mat_concat[:,0], mat_concat[:,3], width=0.8, color="tab:blue")
plt.title('Variável 3')
plt.ylabel('Valor médio')
plt.xlabel('Genótipo')

plt.subplot(2,3,4)
plt.bar(mat_concat[:,0], mat_concat[:,4], width=0.8, color="tab:pink")
plt.title('Variável 4')
plt.ylabel('Valor  médio')
plt.xlabel('Genótipo')
plt.subplot(2,3,5)
plt.bar(mat_concat[:,0], mat_concat[:,5], width=0.8, color="tab:purple")
plt.title('Variável 5')
plt.ylabel('Valor  médio')
plt.xlabel('Genótipo')

print("Disperão 2D da médias dos genótipos (Utilizar as três primeiras variáveis). "
      "No eixo X uma variável e no eixo Y outra.")
cores = ['black','blue','red','green','yellow','pink','cyan','orange','darkviolet','slategray']
plt.style.use('ggplot')
plt.style.use('ggplot')
fig = plt.figure('Dispersão 2D das médias')
nl_4,nc_4=mat_concat.shape


plt.subplot(1,3,1)
cores = ['black','blue','red','green','yellow','pink','cyan','orange','darkviolet','slategray']
# https://matplotlib.org/3.1.0/gallery/color/named_colors.html
for i in np.arange(0,nl_4,1):
    plt.scatter(mat_concat[i,1], mat_concat[i,2], s=50, alpha=0.8, label = mat_concat[i,0], c = cores[i])

plt.title('Dispersão ')
plt.xlabel('Var 1')
plt.ylabel('Var 2')
plt.legend()
plt.subplot(1,3,2)
for i in np.arange(0,nl_4,1):
    plt.scatter(mat_concat[i,1], mat_concat[i,3], s=50, alpha=0.8, label = mat_concat[i,0], c = cores[i])

plt.title('Dispersão ')
plt.xlabel('Var 1')
plt.ylabel('Var 3')
plt.legend()
plt.subplot(1,3,3)
for i in np.arange(0,nl_4,1):
    plt.scatter(mat_concat[i,2], mat_concat[i,3], s=50, alpha=0.8, label = mat_concat[i,0], c = cores[i])

plt.title('Dispersão ')
plt.xlabel('Var 2')
plt.ylabel('Var 3')
plt.legend()
plt.show()

#Salvar grafico
#nome = 'dispersao2D'
#fig.savefig((nome+'.png'), bbox_inches="tight")
#os.startfile(nome+'.png')
