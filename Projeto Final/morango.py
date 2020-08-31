#######################################################################################################################
# DATA: 17/07/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# ALUNO: EDUARDO ALVES DA SILVA
# GITHUB: eduardo-a-silva
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# GITHUB: vqcarneiro
########################################################################################################################
#Trabalho prático final
#Fenotipagem com o uso de imagem em morango
########################################################################################################################
# Importar pacotes
print("---------------------------------------------------------------------------------------------------------------")
import numpy as np
import cv2
from matplotlib import pyplot as plt
########################################################################################################################

#Leitura da imagem
#Redimensionamento das imagens, pois estavam grandes e pesadas
import PIL
from PIL import Image
'''
mywidth = 1200
img = Image.open('1_A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('1 A resized.jpg')

### Imagem 1_B está corrompida! ###
img = Image.open('1 b.JPG')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('1 B resized.jpg')


img = Image.open('2_A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('2 A resized.jpg')

img = Image.open('2 B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('2 B resized.jpg')

img = Image.open('3 A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('3 A resized.jpg')

img = Image.open('3 B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('3 B resized.jpg')

img = Image.open('4_A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('4 A resized.jpg')

img = Image.open('4 B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('4 B resized.jpg')

img = Image.open('5_A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('5 A resized.jpg')

img = Image.open('5_B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('5 B resized.jpg')

img = Image.open('6_A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('6 A resized.jpg')

img = Image.open('6_B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('6 B resized.jpg')

img = Image.open('7_A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('7 A resized.jpg')

img = Image.open('7_B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('7 B resized.jpg')

img = Image.open('8 A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('8 A resized.jpg')

img = Image.open('8 B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('8 B resized.jpg')

img = Image.open('9_A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('9 A resized.jpg')

img = Image.open('9_B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('9 B resized.jpg')

### Imagem 10 está corrompida! ###
img = Image.open('10 a.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('10 A resized.jpg')

img = Image.open('10_B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('10 B resized.jpg')

img = Image.open('11_A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('11 A resized.jpg')


img = Image.open('11_B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('11 B resized.jpg')

img = Image.open('12 A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('12 A resized.jpg')

img = Image.open('12_B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('12 B resized.jpg')

img = Image.open('13 A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('13 A resized.jpg')

img = Image.open('13 B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('13 B resized.jpg')

img = Image.open('14 A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('14 A resized.jpg')

img = Image.open('14 B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('14 B resized.jpg')

img = Image.open('15 A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('15 A resized.jpg')

img = Image.open('15 B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('15 B resized.jpg')

img = Image.open('16 A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('16 A resized.jpg')

img = Image.open('16 B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('16 B resized.jpg')

img = Image.open('17 A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('17 A resized.jpg')

img = Image.open('17 B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('17 B resized.jpg')

img = Image.open('18_A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('18 A resized.jpg')

img = Image.open('18_B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('18 B resized.jpg')

img = Image.open('19_A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('19 A resized.jpg')

img = Image.open('19_B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('19 B resized.jpg')

img = Image.open('20_A.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('20 A resized.jpg')

img = Image.open('20_B.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('20 B resized.jpg')

'''
#Apos o redimensionamento foi feito o recorte da imagem
#Leitura da imagem
arquivo = "1 A resized.jpg"

img_bgr = cv2.imread(arquivo,1)
img_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)

#Apresentar a imagem selecionada
plt.figure("Imagem selecionada")
plt.imshow(img_rgb)
plt.title("Imagem selecionada")
plt.xticks([])
plt.yticks([])
plt.show()

#Recorte da imagem para captura da area de interesse
imagem1 = cv2.imread("1 A resized.jpg")
imagem_recorte = imagem1[100:550,473:1080]#primeiro é o y
cv2.imwrite("1 A resized rec.jpg", imagem_recorte)
imagem_recorte = cv2.cvtColor(imagem_recorte,cv2.COLOR_BGR2RGB)
img_rgb=imagem_recorte

#Apresentar a imagem recortada
plt.figure("Imagem selecionada")
plt.imshow(imagem_recorte)
plt.title("Imagem selecionada")
plt.xticks([])
plt.yticks([])
plt.show()

########################################################################################################################
#Suavização das banda R, G, B para melhor obtenção da máscara para a limiarização
########################################################################################################################
#Separação das bandas
r,g,b=cv2.split(img_rgb)

#Aplicar filtro nas bandas
r_med= cv2.medianBlur(r,9)
g_med= cv2.medianBlur(g,9)
b_med= cv2.medianBlur(b,9)

#Bandas originais e com filtro aplicado
plt.figure("Canais: R, G e B")
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
#Obtenção das mácascaras/limiares para a segmentação da Imagem do morango
#Histogramas
########################################################################################################################
#Limiarização de OTSU
#Banda B original
histograma_1=cv2.calcHist([r],[0],None,[256], [0,256])
l, img_1=cv2.threshold(r,0,256,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
 #Banda B suavizada
histograma_2=cv2.calcHist([r_med],[0],None,[256], [0,256])
l_B, img_B_1=cv2.threshold(r_med,0,256,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
########################################################################################################################
#Apresentando das máscaras obtidas do Canal BLUE da imagem e do mesmo canal com precesso de filtro de mediana e
#  os respectivos histogramas.
########################################################################################################################
#Máscascaras obtidas
plt.figure("Obtenção da Máscara")
plt.subplot(2,3,1)
plt.imshow(r, cmap="gray")
plt.title("Canal R - Original")
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
plt.imshow(r_med, cmap="gray")
plt.title("Canal R - Filtro Mediana")
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

#Outro sistema de cor para a obtenção das máscaras
#######################################################################
#Utilização do sistema YCrCb para a obtenção das máscaras.
#######################################################################
#Tranformação da imagem para o sistema YCrCb
img_YCRCB = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2YCR_CB)
#Obtenção das bandas
y,cr,cb=cv2.split(img_YCRCB)

#Aplicar filtro nas bandas
y_med=cv2.medianBlur(y, 19)
cr_med=cv2.medianBlur(cr, 19)
cb_med=cv2.medianBlur(cb, 19)

#Bandas originais e as mesmas com filtro aplicado
plt.figure("Sistema YCrCb")
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
plt.figure(" Obtenção da Mascara")
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
plt.figure(" Segmentação com as mascaras")
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
#Salvar a imagem de morango segmentada
########################################################################################################################
img_seg_new=cv2.cvtColor(img_seg_f,cv2.COLOR_BGR2RGB)
cv2.imwrite("1 A segmentada.jpg", img_seg_new)

#Apresentação da imagem segmentada
plt.figure("Imagem de morango segmentada")
plt.imshow(img_seg_f)
plt.title("Imagem segmentada")
plt.xticks([])
plt.yticks([])
plt.show()

########################################################################################################################
#DadosCom a utilização da biblioteca Scikit-Image é possível identificar o numero de objetos na imagem automaticamente.
#Além disso, esta mesma biblioteca, nos permite estimar inúmeras informações de cada objeto na imagem, como exemplo a área,
#  o perímetro, largura, medidas de cor e ainda permite selecionar e salvar cada objeto separadamente em uma nova imagem .


#Importar pacote
from skimage.measure import label, regionprops

###########################################################################
#Objetos
mascara=img_cB_1.copy()
cnts, h = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


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
      #print("Centroide", regiao[0].centroid)
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
#Criar um arquivo de TXT para salvar os dados obtidos.
########################################################################################################################
#Importar pacotes
from datetime import date
data_atual = date.today()
########################################################################################################################
#Alterar o nome do arquivo a cada nova imagem
with open('Resultados 1 A.txt', 'w') as arquivo:
      print("_"*60, file=arquivo)
      print(" ", file=arquivo)
      print("Análise de dados utilizando o programa Python", file=arquivo)
      print("Dados analisados em: ", data_atual, file=arquivo)
      print("Análise executada por: Silva, E. A.", file=arquivo)
      print(" ", file=arquivo)
      print("Arquivo com os dados obtidos com o pacote Scikit-Image", file=arquivo)
      print("_" * 60, file=arquivo)
      print('Número de objetos a serem apresentados: ', len(cnts), file=arquivo)
      print("=" * 60, file=arquivo)
      for (i, c) in enumerate(cnts):
            (x, y, w, h) = cv2.boundingRect(c)
            obj = img_cB_1[y:y + h, x:x + w]
            obj_rgb = img_seg_f[y:y + h, x:x + w]
            obj_bgr = cv2.cvtColor(obj_rgb, cv2.COLOR_RGBA2BGR)
            cv2.imwrite("s" + str(i + 1) + ".png", obj_bgr)
            cv2.imwrite('sb' + str(i + 1) + '.png', obj)

            regiao = regionprops(obj)
            print('Objeto', str(i + 1), file=arquivo)
            print('=' * 60, file=arquivo)
            #print("Dimensão da imagem", np.shape(obj), file=arquivo)
            #print('_' * 20, file=arquivo)
            print("Medidas_Fisicas", file=arquivo)
            print('_' * 20, file=arquivo)
            print("Centroide", regiao[0].centroid, file=arquivo)
            print('Comprimento_do_eixo_menor: ', regiao[0].minor_axis_length, file=arquivo)
            print('Comprimento_do_eixo_maior: ', regiao[0].major_axis_length, file=arquivo)
            #print('Razão: ', regiao[0].major_axis_length / regiao[0].minor_axis_length, file=arquivo)
            area = cv2.contourArea(c)
            print('Área: ', area, file=arquivo)
            print('Perímetro: ', cv2.arcLength(c, True), file=arquivo)

            #print('_' * 20, file=arquivo)
            print('Medidas_de_Cor', file=arquivo)
            #print('_' * 20, file=arquivo)
            min_val_r, max_val_r, min_loc_r, max_loc_r = cv2.minMaxLoc(obj_rgb[:, :, 0], mask=obj)
            print('Valor_Mínimo_no_R: ', min_val_r, file=arquivo)
            print('Valor_Máximo_no_R: ', max_val_r, file=arquivo)
            med_val_r = cv2.mean(obj_rgb[:, :, 0], mask=obj)
            print('Média_no_Vermelho: ', med_val_r, file=arquivo)

            min_val_g, max_val_g, min_loc_g, max_loc_g = cv2.minMaxLoc(obj_rgb[:, :, 1], mask=obj)
            print('Valor_Mínimo_no_G: ', min_val_g, file=arquivo)
            print('Valor_Máximo_no_G: ', max_val_g,  file=arquivo)
            med_val_g = cv2.mean(obj_rgb[:, :, 1], mask=obj)
            print('Média_no_Verde: ', med_val_g, file=arquivo)

            min_val_b, max_val_b, min_loc_b, max_loc_b = cv2.minMaxLoc(obj_rgb[:, :, 2], mask=obj)
            print('Valor_Mínimo_no_B: ', min_val_b,  file=arquivo)
            print('Valor_Máximo_no_B: ', max_val_b,  file=arquivo)
            med_val_b = cv2.mean(obj_rgb[:, :, 2], mask=obj)
            print('Média_no_Azul: ', med_val_b, file=arquivo)
            print('=' * 60, file=arquivo)
