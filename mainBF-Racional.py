from ortools.linear_solver import pywraplp
import json

from scipy import stats
import numpy as np

S_MIN_GRADE = 1
S_MAX_GRADE = 5



def solution():
    #m, o, ow, s, sw, available_instances, required_instance, maxValues, alpha


    #solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    #JSON USADOS NO TESTE
    #com a primeira máquina 
    #json_importado='{"m": [ [4, 16, 2000, 4000, 5, 2, 1, 3], [32, 204, 4438, 941, 4, 3, 2, 3], [32, 331, 3251, 403, 3, 3, 4, 4], [38, 357, 2730, 114, 1, 5, 1, 3], [36, 454, 2922, 367, 4, 2, 1, 1], [25, 249, 8270, 3257, 1, 2, 3, 1], [42, 245, 7648, 930, 5, 1, 2, 4], [5, 233, 3858, 631, 5, 2, 1, 2], [46, 223, 8184, 903, 4, 1, 1, 1], [10, 376, 4099, 490, 1, 2, 3, 4], [12, 268, 3737, 624, 1, 3, 3, 1], [14, 434, 7298, 1775, 4, 3, 1, 2], [33, 58, 8408, 261, 4, 2, 2, 1], [40, 86, 5071, 3148, 5, 1, 3, 4], [22, 172, 3406, 2604, 4, 2, 2, 4], [42, 371, 6057, 1418, 5, 2, 1, 2], [48, 119, 7237, 2619, 5, 2, 4, 1], [32, 403, 5540, 3856, 4, 4, 3, 3], [35, 225, 7043, 4725, 5, 3, 3, 4], [20, 447, 1369, 427, 2, 2, 4, 5] ], "o": [4, 16, 2000, 4000], "ow": [0.25, 0.25, 0.25, 0.25], "s": [5, 2, 1, 3], "sw": [0.25, 0.25, 0.25, 0.25], "maxValues": [48, 454, 8408, 4725]}'
    
    #Usado na escrita do artigo
    #json_importado='{"m": [ [32, 204, 4438, 941, 4, 3, 2, 3], [32, 331, 1251, 403, 3, 3, 4, 4], [38, 357, 2730, 114, 1, 5, 1, 3], [36, 454, 2922, 367, 4, 2, 1, 1], [25, 249, 8270, 3257, 1, 2, 3, 1], [42, 245, 7648, 930, 5, 1, 2, 4], [5, 233, 3858, 631, 5, 2, 1, 2], [46, 223, 8184, 903, 4, 1, 1, 1], [10, 376, 4099, 490, 1, 2, 3, 4], [12, 268, 3737, 624, 1, 3, 3, 1], [14, 434, 7298, 1775, 4, 3, 1, 2], [33, 58, 8408, 261, 4, 2, 2, 1], [40, 86, 5071, 3148, 5, 1, 3, 4], [22, 172, 3406, 2604, 4, 2, 2, 4], [42, 371, 6057, 1418, 5, 2, 1, 2], [31, 100, 2567, 689, 4, 5, 2, 3], [48, 119, 7237, 2619, 5, 2, 4, 1], [32, 403, 5540, 3856, 4, 4, 3, 3], [35, 225, 7043, 4725, 5, 3, 3, 4], [20, 447, 1369, 427, 2, 2, 4, 5] ], "o": [4, 16, 2000, 4000], "ow": [0.125, 0.125, 0.125, 0.125], "s": [5, 2, 1, 3], "sw": [0.125, 0.125, 0.125, 0.125], "maxValues": [50, 500, 9993, 4868]}'

    for i in range(1,1001):
        nome = '/home/joao/Documentos/unb-fog/datasets/'+str(i)+'.txt'
        # print('####################################')
        # print(nome)
        # print('####################################')

        dataset = i

        arquivo = open(nome, 'r') 
        #arquivo = open('/home/joao/Documentos/unb-fog/datasets/995.txt', 'r')
        conteudo = arquivo.read() 

        json_importado=conteudo
        
      
        
        vimported = json.loads(json_importado)
        m = vimported['m'] 
        #maquinas = vimported['m'] 
        o = vimported['o'] 
        ow = vimported['ow'] 
        s = vimported['s'] 
        sw = vimported['sw'] 
        maxValues = vimported['maxValues']
        alpha = 0
        #m = []

        #TOTALM = len(maquinas)

        

        # for i in range(0,TOTALM):
        #     if maquinas[i][0]>=o[0] and maquinas[i][1]>=o[1] and maquinas[i][2]>=o[2] and maquinas[i][3]<=o[3]:
        #         m.append([maquinas[i][0], maquinas[i][1], maquinas[i][2], maquinas[i][3], maquinas[i][4], maquinas[i][5], maquinas[i][6], maquinas[i][7]])



        #Parameters
        M = len(m)
        N = len(o)+len(s)



        #Valores normalizados
        normal_cpu = 0
        normal_mem = 0
        normal_storage = 0
        normal_latencia = 0
        normal_availability = 0
        normal_autonomy = 0 
        normal_reliability = 0
        normal_mobility = 0
        
        #Vetores Normalizados
        vetor_normal_cpu = []
        vetor_normal_mem = []
        vetor_normal_storage = []
        vetor_normal_latencia = []
        vetor_normal_availability = []
        vetor_normal_autonomy = []
        vetor_normal_reliability = []
        vetor_normal_mobility = []

        vetor_interessev1 = []
        vetor_interessev2 = []
        vetor_interessev2racional = []

        vetor_total_otimo = []
        vetor_total_racional = []

        
        #Restrições

        if(ow[0]+ow[1]+ow[2]+ow[3]+sw[0]+sw[1]+sw[2]+sw[3]!=1):
            print("########################################")
            print("########################################")
            print("ATENÇÃO:Pesos errados")
            print("########################################")
            print("########################################")

            
        #Calculo da Normalizacao
        for i in range(0,M):
            normal_cpu = normal_cpu + (m[i][0]**2)
            normal_mem = normal_mem + (m[i][1]**2)
            normal_storage = normal_storage + (m[i][2]**2)
            normal_latencia = normal_latencia + (m[i][3]**2)
            normal_availability = normal_availability + (m[i][4]**2)
            normal_autonomy = normal_autonomy + (m[i][5]**2) 
            normal_reliability = normal_reliability + (m[i][6]**2)
            normal_mobility = normal_mobility + (m[i][7]**2)


        normal_cpu = normal_cpu ** (1/2)
        normal_mem = normal_mem ** (1/2)
        normal_storage = normal_storage ** (1/2)
        normal_latencia = normal_latencia ** (1/2)
        normal_availability = normal_availability ** (1/2)
        normal_autonomy = normal_autonomy ** (1/2)
        normal_reliability = normal_reliability ** (1/2)
        normal_mobility = normal_mobility ** (1/2)   
        

        #Geração de Vetores Normalizados
        for i in range(0,M):
            cpu = (m[i][0]-o[0])/normal_cpu*ow[0]
            vetor_normal_cpu.append(cpu)

            mem = (m[i][1]-o[1])/normal_mem*ow[1]
            vetor_normal_mem.append(mem)

            storage = (m[i][2]-o[2])/normal_storage*ow[2]
            vetor_normal_storage.append(storage)

            latencia = -1*((m[i][3]-o[3])/normal_latencia*ow[3])
            vetor_normal_latencia.append(latencia)

            availability = (m[i][4]-s[0])/normal_availability*sw[0]
            vetor_normal_availability.append(availability)

            autonomy = (m[i][5]-s[1])/normal_autonomy*sw[1]
            vetor_normal_autonomy.append(autonomy)

            reliability = (m[i][6]-s[2])/normal_reliability*sw[2]
            vetor_normal_reliability.append(reliability)

            mobility = (m[i][7]-s[3])/normal_mobility*sw[3]
            vetor_normal_mobility.append(mobility)

            vetor_interessev1.append(vetor_normal_cpu[i] + vetor_normal_mem[i] + vetor_normal_storage[i] + vetor_normal_latencia[i])
            
            vetor_interessev2.append(vetor_normal_availability[i] + vetor_normal_autonomy[i] + vetor_normal_reliability[i] + vetor_normal_mobility[i])
            
            vetor_interessev2racional.append(abs(vetor_normal_availability[i]) + abs(vetor_normal_autonomy[i]) + abs(vetor_normal_reliability[i]) + abs(vetor_normal_mobility[i]))

            vetor_total_otimo.append(vetor_interessev1[i] + vetor_interessev2[i])

            vetor_total_racional.append(vetor_interessev1[i] + vetor_interessev2racional[i])


        score = max(vetor_total_racional)
        escolhida = 0
        existe = 0

        

        for i in range(0, M):
            if m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3] and m[i][4]>=s[0] and m[i][5]>=s[1] and m[i][6]>=s[2] and m[i][7]>=s[3]:
                if score > vetor_total_racional[i]:
                    score = vetor_total_racional[i]
                    escolhida = i
                    existe = 1
        
        if existe==1:
            print("Força Bruta; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d"%(dataset, (m[escolhida][0]-o[0]), (m[escolhida][1]-o[1]), (m[escolhida][2]-o[2]), (m[escolhida][3]-o[3]), (m[escolhida][4]-s[0]), (m[escolhida][5]-s[1]), (m[escolhida][6]-s[2]), (m[escolhida][7]-s[3])))
        else:
            print("Nenhuma máquina selecionada pelo Força Bruta no dataset %d"%(dataset))
    
   
    
solution()