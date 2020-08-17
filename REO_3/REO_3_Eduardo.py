########################################################################################################################
# DATA: 17/08/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# ALUNO: EDUARDO ALVES DA SILVA
# GITHUB: eduardo-a-silva
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# GITHUB: vqcarneiro
########################################################################################################################
# EXERCÍCIO 01:
########################################################################################################################
# Importar pacotes
print("---------------------------------------------------------------------------------------------------------------")
import numpy as np
import cv2
from matplotlib import pyplot as plt

print("Exercicio N°1")
print("Selecione uma imagem a ser utilizada no trabalho prático e realize os seguintes processos utilizando "
      "as bibliotecas OPENCV e Scikit-Image do Python:")
########################################################################################################################
# Leitura da imagem
arquivo="BD_recorte.jpg"
img_bgr = cv2.imread(arquivo,1)
img_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
#Apresentar a imagem
plt.figure("Imagem selecionada")
plt.imshow(img_rgb)
plt.title("Imagem selecionada")
plt.xticks([])
plt.yticks([])
plt.show()

########################################################################################################################

print("Letra A)")
print("Aplique o filtro de média com cinco diferentes tamanhos de kernel e compare os resultados com a imagem original;")

#Aplicar os filtros
#Filtros de Média
img_F1=cv2.blur(img_rgb, (3,3))
img_F2=cv2.blur(img_rgb, (7,7))
img_F3=cv2.blur(img_rgb, (11,11))
img_F4=cv2.blur(img_rgb, (15,15))
img_F5=cv2.blur(img_rgb, (19,19))

#Plotar as imagens
plt.figure("Letra A) Filtro de média com diferentes tamanhos de kernel")
plt.subplot(2,3,1)
plt.imshow(img_rgb)
plt.title("Imagem Original")
plt.xticks([])#Eliminar o eixo x
plt.yticks([])#Eliminar o eixo y

plt.subplot(2,3,2)
plt.imshow(img_F1)
plt.title("Kernel 3x3")
plt.xticks([])#Eliminar o eixo x
plt.yticks([])#Eliminar o eixo y

plt.subplot(2,3,3)
plt.imshow(img_F2)
plt.title("Kernel 7x7")
plt.xticks([])#Eliminar o eixo x
plt.yticks([])#Eliminar o eixo y

plt.subplot(2,3,4)
plt.imshow(img_F3)
plt.title("Kernel 11x11")
plt.xticks([])#Eliminar o eixo x
plt.yticks([])#Eliminar o eixo y

plt.subplot(2,3,5)
plt.imshow(img_F4)
plt.title("Kernel 15x15")
plt.xticks([])#Eliminar o eixo x
plt.yticks([])#Eliminar o eixo y

plt.subplot(2,3,6)
plt.imshow(img_F5)
plt.title("Kernel 19x19")
plt.xticks([])#Eliminar o eixo x
plt.yticks([])#Eliminar o eixo y

plt.show()

########################################################################################################################

print("Letra B)")
print("Aplique diferentes tipos de filtros com pelo menos dois tamanhos de kernel "
      "e compare os resultados entre si e com a imagem original.")
##Uso de diferentes Filtros
#Filtro de média
img_F_media_1=cv2.blur(img_rgb, (3,3))#O F corresponde a Filtro(Ex:F_media; é o filtro de média)
img_F_media_2=cv2.blur(img_rgb, (15,15))

#Filtro com base na média ponderada ("0" é usado para determinar os pesos de cada pixel de forma aleatória, vizinhos mais próximos com peso maior)
img_F_gaussiano_1=cv2.GaussianBlur(img_rgb,(3,3),0)
img_F_gaussiano_2=cv2.GaussianBlur(img_rgb,(15,15),0)

#Filtro de mediana (Seleciona um pixel mais comum, um valor mais comum naquela região
img_F_mediana_1=cv2.medianBlur(img_rgb,3)
img_F_mediana_2=cv2.medianBlur(img_rgb,15)

#Filtro bilateral, elimina os pixels muito discrepantes na imagem(os outliers)
img_F_bilateral_1=cv2.bilateralFilter(img_rgb,3,3,5)###também
img_F_bilateral_2=cv2.bilateralFilter(img_rgb,15,11,9)###O 2° argumento é o desvio padrão em relação a intesidade (Quanto vai eliminar)
###3° a distancia entre os vizinhos

#Plotar as imagens obtidas com diferentes filtros
plt.figure("Letra B) Diferentes Filtros e Dois Tamanhos de Kernel")
plt.subplot(5,2,1)
plt.imshow(img_rgb)
plt.title("Imagem Original")
plt.xticks([])#Eliminar o eixo x
plt.yticks([])#Eliminar o eixo y

plt.subplot(5,2,3)
plt.imshow(img_F_media_1)
plt.title("Filtro de Média - Kernel 3x3")
plt.xticks([])
plt.yticks([])

plt.subplot(5,2,4)
plt.imshow(img_F_media_2)
plt.title("Filtro de Média - Kernel 15x15")
plt.xticks([])
plt.yticks([])

plt.subplot(5,2,5)
plt.imshow(img_F_gaussiano_1)
plt.title("Filtro de Média Ponderada - Kernel 3x3")
plt.xticks([])
plt.yticks([])

plt.subplot(5,2,6)
plt.imshow(img_F_gaussiano_2)
plt.title("Filtro de Média Ponderada - Kernel 15x15")
plt.xticks([])
plt.yticks([])

plt.subplot(5,2,7)
plt.imshow(img_F_bilateral_1)
plt.title("Filtro Bilateral - Kernel 3x3")
plt.xticks([])
plt.yticks([])

plt.subplot(5,2,8)
plt.imshow(img_F_bilateral_2)
plt.title("Filtro Bilateral - Kernel 15x15")
plt.xticks([])
plt.yticks([])

plt.subplot(5,2,9)
plt.imshow(img_F_mediana_1)
plt.title("Filtro de mediana - Kernel 3x3")
plt.xticks([])
plt.yticks([])

plt.subplot(5,2,10)
plt.imshow(img_F_mediana_2)
plt.title("Filtro de mediana - Kernel 15x15")
plt.xticks([])
plt.yticks([])

plt.show()

########################################################################################################################
print("Letra C)")
print("Realize a segmentação da imagem utilizando o processo de limiarização."
      " Utilizando o reconhecimento de contornos, identifique e salve os objetos de interesse."
      " Além disso, acesse as bibliotecas Opencv e Scikit-Image, verifique as variáveis que podem ser mensuradas e "
      " extraia as informações pertinentes (crie e salve uma tabela com estes dados)."
      " Apresente todas as imagens obtidas ao longo deste processo")

########################################################################################################################
#Suavização das banda R, G, B para melhor obtenção da máscara para a limiarização
########################################################################################################################
#Separação das bandas
r,g,b=cv2.split(img_rgb)

#Aplicar filtro nas bandas
r_med=cv2.medianBlur(r, 25)
g_med=cv2.medianBlur(g, 25)
b_med=cv2.medianBlur(b, 25)

#Bandas originais e com filtro aplicado
plt.figure("Letra C) Canais: R, G e B")
plt.subplot(2,3,1)
plt.imshow(r, cmap="gray")
plt.title("R")
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,4)
plt.imshow(r_med, cmap="gray")
plt.title("R mediana - kernel 25x25")
plt.xticks([])
plt.yticks([])


plt.subplot(2,3,2)
plt.imshow(g, cmap="gray")
plt.title("G")
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,5)
plt.imshow(g_med, cmap="gray")
plt.title("G mediana - kernel 25x25")
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,3)
plt.imshow(b, cmap="gray")
plt.title("B")
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,6)
plt.imshow(b_med, cmap="gray")
plt.title("B mediana - kernel 25x25")
plt.xticks([])
plt.yticks([])

plt.show()


########################################################################################################################
#Obtenção das mácascaras/limiares para a segmentação da Imagem de batata-doce
#Histogramas
########################################################################################################################
#Limiarização de OTSU
#Banda B original
histograma_1=cv2.calcHist([b],[0],None,[256], [0,256])
l, img_1=cv2.threshold(b,0,256,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
 #Banda B suavizada
histograma_2=cv2.calcHist([b_med],[0],None,[256], [0,256])
l_B, img_B_1=cv2.threshold(b_med,0,256,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
########################################################################################################################
#Apresentando das máscaras obtidas do Canal BLUE da imagem e do mesmo canal com precesso de filtro de mediana e
#  os respectivos histogramas.
########################################################################################################################
#Máscascaras obtidas
plt.figure("Letra C) Obtenção da Máscara")
plt.subplot(2,3,1)
plt.imshow(b, cmap="gray")
plt.title("Canal B - Original")
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,2)
plt.plot(histograma_1, color='r')
plt.axvline(x=l, color='k')
plt.title("L: " + str(l))
plt.xlim([0,256])
plt.ylabel("Número de Pixels")

plt.subplot(2,3,3)
plt.imshow(img_1, cmap="gray")
plt.title("Mascara")
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,4)
plt.imshow(b_med, cmap="gray")
plt.title("Canal B - Filtro Mediana")
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,5)
plt.plot(histograma_2, color="r")
plt.axvline(x=l_B, color="k")
plt.title("L: " + str(l_B))
plt.xlim([0,256])
plt.ylabel("Número de Pixels")

plt.subplot(2,3,6)
plt.imshow(img_B_1, cmap="gray")
plt.title("Máscara com Filtro")
plt.xticks([])
plt.yticks([])

plt.show()

########################################################################################################################
#Imagem segmentada com base no canal B e no canal B suavizado
########################################################################################################################
#Obtenção das imagens segmentadas
#Máscara original
img_seg = cv2.bitwise_and(img_rgb,img_rgb,mask=img_1)

#Máscara suavizada
img_seg_1 = cv2.bitwise_and(img_rgb,img_rgb,mask=img_B_1)

#Imagens obtidas
plt.figure("Letra C) Imagens Segmentadas")
plt.subplot(1,3,1)
plt.imshow(img_rgb)
plt.title("Imagem Original")
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,2)
plt.imshow(img_seg)
plt.xticks([])
plt.yticks([])
plt.title("Mascara sem Filtro")

plt.subplot(1,3,3)
plt.imshow(img_seg_1)
plt.xticks([])
plt.yticks([])
plt.title("Mascara com Filtro")
plt.show()

#Outro sistema de cor para a obtenção das máscaras
#######################################################################
#Utilização do sistema YCrCb para a obtenção das máscaras.
#######################################################################
#Tranformação da imagem para o sistema YCrCb
img_YCRCB = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2YCR_CB)
#Obtenção das bandas
y,cr,cb=cv2.split(img_YCRCB)

#Aplicar filtro nas bandas
y_med=cv2.medianBlur(y, 15)
cr_med=cv2.medianBlur(cr, 15)
cb_med=cv2.medianBlur(cb, 15)

#Bandas originais e as mesmas com filtro aplicado
plt.figure("Letra C) Sistema YCrCb")
plt.subplot(2,3,1)
plt.imshow(y, cmap="gray")
plt.title("Y")
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,4)
plt.imshow(y_med, cmap="gray")
plt.title("Y mediana - kernel 25x25")
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,2)
plt.imshow(cr, cmap="gray")
plt.title("Cr")
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,5)
plt.imshow(cr_med, cmap="gray")
plt.title("Cr mediana - kernel 25x25")
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,3)
plt.imshow(cb, cmap="gray")
plt.title("Cb")
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,6)
plt.imshow(cb_med, cmap="gray")
plt.title("Cb mediana - kernel 25x25")
plt.xticks([])
plt.yticks([])
plt.show()
########################################################################################################################
#Imagem segmentada com base no canal Cb e no canal Cb suavizado
########################################################################################################################
#Obtenção das imagens segmentadas
#histogramas
########################################################################################################################
#Limiarização de OTSU
histograma_1=cv2.calcHist([cb],[0],None,[256], [0,256])
l_3, img_1=cv2.threshold(cb,0,256,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

histograma_2=cv2.calcHist([cb_med],[0],None,[256], [0,256])
l_B1, img_cB_1=cv2.threshold(cb_med,0,256,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
########################################################################################################################
#Apresentando as máscaras obtidas do Canal Cb da imagem e do mesmo canal com precesso de filtro de mediana e
#  os respectivos histogramas.
########################################################################################################################
plt.figure("Letra C) Obtenção da Mascara")
plt.subplot(2,3,1)
plt.imshow(cb, cmap="gray")
plt.title("Canal Cb - Original")
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,2)
plt.plot(histograma_1, color="r")
plt.axvline(x=l_3, color="k")
plt.title("L: " + str(l))
plt.xlim([0,256])
plt.ylabel("Número de Pixels")

plt.subplot(2,3,3)
plt.imshow(img_1, cmap="gray")
plt.title("Mascara")
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,4)
plt.imshow(cb_med, cmap="gray")
plt.title("Canal Cb - Filtro Mediana")
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,5)
plt.plot(histograma_2, color="r")
plt.axvline(x=l_B1, color="k")
plt.title("L: " + str(l_B))
plt.xlim([0,256])
plt.ylabel("Número de Pixels")

plt.subplot(2,3,6)
plt.imshow(img_cB_1, cmap="gray")
plt.title("Máscara com Filtro")
plt.xticks([])
plt.yticks([])

plt.show()
########################################################################################################################
#Imagem segmentada com base no canal CB e no canal CB suavizado
########################################################################################################################
#Obtenção das imagens segmentadas
#Máscara original
img_seg = cv2.bitwise_and(img_rgb,img_rgb,mask=img_1)

#Máscara suavizada
img_seg_f = cv2.bitwise_and(img_rgb,img_rgb,mask=img_cB_1)

#Imagens
plt.figure("Letra C) Segmentação com as mascaras")
plt.subplot(1,3,1)
plt.imshow(img_rgb)
plt.title("Imagem Original")
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,2)
plt.imshow(img_seg)
plt.title("Mascara sem Filtro")
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,3)
plt.imshow(img_seg_f)
plt.title("Mascara com Filtro")
plt.xticks([])
plt.yticks([])

plt.show()

########################################################################################################################
#Salvar a imagem segmentada
########################################################################################################################
img_seg_new=cv2.cvtColor(img_seg_f,cv2.COLOR_BGR2RGB)
cv2.imwrite("IMG_segmentada.jpg", img_seg_new)

#Imagem segmentada
plt.figure("Letra C)Imagem Segmentada")
plt.imshow(img_seg_f)
plt.title("Imagem segmentada")
plt.xticks([])
plt.yticks([])
plt.show()


#Importar pacote
from skimage.measure import label, regionprops

###########################################################################
#Objetos
mascara=img_cB_1.copy()
cnts, h = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

########################################################################################################################
#DadosCom a utilização da biblioteca Scikit-Image é possível identificar o numero de objetos na imagem automaticamente.
#Além disso, esta mesma biblioteca, nos permite estimar inúmeras informações de cada objeto na imagem, como exemplo a área,
#  o perímetro, largura, medidas de cor e ainda permite selecionar e salvar cada objeto separadamente em uma nova imagem .

########################################################################################################################
#Obtenção de informações com o pacote Scikit-Image
print("-"*50)
for (i,c) in enumerate(cnts):
      (x,y,w,h) =cv2.boundingRect(c)
      obj = img_cB_1[y:y+h, x:x+w]
      obj_rgb = img_seg_f[y:y+h, x:x+w]
      obj_bgr = cv2.cvtColor(obj_rgb, cv2.COLOR_RGBA2BGR)
      cv2.imwrite("s"+str(i+1) + ".png", obj_bgr)
      cv2.imwrite('sb' + str(i+1) + '.png', obj)

      regiao = regionprops(obj)
      print('Batatas', str(i+1))
      print("Dimensão da imagem", np.shape(obj))
      print("Medidas Fisicas")
      print("Centroide", regiao[0].centroid)
      print('Comprimento do eixo menor: ', regiao[0].minor_axis_length)
      print('Comprimento do eixo maior: ', regiao[0].major_axis_length)
      print('Razão: ', regiao[0].major_axis_length / regiao[0].minor_axis_length)
      area = cv2.contourArea(c)
      print('Área: ', area)
      print('Perímetro: ', cv2.arcLength(c, True))

      print('Medidas de Cor')
      min_val_r, max_val_r, min_loc_r, max_loc_r = cv2.minMaxLoc(obj_rgb[:, :, 0], mask=obj)
      print('Valor Mínimo no R: ', min_val_r, ' - Posição: ', min_loc_r)
      print('Valor Máximo no R: ', max_val_r, ' - Posição: ', max_loc_r)
      med_val_r = cv2.mean(obj_rgb[:, :, 0], mask=obj)
      print('Média no Vermelho: ', med_val_r)

      min_val_g, max_val_g, min_loc_g, max_loc_g = cv2.minMaxLoc(obj_rgb[:, :, 1], mask=obj)
      print('Valor Mínimo no G: ', min_val_g, ' - Posição: ', min_loc_g)
      print('Valor Máximo no G: ', max_val_g, ' - Posição: ', max_loc_g)
      med_val_g = cv2.mean(obj_rgb[:, :, 1], mask=obj)
      print('Média no Verde: ', med_val_g)

      min_val_b, max_val_b, min_loc_b, max_loc_b = cv2.minMaxLoc(obj_rgb[:, :, 2], mask=obj)
      print('Valor Mínimo no B: ', min_val_b, ' - Posição: ', min_loc_b)
      print('Valor Máximo no B: ', max_val_b, ' - Posição: ', max_loc_b)
      med_val_b = cv2.mean(obj_rgb[:, :, 2], mask=obj)
      print('Média no Azul: ', med_val_b)
      print('-' * 50)

########################################################################################################################
print('Total de cortes: ', len(cnts))
print('-'*50)
########################################################################################################################

seg = img_seg_f.copy()
cv2.drawContours(seg,cnts,-1,(0,255,0),2)

#Apresentação da Imagem com os contornos
plt.figure("Batata-Doce")
plt.imshow(seg)
plt.xticks([])
plt.yticks([])

plt.show()

########################################################################################################################
print("Letra D)")
print("Utilizando máscaras, apresente o histograma somente dos objetos de interesse.")
########################################################################################################################
#Leitura da imagem
########################################################################################################################
arq="IMG_segmentada.jpg"
imagem_bgr = cv2.imread(arq,1)
imagem_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
#Obtenção do histograma
histograma_3=cv2.calcHist([imagem_rgb],[0],None,[256], [0,256])

#Plotar as imagens
plt.figure("Letra D) Segmentação com as mascaras")
plt.subplot(3,1,1)
plt.imshow(imagem_rgb)
plt.title("Imagem Original")
plt.xticks([])
plt.yticks([])

plt.subplot(3,1,2)
plt.imshow(img_seg_f)
plt.title("Imagem Segmentada")
plt.xticks([])
plt.yticks([])

plt.subplot(3,1,3)
plt.plot(histograma_3, color="r")
plt.title("Histograma da imagem segmentada ")
plt.xlim([0,256])
plt.ylabel("Número de Pixels")

plt.show()


########################################################################################################################
#Codigo para criar o arquivo e salavar em CSV
#Importar o pacote pandas
import pandas as pd
mask = np.zeros(img_rgb.shape,dtype = np.uint8)
cnts = cv2.findContours(mascara,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

dimen = []
for (i,c) in enumerate(cnts):
    (x,y,w,h) = cv2.boundingRect(c)
    obj = img_seg_f[y:y+h,x:x+w]
    obj_bgr = cv2.cvtColor(obj,cv2.COLOR_RGB2BGR)
    area = cv2.contourArea(c)
    razao = round(h/w,2)
    dimen += [[str(i+1),str(h),str(w),str(area),str(razao)]]

dados_batata = pd.DataFrame(dimen)
dados_batata = dados_batata.rename(columns={0:"BATATA", 1: "ALTURA",2:"LARGURA",3:"AREA",4:"RAZAO" })
dados_batata.to_csv("Informações dos Objetos(SCIKIT_IMAGE).csv",index=False,sep=";")

########################################################################################################################
########################################################################################################################
#Criar um arquivo de TXT para salvar os dados.
########################################################################################################################
#Importar pacotes
from datetime import date
data_atual = date.today()
########################################################################################################################

with open('Resultados_SCIKIT_IMAGE.txt', 'w') as arquivo:
      print("_"*60, file=arquivo)
      print(" ", file=arquivo)
      print("Análise de dados utilizando o programa Python", file=arquivo)
      print("Dados analisados em: ", data_atual, file=arquivo)
      print("Análise feita por: Silva, E. A.", file=arquivo)
      print(" ", file=arquivo)
      print("Arquivo com os dados obtidos com o pacote Scikit-Image", file=arquivo)
      print("_" * 60, file=arquivo)
      print('Número de cortes a serem apresentados: ', len(cnts), file=arquivo)
      print("=" * 60, file=arquivo)
      for (i, c) in enumerate(cnts):
            (x, y, w, h) = cv2.boundingRect(c)
            obj = img_B_1[y:y + h, x:x + w]
            obj_rgb = img_seg_f[y:y + h, x:x + w]
            obj_bgr = cv2.cvtColor(obj_rgb, cv2.COLOR_RGBA2BGR)
            cv2.imwrite("s" + str(i + 1) + ".png", obj_bgr)
            cv2.imwrite('sb' + str(i + 1) + '.png', obj)

            regiao = regionprops(obj)
            print('Batatas', str(i + 1), file=arquivo)
            print('=' * 60, file=arquivo)
            print("Dimensão da imagem", np.shape(obj), file=arquivo)
            print('_' * 20, file=arquivo)
            print("Medidas Fisicas", file=arquivo)
            print('_' * 20, file=arquivo)
            print("Centroide", regiao[0].centroid, file=arquivo)
            print('Comprimento do eixo menor: ', regiao[0].minor_axis_length, file=arquivo)
            print('Comprimento do eixo maior: ', regiao[0].major_axis_length, file=arquivo)
            print('Razão: ', regiao[0].major_axis_length / regiao[0].minor_axis_length, file=arquivo)
            area = cv2.contourArea(c)
            print('Área: ', area, file=arquivo)
            print('Perímetro: ', cv2.arcLength(c, True), file=arquivo)

            print('_' * 20, file=arquivo)
            print('Medidas de Cor', file=arquivo)
            print('_' * 20, file=arquivo)
            min_val_r, max_val_r, min_loc_r, max_loc_r = cv2.minMaxLoc(obj_rgb[:, :, 0], mask=obj)
            print('Valor Mínimo no R: ', min_val_r, ' - Posição: ', min_loc_r, file=arquivo)
            print('Valor Máximo no R: ', max_val_r, ' - Posição: ', max_loc_r, file=arquivo)
            med_val_r = cv2.mean(obj_rgb[:, :, 0], mask=obj)
            print('Média no Vermelho: ', med_val_r, file=arquivo)

            min_val_g, max_val_g, min_loc_g, max_loc_g = cv2.minMaxLoc(obj_rgb[:, :, 1], mask=obj)
            print('Valor Mínimo no G: ', min_val_g, ' - Posição: ', min_loc_g, file=arquivo)
            print('Valor Máximo no G: ', max_val_g, ' - Posição: ', max_loc_g, file=arquivo)
            med_val_g = cv2.mean(obj_rgb[:, :, 1], mask=obj)
            print('Média no Verde: ', med_val_g, file=arquivo)

            min_val_b, max_val_b, min_loc_b, max_loc_b = cv2.minMaxLoc(obj_rgb[:, :, 2], mask=obj)
            print('Valor Mínimo no B: ', min_val_b, ' - Posição: ', min_loc_b, file=arquivo)
            print('Valor Máximo no B: ', max_val_b, ' - Posição: ', max_loc_b, file=arquivo)
            med_val_b = cv2.mean(obj_rgb[:, :, 2], mask=obj)
            print('Média no Azul: ', med_val_b, file=arquivo)
            print('=' * 60, file=arquivo)

########################################################################################################################
print("Letra E)")
print("Realize a segmentação da imagem utilizando a técnica de k-means. Apresente as imagens obtidas neste processo.")
########################################################################################################################

########################################################################################################################
print('Dimensão: ',np.shape(img_rgb))
print(np.shape(img_rgb)[0], ' x ',np.shape(img_rgb)[1], ' = ', np.shape(img_rgb)[0] * np.shape(img_rgb)[1])
print('--------------------------------------------------------------------------------------------------------------')

# Formatação da imagem para uma matriz de dados
pixel_values = img_rgb.reshape((-1, 3))

# Conversão para Decimal
pixel_values = np.float32(pixel_values)
print("-"*80)
print("Dimensão Matriz: ",pixel_values.shape)
print('-'*80)

########################################################################################################################
# K-means
# Critério de Parada
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

########################################################################################################################
# Número de Grupos (k)
k = 2
dist, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 30, cv2.KMEANS_RANDOM_CENTERS)
print("SQ das Distâncias de Cada Ponto ao Centro: ", dist)
print("Dimensão labels: ", labels.shape)
print("Valores únicos: ",np.unique(labels))
print("Tipo labels: ", type(labels))
print("-"*80)

########################################################################################################################
# flatten the labels array
labels = labels.flatten()
print("Dimensão flatten labels: ", labels.shape)
print("Tipo labels (f): ", type(labels))
print("-"*80)

########################################################################################################################
# Valores dos labels
val_unicos,contagens = np.unique(labels,return_counts=True)
val_unicos = np.reshape(val_unicos,(len(val_unicos),1))
contagens = np.reshape(contagens,(len(contagens),1))
# Histograma
hist = np.concatenate((val_unicos,contagens),axis=1)
print("Histograma")
print(hist)
print("-"*80)
print("Centroides Decimais")
print(centers)
print("-"*80)

########################################################################################################################
# Conversão dos centroides para valores de interos de 8 digitos
centers = np.uint8(centers)
print("-"*80)
print("Centroides uint8")
print(centers)
print("-"*80)

########################################################################################################################
# Conversão dos pixels para a cor dos centroides.
matriz_segmentada = centers[labels]
print("-"*80)
print("Dimensão Matriz Segmentada: ",matriz_segmentada.shape)
print("Matriz Segmentada")
print(matriz_segmentada[0:5,:])
print("-"*80)

########################################################################################################################
# Reformatar a matriz na imagem de formato original
########################################################################################################################
img_segmentada = matriz_segmentada.reshape(img_rgb.shape)
##Criar grupos
# Grupo 1
original_01 = np.copy(img_rgb)
matriz_or_01 = original_01.reshape((-1, 3))
matriz_or_01[labels != 0] = [0, 0, 0]
img_final_01 = matriz_or_01.reshape(img_rgb.shape)

# Grupo 2
original_02 = np.copy(img_rgb)
matriz_or_02 = original_02.reshape((-1, 3))
matriz_or_02[labels != 1] = [0, 0, 0]
img_final_02 = matriz_or_02.reshape(img_rgb.shape)

########################################################################################################################
#Segmentação com base no K-means
# Apresentar Imagem
plt.figure("Letra E) Imagens")
plt.subplot(2,2,1)
plt.imshow(img_rgb)
plt.title("Original")
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,2)
plt.imshow(img_segmentada)
plt.title("Rotulos")
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(img_final_01)
plt.title("Grupo 1")
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(img_final_02)
plt.title("Grupo 2")
plt.xticks([])
plt.yticks([])


plt.show()

########################################################################################################################
print("Letra F)")
print("Realize a segmentação da imagem utilizando a técnica de watershed. Apresente as imagens obtidas neste processo.")
#Importar pacotes
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy import ndimage

########################################################################################################################
# Leitura da imagem em YCrCb
img_YCRCB = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2YCR_CB)

#Partição dos canais
y,cr,cb=cv2.split(img_YCRCB)

# Limiarização - OTSU
limiar, mask =cv2.threshold(cb,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Distancia entre pontos brancos da mascara e pontos pretos do fundo (zero)
img_dist = ndimage.distance_transform_edt(mask)

# Localização e separação dos picos
max_local = peak_local_max(img_dist, indices= False, min_distance=100, labels=mask)#Distancia minima deve ser alterada
########################################################################################################################
print("-"*80)
print("Numero de picos")
print(np.unique(max_local, return_counts=True))
print("-"*80)

# Marcação dos picos
marcadores, n_marcadores = ndimage.label(max_local, structure=np.ones((3,3)))

print("Análise de conectividade")
print(np.unique(marcadores, return_counts=True))
print("o *0* provavelmente é o fundo")
print("-"*80)
########################################################################################################################

########################################################################################################################
# Imagem rotulada
#Segmentação Watershed
img_ws = watershed(-img_dist, marcadores, mask=mask)# o "-img_ws" o menos deve estar para inverter onde era pico vira vale
####################################
print("Número de discos de Batata-doce: ", len(np.unique(img_ws))-1)
print("-"*80)
img_final_1 = np.copy(img_rgb)
img_final_1[img_ws != 1] = [0,0,0] # Acessando a batata doce 1
img_final_2 = np.copy(img_rgb)
img_final_2[img_ws != 2] = [0,0,0] # Acessando a batata doce 2
img_final_3 = np.copy(img_rgb)
img_final_3[img_ws != 3] = [0,0,0] # Acessando a batata doce 3

########################################################################################################################
plt.figure('Letra F) Watershed')
plt.subplot(2,4,1)
plt.imshow(img_rgb)
plt.xticks([])
plt.yticks([])
plt.title("Original")

plt.subplot(2,4,2)
plt.imshow(cb,cmap="gray")
plt.xticks([])
plt.yticks([])
plt.title("Cb")

plt.subplot(2,4,3)
plt.imshow(mask,cmap="gray")
plt.xticks([])
plt.yticks([])
plt.title("Máscara")

plt.subplot(2,4,4)
plt.imshow(img_dist,cmap="jet")
plt.xticks([])
plt.yticks([])
plt.title("Picos")

plt.subplot(2,4,5)
plt.imshow(img_ws,cmap="jet")
plt.xticks([])
plt.yticks([])
plt.title("Batata-doce")

plt.subplot(2,4,6)
plt.imshow(img_final_1)
plt.xticks([])
plt.yticks([])
plt.title("Disco 1")

plt.subplot(2,4,7)
plt.imshow(img_final_2)
plt.xticks([])
plt.yticks([])
plt.title("Disco 2")

plt.subplot(2,4,8)
plt.imshow(img_final_3)
plt.xticks([])
plt.yticks([])
plt.title("Disco 3")

plt.show()

########################################################################################################################
print("Letra G)")
print("Compare os resultados das três formas de segmentação (limiarização, k-means e watershed) e identifique as potencialidades de cada delas.")
#Imagem segmentada com a mascara de WATERSHED
img_seg_ws = cv2.bitwise_and(img_rgb,img_rgb,mask=mask)

plt.figure("Três formas de segmentação")
plt.subplot(1,4,1)
plt.imshow(img_rgb)
plt.xticks([])
plt.yticks([])
plt.title("Original")

plt.subplot(1,4,2)
plt.imshow(img_seg_f)
plt.xticks([])
plt.yticks([])
plt.title("Limiarizada - Filtro de mediana")

plt.subplot(1,4,3)
plt.imshow(img_seg_ws)
plt.xticks([])
plt.yticks([])
plt.title("Watershed")

plt.subplot(1,4,4)
plt.imshow(img_final_02)
plt.xticks([])
plt.yticks([])
plt.title("K-means")

plt.show()
########################################################################################################################
