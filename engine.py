import face_recognition as fr

def reconhece_rosto(url_imagem): #Funçao de reconhecimento facial
    imagem = fr.load_image_file(url_imagem, mode='RGB') #Carregamento da imagem
    rostos = fr.face_encodings(imagem, model="large") #Faz o reconhecimento do rosto, retornando os pontos de encodings de cada rosto
    if(len(rostos) > 0): #Se o tamanho da variavel [rostos] for maior que 0, existe um ou mais rosto na imagem 
        return True, rostos  #Retorna verdadeiro e os pontos de encodings da variavel [rostos]
    
    return False, [] #Caso não haja nenhum rosto na imagem retorna-se falso e um array vazio


def get_rosto(): #Funçao que retorna os rostos conhecidos, ou seja, os previamente inseridos aqui nesta funçao 
    rostos_conhecidos = [] #Array de rostos conhecidos
    nomes_rostos = [] #Array de nomes conhecidos, pertencentes a cada rosto conhecido
    
    rosto_conhecido = reconhece_rosto("./img/bill-gates.webp") #Carrega a imagem de parametro conhecido usando a funçao[reconhece_rosto]
    nomes_rostos.append("bill gates") #Ao carregar o rosto conhecido, carrega tbm no array [nomes_rostos] o nome pertencente a esta rosto, ou seja estao no mesmo indice dos arrays
    if(rosto_conhecido[0]): #Se o primeiro rosto for true
        rostos_conhecidos.append(rosto_conhecido[1][0]) #Acrescenta este rosto no array [rostos_conhecidos]
        
    rosto_conhecido = reconhece_rosto("./img/eu.jpeg") #Carrega a imagem de parametro conhecido usando a funçao[reconhece_rosto]
    nomes_rostos.append("gustavo X") #Ao carregar o rosto conhecido, carrega tbm no array [nomes_rostos] o nome pertencente a esta rosto, ou seja estao no mesmo indice dos arrays
    if(rosto_conhecido[0]): #Se o primeiro rosto for true
        rostos_conhecidos.append(rosto_conhecido[1][0]) #Acrescenta este rosto no array [rostos_conhecidos]
    
    return rostos_conhecidos, nomes_rostos #Retorna o array [rostos_conhecidos] e o nome pertencente a imagem