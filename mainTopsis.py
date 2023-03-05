from ortools.linear_solver import pywraplp
import json

S_MIN_GRADE = 1
S_MAX_GRADE = 5



#interestv1 será o melhor v1
# def interest_v1(m, o, ow, s, sw, maxValues, alpha):
    
    

#     #Desperdicio 
#     cpu =  (m[0] - o[0]) / (maxValues[0] - o[0]) * ow[0] if o[0] < maxValues[0] else 0
#     memory = (m[1] - o[1]) / (maxValues[1] - o[1]) * ow[1] if o[1] < maxValues[1] else 0
#     storage = (m[2] - o[2]) / (maxValues[2] - o[2]) * ow[2] if o[2] < maxValues[2] else 0
#     latency =  (m[3] - o[3]) / (maxValues[3] - o[3]) * ow[3] if o[3] > maxValues[3] else 0

#     # print("-------------------------------------------")
#     # print("CPU",cpu)
#     # print("Memory",memory)
#     # print("Storage",storage)
#     # print("Latency",latency)
#     # print("-------------------------------------------")

#     res_v1 = (cpu + memory + storage + latency) 
    
    
#     return res_v1


    #interestv2 será o melhor v2
# def interest_v2(m, o, ow, s, sw, maxValues, alpha):
    
      
#     #Beneficio subjetivo
#     availability = (m[4]-s[0])/(S_MAX_GRADE-S_MIN_GRADE)*sw[0]
#     autonomy = (m[5]-s[1])/(S_MAX_GRADE-S_MIN_GRADE)*sw[1]
#     reliability = (m[6]-s[2])/(S_MAX_GRADE-S_MIN_GRADE)*sw[2]
#     mobility = (m[7]-s[3])/(S_MAX_GRADE-S_MIN_GRADE)*sw[3]
    
    
#     # print("Availability",availability)
#     # print("Autonomy",autonomy)
#     # print("Reliability",reliability)
#     # print("Mobility",mobility)
#     # print("-------------------------------------------")

#     #alpha representa o peso para os subjetivos. Enquanto 1-alpha é o peso dos objetivos.

#     v2 = (availability + autonomy + reliability + mobility) 
#     #res = ((alpha*v2) - (1-alpha)*v1) 
#     res_v2 = v2
#     # print("V1",v1)
#     # print("V2",v2)
#     # print("Res",res)
#     # print("-------------------------------------------")
#     # print("")
#     # print("")

#     return res_v2

    #interestv2racional será o melhor v2 racional
#def interest_v2racional(m, o, ow, s, sw, maxValues, alpha):
    
    #Desperdicio 
    # cpu =  (m[0] - o[0]) / (maxValues[0] - o[0]) * ow[0] if o[0] < maxValues[0] else 0
    # memory = (m[1] - o[1]) / (maxValues[1] - o[1]) * ow[1] if o[1] < maxValues[1] else 0
    # storage = (m[2] - o[2]) / (maxValues[2] - o[2]) * ow[2] if o[2] < maxValues[2] else 0
    # latency =  (o[3] - m[3]) / (maxValues[3] - o[3]) * ow[3] if o[3] < maxValues[3] else 0

    # print("-------------------------------------------")
    # print("CPU",cpu)
    # print("Memory",memory)
    # print("Storage",storage)
    # print("Latency",latency)
    # print("-------------------------------------------")

    #v1 = (cpu + memory + storage + latency) 
    
    #Beneficio subjetivo
    # availability = abs((m[4]-s[0])/(S_MAX_GRADE-S_MIN_GRADE)*sw[0])
    # autonomy = abs((m[5]-s[1])/(S_MAX_GRADE-S_MIN_GRADE)*sw[1])
    # reliability = abs((m[6]-s[2])/(S_MAX_GRADE-S_MIN_GRADE)*sw[2])
    # mobility = abs((m[7]-s[3])/(S_MAX_GRADE-S_MIN_GRADE)*sw[3])
    
    
    # print("Availability",availability)
    # print("Autonomy",autonomy)
    # print("Reliability",reliability)
    # print("Mobility",mobility)
    # print("-------------------------------------------")

    #alpha representa o peso para os subjetivos. Enquanto 1-alpha é o peso dos objetivos.

    # v2 = (availability + autonomy + reliability + mobility) 
    # #res = ((alpha*v2) - (1-alpha)*v1) 
    # res_v2racional = v2
    # # print("V1",v1)
    # print("V2",v2)
    # print("Res",res)
    # print("-------------------------------------------")
    # print("")
    # print("")

   # return res_v2racional



def solution():
    #m, o, ow, s, sw, available_instances, required_instance, maxValues, alpha


    # solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    json_importado='{"m": [ [32, 204, 4438, 941, 4, 3, 2, 3], [38, 357, 2730, 114, 1, 5, 1, 3], [36, 454, 2922, 367, 4, 2, 1, 1], [25, 249, 8270, 3257, 1, 2, 3, 1], [42, 245, 7648, 930, 5, 1, 2, 4], [5, 233, 3858, 631, 5, 2, 1, 2], [46, 223, 8184, 903, 4, 1, 1, 1], [10, 376, 4099, 490, 1, 2, 3, 4], [12, 268, 3737, 624, 1, 3, 3, 1], [14, 434, 7298, 1775, 4, 3, 1, 2], [33, 58, 8408, 261, 4, 2, 2, 1], [40, 86, 5071, 3148, 5, 1, 3, 4], [22, 172, 3406, 2604, 4, 2, 2, 4], [42, 371, 6057, 1418, 5, 2, 1, 2], [31, 100, 2567, 689, 4, 5, 2, 3], [48, 119, 7237, 2619, 5, 2, 4, 1], [32, 403, 5540, 3856, 4, 4, 3, 3], [35, 225, 7043, 4725, 5, 3, 3, 4]], "o": [4, 16, 2000, 4000], "ow": [0.125, 0.125, 0.125, 0.125], "s": [5, 2, 1, 3], "sw": [0.125, 0.125, 0.125, 0.125], "maxValues": [50, 500, 9993, 4868]}'


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

        

        #for i in range(0,TOTALM):
         #   if maquinas[i][0]>=o[0] and maquinas[i][1]>=o[1] and maquinas[i][2]>=o[2] and maquinas[i][3]<=o[3]:
          #      m.append([maquinas[i][0], maquinas[i][1], maquinas[i][2], maquinas[i][3], maquinas[i][4], maquinas[i][5], maquinas[i][6], maquinas[i][7]])





        #Parameters
        M = len(m)
        N = len(o)+len(s)

        # #Decision Variables   
        # # A = [solver.BoolVar('A%d'%(i)) for i in range(0,M)]

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

        vetor_grau_ideal = []
        vetor_grau_pior = []
        vetor_simetria = []
        


            
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
            cpu = (m[i][0])/normal_cpu*ow[0]
            vetor_normal_cpu.append(cpu)

            mem = (m[i][1])/normal_mem*ow[1]
            vetor_normal_mem.append(mem)

            storage = (m[i][2])/normal_storage*ow[2]
            vetor_normal_storage.append(storage)

            latencia = (m[i][3])/normal_latencia*ow[3]
            vetor_normal_latencia.append(latencia)

            availability = (m[i][4])/normal_availability*sw[0]
            vetor_normal_availability.append(availability)

            autonomy = (m[i][5])/normal_autonomy*sw[1]
            vetor_normal_autonomy.append(autonomy)

            reliability = (m[i][6])/normal_reliability*sw[2]
            vetor_normal_reliability.append(reliability)

            mobility = (m[i][7])/normal_mobility*sw[3]
            vetor_normal_mobility.append(mobility)


        ideal_cpu = max(vetor_normal_cpu)
        pior_cpu = min(vetor_normal_cpu)

        ideal_mem = max(vetor_normal_mem)    
        pior_mem = min(vetor_normal_mem)  

        ideal_storage = max(vetor_normal_storage)    
        pior_storage = min(vetor_normal_storage) 

        ideal_latencia = min(vetor_normal_latencia)    
        pior_latencia = max(vetor_normal_latencia) 

        ideal_availability = max(vetor_normal_availability)    
        pior_availability = min(vetor_normal_availability) 

        ideal_autonomy = max(vetor_normal_autonomy)    
        pior_autonomy = min(vetor_normal_autonomy) 

        ideal_reliability = max(vetor_normal_reliability)    
        pior_reliability = min(vetor_normal_reliability) 

        ideal_mobility = max(vetor_normal_mobility)    
        pior_mobility = min(vetor_normal_mobility) 


        for i in range(0,M):
            grau_ideal = ((vetor_normal_cpu[i]-ideal_cpu)**2 + (vetor_normal_mem[i]-ideal_mem)**2 + (vetor_normal_storage[i]-ideal_storage)**2 + (vetor_normal_latencia[i]-ideal_latencia)**2 + (vetor_normal_availability[i]-ideal_availability)**2 + (vetor_normal_autonomy[i]-ideal_autonomy)**2 + (vetor_normal_reliability[i]-ideal_reliability)**2 + (vetor_normal_mobility[i]-ideal_mobility)**2)
            grau_ideal =grau_ideal ** (1/2)
            vetor_grau_ideal.append(grau_ideal)

            grau_pior = ((vetor_normal_cpu[i]-pior_cpu)**2 + (vetor_normal_mem[i]-pior_mem)**2 + (vetor_normal_storage[i]-pior_storage)**2 + (vetor_normal_latencia[i]-pior_latencia)**2 + (vetor_normal_availability[i]-pior_availability)**2 + (vetor_normal_autonomy[i]-pior_autonomy)**2 + (vetor_normal_reliability[i]-pior_reliability)**2 + (vetor_normal_mobility[i]-pior_mobility)**2)
            grau_pior =grau_pior ** (1/2)
            vetor_grau_pior.append(grau_pior)

            simetria = vetor_grau_pior[i]/(vetor_grau_pior[i]+vetor_grau_ideal[i])
            vetor_simetria.append(simetria)

        for i in range(0,M):
            if vetor_simetria[i] == max(vetor_simetria):
                #print("ALGORITMO TOPSIS")
                #print("Maquina %d selecionada"%(i+1))
                if m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
                    print("Topsis; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_simetria[i]))
                else:
                    print("Máquina escolhida não é válida")
                #print("######################################")

        
    ##########################################################################################

        #ALGORITMO DA FORÇA BRUTA

        #print("ALGORITMO DA FORÇA BRUTA")
        
        # encontrado = 0

        # for i in range(0, M):
        #     if encontrado==0:
        #         if m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3] and m[i][4]>=s[0] and m[i][5]>=s[1] and m[i][6]>=s[2] and m[i][7]>=s[3]:
        #             #print("Maquina %d selecionada"%(i+1))
        #             print("Força Bruta; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
        #             encontrado = 1

        # if encontrado==0:
        #     print("Nenhuma máquina selecionada pelo Força Bruta no dataset %d"%(dataset))

solution()