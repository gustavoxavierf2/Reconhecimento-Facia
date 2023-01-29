'''
# criar ambiente virtual anaconda
# neste site(https://anaconda.org/conda-forge/dlib) procure as dependencias
Cmake( conda install cmake)/\
DLIB([ conda install -c conda-forge dlib],[ conda install -c "conda-forge/label/cf201901" dlib],
                                                            [ conda install -c "conda-forge/label/cf202003" dlib]) /\
NUMPY( pip install numpy==1.21.00)/\
OPENCV( conda install -c fastchan opencv)/\
FECE_RECOGNITION( conda install -c conda-forge face-recognition)
# instale pelo terminal do anaconda'''
import cv2
import face_recognition as fr
import numpy as np
from engine import get_rosto


imagens_conhecidas, nomes_rostos = get_rosto() #Atribui a estas variaveis os nomes conhecidos e rostos conhecidos
webcam = cv2.VideoCapture(0) #Inicia a webcam

while True: #loop infinito
    verificador, frame = webcam.read() #Le os dados da [webcam], e as variaveis [frame] e [verificador] recebem os seus returns
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #Converte o [frame] do padrao bgr para o rgb

    localizacao_rosto = fr.face_locations(rgb_frame, model='hog') #Localiza um rosto no [frame] com o padrao rgb
    rosto_webcam = fr.face_encodings(rgb_frame, localizacao_rosto,  model='small') #Captura os pontos de encodings do rosto,passando como parametro o [rgb_frame] e a [localizaçao_rosto]

    for (top, right, bottom, left), rosto_webcam in zip(localizacao_rosto,rosto_webcam):#    
        result = fr.compare_faces(imagens_conhecidas, rosto_webcam, tolerance=0.6)#Compara os rostos conhecidos com os rostos em formato de encodings da webcam, retorna um [boolean]
        print(result)
        
        proximidade_rostos = fr.face_distance(imagens_conhecidas, rosto_webcam) #Outro metodo que compara os rostos conhecidos com os rostos da webcam,baseando-se na distancia, [float] 
        melhor_proximidade= np.argmin(proximidade_rostos) #Faz o calculo da melhor proximidade
        
        if result[melhor_proximidade]: #Se a varivel [result](que e boolean) no indice de [melhor_proximidade] for true
            nome = nomes_rostos[melhor_proximidade] #[Nome] recebe o nome do rosto idenficado
        else:
            nome = "desconhecido" #Se nao for encontrado nenhum nome, [nome] recebe desconhecido
            
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2) #Cria um rentangulo vermeho no rosto identificado, o [2] e expessura do retanguo

        #Embaixo
        cv2.rectangle(frame, (left, bottom - 35), (right -30, bottom), (0, 0, 255), cv2.FILLED)#Cria a rebarba para inserir o nome
        font = cv2.FONT_HERSHEY_SIMPLEX #Fonte do texto

        #Texto
        cv2.putText(frame, nome, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 4) #Insere o nome do rosto no [frame]
        
        cv2.imshow("webbcan", frame) #Cria a janela, sendo "webbcan" o nome da janela
    if cv2.waitKey(10) == 27: #Se apertado a tecla [esq] encerra o loop
        break
    
webcam.release() #Desativa webcam
cv2.destroyAllWindows() #Fecha todas as janelas

            
             

    