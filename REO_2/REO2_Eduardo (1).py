print("---------------------------------------------------------------------------------------------------------------")
print("Exercicio N°1")
print("Selecione uma imagem a ser utilizada no trabalho prático e realize os seguintes processos utilizando o pacote OPENCV do Python:")
print("Letra A)")
print("Apresente a imagem e as informações de número de linhas e colunas; número de canais e número total de pixels;")
#Importar os pacotes
import numpy as np
import cv2# Importa o pacote opencv
import numpy as np# Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
#'''
#Leitura e armazenamento da imagem pelo python
arquivo = "C_pepo.jpg" # Nome do arquivo a ser utilizado na análise
imagem = cv2.imread(arquivo,1)# Carrega imagem (1 - Colorida (BGR))
imagem = cv2.cvtColor(imagem,cv2.COLOR_BGR2RGB)#inverter as cores padrão para RGB

plt.figure("Questão 1 - Letra A)")

plt.imshow(imagem)
plt.title("Abobrinha (Curcubita pepo)")
plt.show()

nl,nc,canais = np.shape(imagem)
pixel = nl*nc
#total_pixel = np.ndarray(imagem(np.uint8))
print("O numero de Linhas da Imagem é:", nl)
print("O numero de Colunas da Imagem é:", nc)
print("O numero de Canais da Imagem é:", canais)
print("O numero de Pixels da Imagem é:", pixel)

print("Letra B)")
print("Faça um recorte da imagem para obter somente a área de interesse. Utilize esta imagem para a solução das próximas alternativas.")
#Recortar a imagem
imagem1 = cv2.imread("C_pepo.jpg")
imagem_recorte = imagem1[1215:3278,2704:3370]
cv2.imwrite("recorte.jpg", imagem_recorte)
imagem_recorte = cv2.cvtColor(imagem_recorte,cv2.COLOR_BGR2RGB)#RGB

plt.figure("Questão 1 - Letra B)")
plt.subplot(1,2,1)
plt.imshow(imagem)
plt.title("Imagem original")
plt.subplot(1,2,2)
plt.imshow(imagem_recorte)
plt.title("Recorte da área de interesse")
plt.show()


print("Letra C)")
print("Converta a imagem colorida para uma de escala de cinza (intensidade) e a apresente utilizando os mapas de cores “Escala de Cinza” e “JET”;")

arquivo_2 = "recorte.jpg"
img_recorte=cv2.imread(arquivo_2,1)
img_recorte_rgb=cv2.cvtColor(img_recorte,cv2.COLOR_BGR2RGB)
img_recorte_cinza = cv2.cvtColor(img_recorte, cv2.COLOR_BGR2GRAY)

plt.figure("Questão 1 - Letra C) Imagens em Escala de Cinza e JET")
plt.subplot(1,2,1)
plt.imshow(img_recorte_cinza, cmap = 'gray')
plt.title("Escala cinza")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y
plt.colorbar(orientation= "horizontal")
plt.subplot(1,2,2)
plt.imshow(img_recorte_cinza, cmap = 'jet')
plt.title("Escala JET")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y
plt.colorbar(orientation= "horizontal")

plt.show()

print("Letra D)")
print("Apresente a imagem em escala de cinza e o seu respectivo histograma; Relacione o histograma e a imagem.")

histograma = cv2.calcHist([img_recorte_cinza], [0], None, [256],[0,256])#o primeiro 0 é o numero de caniai
# NONE é uma mascara, ou seja uma região especifica
# [256] é o numero de pontpos que podem ser amortrados
#[0,256] é o intervalo que vamos trabalhar
#print(histograma)

plt.figure("Questão 1 - Letra D) Imagem em escala de cinza e seu respectivo histograma")


plt.subplot(1,2,1)
plt.imshow(img_recorte_cinza, cmap = 'gray')
plt.title("Imagem em tons de cinza")
plt.xticks([])# Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y
plt.colorbar(orientation= "horizontal")


plt.subplot(1,2,2)
plt.plot(histograma, color='black')
plt.title("Escala de Cinza")
plt.xlabel("Valores de Pixels")
plt.ylabel("Número de Pixels")
plt.show()

print("Letra E)")
print("Utilizando a imagem em escala de cinza (intensidade) realize a segmentação da imagem de modo a remover o fundo da imagem utilizando um limiar manual"
      " e o limiar obtido pela técnica de Otsu. "
      "Nesta questão apresente o histograma com marcação dos limiares utilizados, a imagem limiarizada (binarizada) e "
      "a imagem colorida final obtida da segmentação. Explique os resultados.")

arquivo_2 = "recorte.jpg"
img_recorte = cv2.imread(arquivo_2,1)
img_recorte_cinza = cv2.cvtColor(img_recorte, cv2.COLOR_BGR2GRAY)
histograma = cv2.calcHist([img_recorte_cinza], [0], None, [256],[0,256])#o primeiro 0 é o numero de caniai

# Técnica de limiarização - Thresholding
# Limiar manual
limiar_cinza = 168
(LM, img_limiar) = cv2.threshold(img_recorte_cinza,limiar_cinza,255,cv2.THRESH_BINARY)
(LMI, img_limiar_inv) = cv2.threshold(img_recorte_cinza,limiar_cinza,255,cv2.THRESH_BINARY_INV)

print('Limiar: ' + str(LM))
# Plotar figuras
plt.figure("Questão 1 - Letra E) Limiarização Manual- Thresholding")
plt.subplot(2,3,1)
plt.imshow(img_recorte_cinza,cmap='gray')
plt.title('Escala cinza')

plt.subplot(2,3,2)
plt.imshow(img_limiar,cmap='gray')
plt.title('Binário - L: ' + str(limiar_cinza))

plt.subplot(2,3,3)
plt.imshow(img_limiar_inv,cmap='gray')
plt.title('Binário Invertido: L: ' + str(limiar_cinza))
plt.colorbar(orientation="vertical")

plt.subplot(2,3,5)
plt.plot(histograma,color = 'black')
plt.axvline(x=limiar_cinza,color = 'g')
plt.title("Histograma")
plt.xlim([0,256])
plt.xlabel("Valores de Pixels")
plt.ylabel("Número de Pixels")

plt.show()


#Técnica de OTSU de limiarização
(L, img_limiar_otsu) = cv2.threshold(img_recorte_cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
(L1, img_limiar_otsu_inv) = cv2.threshold(img_recorte_cinza, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

plt.figure("Questão 1 - Letra E) Limiar - Otsu")
plt.subplot(1,4,1)
plt.title("Imagem em tons de cinza")
plt.imshow(img_recorte_cinza,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.colorbar(orientation= "horizontal")

plt.subplot(1,4,2)
plt.imshow(img_limiar_otsu,cmap='gray')
plt.title('OTSU Binária - L: ' + str(L))
plt.xticks([])
plt.yticks([])
plt.colorbar(orientation= "horizontal")

plt.subplot(1,4,3)
plt.imshow(img_limiar_otsu_inv,cmap='gray')
plt.title('OTSU Binária Invertida- L: ' + str(L1))
plt.xticks([])
plt.yticks([])
plt.colorbar(orientation= "horizontal")

plt.subplot(1,4,4)
plt.plot(histograma,color = 'black')
plt.axvline(x=L1,color = 'g')
plt.title("Histograma")
plt.xlim([0,256])
plt.xlabel("Valores de Pixels")
plt.ylabel("Número de Pixels")
plt.show()


# Obtendo imagem colorida segmentada
img_segmentada = cv2.bitwise_and(img_recorte_cinza,img_recorte_cinza,mask=img_limiar_inv)
img_segmentada1 = cv2.bitwise_and(img_recorte_cinza,img_recorte_cinza,mask=img_limiar_otsu_inv)

# Plotar figuras
plt.figure("Questão 1 - Letra E) Imagens Segmentadas")
plt.subplot(1,3,1)
plt.imshow(img_recorte_cinza,cmap='gray')
plt.title('Escala cinza')
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,2)
plt.imshow(img_segmentada)
plt.title('Segmentada - RGB - Limiar Manual')
plt.xticks([])
plt.yticks([])


plt.subplot(1,3,3)
plt.imshow(img_segmentada1)
plt.title('Segmentada - RGB - Limiar OTSU')
plt.xticks([])
plt.yticks([])


plt.show()
#Explique os resultados

print("Letra F)")
print("Apresente uma figura contento a imagem selecionada nos sistemas RGB, Lab, HSV e YC")
# Imagem RGB
img_rgb = cv2.cvtColor(img_recorte,cv2.COLOR_BGR2RGB)

plt.figure("Questão 1 - Letra F) Sistemas RGB, Lab, HSV e YC")
plt.subplot(1,4,1)
plt.imshow(img_rgb)
plt.title("RGB")

# Imagem Lab
img_Lab = cv2.cvtColor(img_recorte,cv2.COLOR_BGR2Lab)

plt.subplot(1,4,2)
plt.imshow(img_Lab)
plt.title("Lab")

# Imagem HSV
img_HSV = cv2.cvtColor(img_recorte,cv2.COLOR_BGR2HSV)
plt.subplot(1,4,3)
plt.imshow(img_HSV)
plt.title("HSV")

# Imagem YCrCb
img_YCRCB = cv2.cvtColor(img_recorte,cv2.COLOR_BGR2YCR_CB)
plt.subplot(1,4,4)
plt.imshow(img_YCRCB)
plt.title("YCrCb")

plt.show()

print("Apresente uma figura para cada um dos sistemas de cores (RGB, HSV, Lab e YCrCb) contendo a imagem de cada um dos canais e seus respectivos histogramas.")

histograma_RGB = cv2.calcHist([img_rgb], [0], None, [256],[0,256])#o primeiro 0 é o numero de caniai
# Imagem RGB
plt.figure('Questão 1 - Letra G) Os sistemas RGB, Lab, HSV e YC e os seus respectivos histogramas')
plt.subplot(2,4,1)
plt.imshow(img_rgb)
plt.title("RGB")

plt.subplot(2,4,5)
plt.plot(histograma_RGB,color = 'black')
plt.title("Histograma RGB")
plt.xlim([0,256])
plt.xlabel("Valores de Pixels")
plt.ylabel("Número de Pixels")


# Imagem Lab
img_Lab = cv2.cvtColor(img_recorte,cv2.COLOR_BGR2Lab)
histograma_Lab = cv2.calcHist([img_Lab], [0], None, [256],[0,256])#o primeiro 0 é o numero de caniai

plt.subplot(2,4,2)
plt.imshow(img_Lab)
plt.title("Lab")

plt.subplot(2,4,6)
plt.plot(histograma_Lab,color = 'black')
plt.title("Histograma Lab")
plt.xlim([0,256])
plt.xlabel("Valores de Pixels")
plt.ylabel("Número de Pixels")


# Imagem HSV
img_HSV = cv2.cvtColor(img_recorte,cv2.COLOR_BGR2HSV)
histograma_HSV = cv2.calcHist([img_HSV], [0], None, [256],[0,256])#o primeiro 0 é o numero de caniai

plt.subplot(2,4,3)
plt.imshow(img_HSV)
plt.title("HSV")

plt.subplot(2,4,7)
plt.plot(histograma_HSV,color = 'black')
plt.title("Histograma HSV")
plt.xlim([0,256])
plt.xlabel("Valores de Pixels")
plt.ylabel("Número de Pixels")

# Imagem YCrCb
img_YCRCB = cv2.cvtColor(img_recorte,cv2.COLOR_BGR2YCR_CB)
histograma_YCRCB = cv2.calcHist([img_YCRCB], [0], None, [256],[0,256])#o primeiro 0 é o numero de caniai

plt.subplot(2,4,4)
plt.imshow(img_YCRCB)
plt.title("YCrCb")

plt.subplot(2,4,8)
plt.plot(histograma_YCRCB,color = 'black')
plt.title("Histograma YCRCB")
plt.xlim([0,256])
plt.xlabel("Valores de Pixels")
plt.ylabel("Número de Pixels")
plt.show()

print("Letra H)")
print("Encontre o sistema de cor e o respectivo canal que propicie melhor segmentação da imagem de modo a remover o fundo da imagem utilizando limiar manual e limiar obtido pela técnica de Otsu."
      "Nesta questão apresente o histograma com marcação dos limiares utilizados, a imagem limiarizada (binarizada) e a imagem colorida final obtida da segmentação. Explique os resultados e sua escolha pelo sistema de cor e canal utilizado na segmentação. Nesta questão apresente a imagem limiarizada (binarizada) e a imagem colorida final obtida da segmentação.")


print('Letra H) Melhor segmentação: Sistema de cor HSV')
img_rc = 'recorte.jpg'
img_bgr = cv2.imread(img_rc,1)
img_HSV = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
img_ycb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2YCR_CB)
H,S,V = cv2.split(img_HSV)
########################################################################################################################
# Histograma de imagem
hist_H = cv2.calcHist([img_HSV],[0],None,[256],[0,256])
hist_S = cv2.calcHist([img_HSV],[1],None,[256],[0,256])
hist_V = cv2.calcHist([img_HSV],[2],None,[256],[0,256])

########################################################################################################################
# Limiar manual
limiar_H = 147
(L_HM, img_limiar_H) = cv2.threshold(H,limiar_H,255,cv2.THRESH_BINARY)
limiar_S = 92
(L_SM, img_limiar_S) = cv2.threshold(S,limiar_S,255,cv2.THRESH_BINARY)
limiar_V = 128
(L_VM, img_limiar_V) = cv2.threshold(V,limiar_V,255,cv2.THRESH_BINARY)

########################################################################################################################
# Limiarização - Thresholding - OTSU
(L_H, img_limiar_H_O) = cv2.threshold(H,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
(L_S, img_limiar_S_O) = cv2.threshold(S,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
(L_V, img_limiar_V_O) = cv2.threshold(V,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
########################################################################################################################

# Plotar imagens - Limiar manual
plt.figure('Questão 1 - Letra H) Limiarização')
plt.subplot(3,4,1)
plt.imshow(img_HSV[:,:,0],cmap='gray')
plt.title("H")

plt.subplot(3,4,2)
plt.plot(hist_H,color = 'black')
plt.axvline(x=limiar_H, color = 'blue')
plt.title("Histograma - H")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,4,5)
plt.imshow(img_HSV[:,:,1],cmap='gray')
plt.title("S")

plt.subplot(3,4,6)
plt.plot(hist_S,color = 'black')
plt.axvline(x=limiar_S,color = 'red')
plt.title("Histograma - S")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,4,9)
plt.imshow(img_HSV[:,:,2],cmap='gray')
plt.title("V")

plt.subplot(3,4,10)
plt.plot(hist_V,color = 'black')
plt.axvline(x=limiar_V,color = 'green')
plt.title("Histograma - V")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

#Limiar de OTSU
plt.subplot(3,4,3)
plt.imshow(img_HSV[:,:,0],cmap='gray')
plt.title("H")

plt.subplot(3,4,4)
plt.plot(hist_H,color = 'black')
plt.axvline(x=L_H, color = 'blue')
plt.title("Histograma - H - OTSU")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,4,7)
plt.imshow(img_HSV[:,:,1],cmap='gray')
plt.title("S")

plt.subplot(3,4,8)
plt.plot(hist_S,color = 'black')
plt.axvline(x=L_S,color = 'red')
plt.title("Histograma - S - OTSU")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,4,11)
plt.imshow(img_HSV[:,:,2],cmap='gray')
plt.title("V")

plt.subplot(3,4,12)
plt.plot(hist_V,color = 'black')
plt.axvline(x=L_V,color = 'green')
plt.title("Histograma - V - OTSU")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")
plt.show()

########################################################################################################################
# Obter imagem colorida segmentada
# Melhor Canal S usando o limiar de Otsu
img_segm = cv2.bitwise_and(img_rgb,img_rgb,mask=img_limiar_S_O)

# Plotar imagem colorida segmentada
plt.figure('Questão 1 - Letra H) Imagem Segmentada Usando o Limiar de Otsu ')
plt.subplot(1,3,1)
plt.imshow(img_rgb,cmap="gray")
plt.title("Original")

plt.subplot(1,3,2)
plt.imshow(img_HSV,cmap="gray")
plt.title("HSV")

plt.subplot(1,3,3)
plt.imshow(img_segm)
plt.title('Segmentada')


plt.show()

print("letra I)")
print("Obtenha o histograma de cada um dos canais da imagem em RGB, utilizando como mascara a imagem limiarizada (binarizada) da letra h.")

(L_S_O, img_limiar_S_O) = cv2.threshold(S,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
hist_r = cv2.calcHist([img_rgb],[0],img_limiar_S_O,[256],[0,256])
hist_g = cv2.calcHist([img_rgb],[1],img_limiar_S_O,[256],[0,256])
hist_b = cv2.calcHist([img_rgb],[2],img_limiar_S_O,[256],[0,256])

########################################################################################################################
# Plotar Imagem RGB
plt.figure('Questão 1 - Letra I) histograma de cada um dos canais da imagem em RGB, utilizando como mascara a imagem limiarizada (binarizada) da letra H')
plt.subplot(2,3,1)
plt.imshow(img_rgb[:,:,0],cmap='gray')
plt.title("R")

plt.subplot(2,3,4)
plt.plot(hist_r,color = 'r')
#plt.axvline(x=L_S_O, color='black')
plt.title("Histograma - R")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,3,2)
plt.imshow(img_rgb[:,:,1],cmap='gray')
plt.title("G")

plt.subplot(2,3,5)
plt.plot(hist_g,color = 'g')
#plt.axvline(x=L_S, color='black')
plt.title("Histograma - G")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,3,3)
plt.imshow(img_rgb[:,:,2],cmap='gray')
plt.title("B")

plt.subplot(2,3,6)
plt.plot(hist_b,color = 'b')
#plt.axvline(x=L_S, color='black')
plt.title("Histograma - B")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.show()

print("letra J)")
print("Realize operações aritméticas na imagem em RGB de modo a realçar os aspectos de seu interesse. Exemplo (2*R-0.5*G). Explique a sua escolha pelas operações aritméticas. Segue abaixo algumas sugestões.")

img_cut = 'recorte.jpg'
img_cut_bgr = cv2.imread(img_cut,1)
img_cut_rgb = cv2.cvtColor(img_cut_bgr,cv2.COLOR_BGR2RGB)

R,G,B = cv2.split(img_cut_rgb)
##Modelos de Realce
#De acordo com os histogramas neste caso percebe-se que há predominacia nas cores Red e Green.
BI =G*2.5-R+B
##Outros modelos
#NGRDI_denominador= cv2.sqrt((G^2,R^2,B^2)/3)
#BGI=cv2.divide(B,G)

from matplotlib import pyplot as plt # Importa o pacote matplotlib
plt.figure("Realce dos Aspectos")
plt.subplot(1,3,1)
plt.imshow(img_cut_rgb)
plt.title("Imagem Original - RGB ")
plt.colorbar(orientation= "horizontal")

plt.subplot(1,3,2)
plt.imshow(BI, cmap="gray")
plt.title("Realce em cinza")
plt.colorbar(orientation= "horizontal")

plt.subplot(1,3,3)
plt.imshow(BI, cmap="jet")
plt.title("Realce em JET")
plt.colorbar(orientation= "horizontal")
plt.show()  
print("o fruto apresentou pixels com intensidade mais escura e o fundo com tonalidade mais claras e na escala “Jet”, a pigmentação da casca demonstrou tonalidades mais frias, próximo ao azul,"
      " enquanto que o fundo possuiu tonalidades mais quentes, próximo ao vermelho (imagens acima)."
      " Portanto, conclui-se que dependendo da imagem a ser usada e do aspecto de interesse a ser realçado, as operações aritméticas adotadas são alteradas conforme o objetivo da pesquisa.")

