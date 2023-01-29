import face_recognition as fr 
from engine import reconhece_rosto,  get_rosto


imagem = reconhece_rosto("./img/bill-gates.webp") #Carrega a imagem de input desconhecida

if(imagem[0]):#Se o primeiro rosto for true
   
    rosto_desconhecido = imagem[1][0] #A imagem desconhecida contem 2 retornos da funçao [reconhece_face],o [1] e se o rosto e true ou false  
    imagens_conhecidas, nomes_rostos = get_rosto() #Atribui a estas variaveis, os nomes e rostos conhecidos
    result = fr.compare_faces(imagens_conhecidas,rosto_desconhecido) #Compara os rostos
    print(result) #Printa o resultado
    
    for i in range(len(imagens_conhecidas)): #Percorre o array de rostos conhecidos 
        result = result[i] #Atribui a variavel result o proprio result com o indice [i] em questao,para que possamos verificar um a um
        if(result): #Se result for true
            print("rosto do", nomes_rostos[i], "foi reconhecido") #Nome do rosto com o indice em questao
        else:
            print("não encontrei nenhum rosto compativel no database!")
else:
    print("não ha rostos na foto em questao!")