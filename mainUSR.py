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

    for i in range(1,2):
        nome = '/home/joao/Documentos/unb-fog/datasets/UsadoArtigo.txt'
        # nome = '/home/joao/Documentos/unb-fog/datasets/'+str(i)+'.txt'
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
        maquinas = vimported['m'] 
        o = vimported['o'] 
        ow = vimported['ow'] 
        s = vimported['s'] 
        sw = vimported['sw'] 
        maxValues = vimported['maxValues']
        alpha = 0
        #m = []

        # TOTALM = len(maquinas)

        

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

        vetor_percentil_1_otimo = []
        vetor_percentil_2_otimo = []
        vetor_percentil_3_otimo = []
        vetor_percentil_4_otimo = []
        vetor_percentil_5_otimo = []
        vetor_percentil_6_otimo = []
        vetor_percentil_7_otimo = []
        vetor_percentil_8_otimo = []
        vetor_percentil_9_otimo = []
        vetor_percentil_10_otimo = []

        # vetor_percentil_1_racional = []
        # vetor_percentil_2_racional = []
        # vetor_percentil_3_racional = []
        # vetor_percentil_4_racional = []
        # vetor_percentil_5_racional = []
        # vetor_percentil_6_racional = []
        # vetor_percentil_7_racional = []
        # vetor_percentil_8_racional = []
        # vetor_percentil_9_racional = []
        # vetor_percentil_10_racional = []
        
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
            print(vetor_total_otimo[i])
            #vetor_total_racional.append(vetor_interessev1[i] + vetor_interessev2racional[i])

        #Percentil Ótimo
        percentile_1_otimo=np.percentile(vetor_total_otimo, 10)
        percentile_2_otimo=np.percentile(vetor_total_otimo, 20)
        percentile_3_otimo=np.percentile(vetor_total_otimo, 30)
        percentile_4_otimo=np.percentile(vetor_total_otimo, 40)
        percentile_5_otimo=np.percentile(vetor_total_otimo, 50)
        percentile_6_otimo=np.percentile(vetor_total_otimo, 60)
        percentile_7_otimo=np.percentile(vetor_total_otimo, 70)
        percentile_8_otimo=np.percentile(vetor_total_otimo, 80)
        percentile_9_otimo=np.percentile(vetor_total_otimo, 90)

        # #Percentil Racional
        # percentile_1_racional=np.percentile(vetor_total_racional, 100-10)
        # percentile_2_racional=np.percentile(vetor_total_racional, 100-20)
        # percentile_3_racional=np.percentile(vetor_total_racional, 100-30)
        # percentile_4_racional=np.percentile(vetor_total_racional, 100-40)
        # percentile_5_racional=np.percentile(vetor_total_racional, 100-50)
        # percentile_6_racional=np.percentile(vetor_total_racional, 100-60)
        # percentile_7_racional=np.percentile(vetor_total_racional, 100-70)
        # percentile_8_racional=np.percentile(vetor_total_racional, 100-80)
        # percentile_9_racional=np.percentile(vetor_total_racional, 100-90)
        # percentile_10_racional=np.percentile(vetor_total_racional, 100-100)





        for i in range(0, M):
            if vetor_total_otimo[i]<=percentile_1_otimo:
                vetor_percentil_1_otimo.append(vetor_total_otimo[i])
            else:
                if vetor_total_otimo[i]<=percentile_2_otimo:
                    vetor_percentil_2_otimo.append(vetor_total_otimo[i])
                else:
                    if vetor_total_otimo[i]<=percentile_3_otimo:
                        vetor_percentil_3_otimo.append(vetor_total_otimo[i])
                    else:
                        if vetor_total_otimo[i]<=percentile_4_otimo:
                            vetor_percentil_4_otimo.append(vetor_total_otimo[i])
                        else:
                            if vetor_total_otimo[i]<=percentile_5_otimo:
                                vetor_percentil_5_otimo.append(vetor_total_otimo[i])
                            else:
                                if vetor_total_otimo[i]<=percentile_6_otimo:
                                    vetor_percentil_6_otimo.append(vetor_total_otimo[i])
                                else:
                                    if vetor_total_otimo[i]<=percentile_7_otimo:
                                        vetor_percentil_7_otimo.append(vetor_total_otimo[i])
                                    else:
                                        if vetor_total_otimo[i]<=percentile_8_otimo:
                                            vetor_percentil_8_otimo.append(vetor_total_otimo[i])
                                        else:
                                            if vetor_total_otimo[i]<=percentile_9_otimo:
                                                vetor_percentil_9_otimo.append(vetor_total_otimo[i])
                                            else:
                                                vetor_percentil_10_otimo.append(vetor_total_otimo[i])

        # for i in range(0, M):
        #     if vetor_total_racional[i]>=percentile_1_racional:
        #         vetor_percentil_1_racional.append(vetor_total_racional[i])
        #     else:
        #         if vetor_total_racional[i]>=percentile_2_racional:
        #             vetor_percentil_2_racional.append(vetor_total_racional[i])
        #         else:
        #             if vetor_total_racional[i]>=percentile_3_racional:
        #                 vetor_percentil_3_racional.append(vetor_total_racional[i])
        #             else:
        #                 if vetor_total_racional[i]>=percentile_4_racional:
        #                     vetor_percentil_4_racional.append(vetor_total_racional[i])
        #                 else:
        #                     if vetor_total_racional[i]>=percentile_5_racional:
        #                         vetor_percentil_5_racional.append(vetor_total_racional[i])
        #                     else:
        #                         if vetor_total_racional[i]>=percentile_6_racional:
        #                             vetor_percentil_6_racional.append(vetor_total_racional[i])
        #                         else:
        #                             if vetor_total_racional[i]>=percentile_7_racional:
        #                                 vetor_percentil_7_racional.append(vetor_total_racional[i])
        #                             else:
        #                                 if vetor_total_racional[i]>=percentile_8_racional:
        #                                     vetor_percentil_8_racional.append(vetor_total_racional[i])
        #                                 else:
        #                                     if vetor_total_racional[i]>=percentile_9_racional:
        #                                         vetor_percentil_9_racional.append(vetor_total_racional[i])
        #                                     else:
        #                                         vetor_percentil_10_racional.append(vetor_total_racional[i])
                                                

        


        #######Objective Function VETOR ÓTIMO COM ALPHA DE 1 A 10 #######
        #print("###############OTIMAS ALPHAS##############")

        vetor_percentil_1_otimo.sort(reverse = True)
        vetor_percentil_2_otimo.sort(reverse = True)
        vetor_percentil_3_otimo.sort(reverse = True)
        vetor_percentil_4_otimo.sort(reverse = True)
        vetor_percentil_5_otimo.sort(reverse = True)
        vetor_percentil_6_otimo.sort(reverse = True)
        vetor_percentil_7_otimo.sort(reverse = True)
        vetor_percentil_8_otimo.sort(reverse = True)
        vetor_percentil_9_otimo.sort(reverse = True)
        vetor_percentil_10_otimo.sort(reverse = True)



        achou = 0
        for j in range(0, len(vetor_percentil_1_otimo)):
            if achou == 0:
                for i in range(0, M):
                    if vetor_total_otimo[i] == vetor_percentil_1_otimo[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
                        print("Maquina %d selecionada para alpha 1 ótimo"%(i+1))
                        #print("Score: %f"%(vetor_total_otimo[i]))
                        #print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
                        print("Alpha 01 ótimo; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_otimo[i]))
                        #print("########################################")
                        achou = 1

        
        achou = 0
        for j in range(0, len(vetor_percentil_2_otimo)):
            if achou == 0:
                for i in range(0, M):
                    if vetor_total_otimo[i] == vetor_percentil_2_otimo[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
                        print("Maquina %d selecionada para alpha 2 ótimo"%(i+1))
                        # print("Score: %f"%(vetor_total_otimo[i]))
                        # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
                        # print("########################################")
                        print("Alpha 02 ótimo; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_otimo[i]))
                        achou = 1

        achou = 0
        for j in range(0, len(vetor_percentil_3_otimo)):
            if achou == 0:
                for i in range(0, M):
                    if vetor_total_otimo[i] == vetor_percentil_3_otimo[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
                        print("Maquina %d selecionada para alpha 3 ótimo"%(i+1))
                        # print("Score: %f"%(vetor_total_otimo[i]))
                        # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
                        # print("########################################")
                        print("Alpha 03 ótimo; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_otimo[i]))
                        achou = 1

        achou = 0
        for j in range(0, len(vetor_percentil_4_otimo)):
            if achou == 0:
                for i in range(0, M):
                    if vetor_total_otimo[i] == vetor_percentil_4_otimo[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
                        print("Maquina %d selecionada para alpha 4 ótimo"%(i+1))
                        # print("Score: %f"%(vetor_total_otimo[i]))
                        # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
                        # print("########################################")
                        print("Alpha 04 ótimo; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_otimo[i]))
                        achou = 1

        achou = 0
        for j in range(0, len(vetor_percentil_5_otimo)):
            if achou == 0:
                for i in range(0, M):
                    if vetor_total_otimo[i] == vetor_percentil_5_otimo[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
                        print("Maquina %d selecionada para alpha 5 ótimo"%(i+1))
                        # print("Score: %f"%(vetor_total_otimo[i]))
                        # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
                        # print("########################################")
                        print("Alpha 05 ótimo; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_otimo[i]))
                        achou = 1

        achou = 0
        for j in range(0, len(vetor_percentil_6_otimo)):
            if achou == 0:
                for i in range(0, M):
                    if vetor_total_otimo[i] == vetor_percentil_6_otimo[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
                        print("Maquina %d selecionada para alpha 6 ótimo"%(i+1))
                        # print("Score: %f"%(vetor_total_otimo[i]))
                        # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
                        # print("########################################")
                        print("Alpha 06 ótimo; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_otimo[i]))
                        achou = 1

        achou = 0
        for j in range(0, len(vetor_percentil_7_otimo)):
            if achou == 0:
                for i in range(0, M):
                    if vetor_total_otimo[i] == vetor_percentil_7_otimo[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
                        print("Maquina %d selecionada para alpha 7 ótimo"%(i+1))
                        # print("Score: %f"%(vetor_total_otimo[i]))
                        # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
                        # print("########################################")
                        print("Alpha 07 ótimo; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_otimo[i]))
                        achou = 1

        achou = 0
        for j in range(0, len(vetor_percentil_8_otimo)):
            if achou == 0:
                for i in range(0, M):
                    if vetor_total_otimo[i] == vetor_percentil_8_otimo[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
                        print("Maquina %d selecionada para alpha 8 ótimo"%(i+1))
                        # print("Score: %f"%(vetor_total_otimo[i]))
                        # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
                        # print("########################################")
                        print("Alpha 08 ótimo; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_otimo[i]))
                        achou = 1

        achou = 0
        for j in range(0, len(vetor_percentil_9_otimo)):
            if achou == 0:
                for i in range(0, M):
                    if vetor_total_otimo[i] == vetor_percentil_9_otimo[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
                        print("Maquina %d selecionada para alpha 9 ótimo"%(i+1))
                        # print("Score: %f"%(vetor_total_otimo[i]))
                        # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
                        # print("########################################")
                        print("Alpha 09 ótimo; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_otimo[i]))
                        achou = 1


        achou = 0
        for j in range(0, len(vetor_percentil_10_otimo)):
            if achou == 0:
                for i in range(0, M):
                    if vetor_total_otimo[i] == vetor_percentil_10_otimo[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
                        print("Maquina %d selecionada para alpha 10 ótimo"%(i+1))
                        # print("Score: %f"%(vetor_total_otimo[i]))
                        # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
                        # print("########################################")
                        print("Alpha 10 ótimo; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_otimo[i]))
                        achou = 1
        
        #######Objective Function VETOR RACIONAL COM ALPHA DE 1 A 10 #######
        #print("###############RACIONAIS ALPHAS##############")

        # vetor_percentil_1_racional.sort()
        # vetor_percentil_2_racional.sort()
        # vetor_percentil_3_racional.sort()
        # vetor_percentil_4_racional.sort()
        # vetor_percentil_5_racional.sort()
        # vetor_percentil_6_racional.sort()
        # vetor_percentil_7_racional.sort()
        # vetor_percentil_8_racional.sort()
        # vetor_percentil_9_racional.sort()
        # vetor_percentil_10_racional.sort()


        # achou = 0
        # for j in range(0, len(vetor_percentil_1_racional)):
        #     if achou == 0:
        #         for i in range(0, M):
        #             if vetor_total_racional[i] == vetor_percentil_1_racional[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
        #                 # print("Maquina %d selecionada para alpha 1 racional"%(i+1))
        #                 # print("Score: %f"%(vetor_total_racional[i]))
        #                 # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
        #                 # print("########################################")
        #                 print("Alpha 01 racional; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_racional[i]))
        #                 achou = 1

        
        # achou = 0
        # for j in range(0, len(vetor_percentil_2_racional)):
        #     if achou == 0:
        #         for i in range(0, M):
        #             if vetor_total_racional[i] == vetor_percentil_2_racional[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
        #                 # print("Maquina %d selecionada para alpha 2 racional"%(i+1))
        #                 # print("Score: %f"%(vetor_total_racional[i]))
        #                 # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
        #                 # print("########################################")
        #                 print("Alpha 02 racional; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_racional[i]))
        #                 achou = 1

        # achou = 0
        # for j in range(0, len(vetor_percentil_3_racional)):
        #     if achou == 0:
        #         for i in range(0, M):
        #             if vetor_total_racional[i] == vetor_percentil_3_racional[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
        #                 # print("Maquina %d selecionada para alpha 3 racional"%(i+1))
        #                 # print("Score: %f"%(vetor_total_racional[i]))
        #                 # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
        #                 # print("########################################")
        #                 print("Alpha 03 racional; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_racional[i]))
        #                 achou = 1

        # achou = 0
        # for j in range(0, len(vetor_percentil_4_racional)):
        #     if achou == 0:
        #         for i in range(0, M):
        #             if vetor_total_racional[i] == vetor_percentil_4_racional[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
        #                 # print("Maquina %d selecionada para alpha 4 racional"%(i+1))
        #                 # print("Score: %f"%(vetor_total_racional[i]))
        #                 # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
        #                 # print("########################################")
        #                 print("Alpha 04 racional; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_racional[i]))
        #                 achou = 1

        # achou = 0
        # for j in range(0, len(vetor_percentil_5_racional)):
        #     if achou == 0:
        #         for i in range(0, M):
        #             if vetor_total_racional[i] == vetor_percentil_5_racional[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
        #                 # print("Maquina %d selecionada para alpha 5 racional"%(i+1))
        #                 # print("Score: %f"%(vetor_total_racional[i]))
        #                 # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
        #                 # print("########################################")
        #                 print("Alpha 05 racional; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_racional[i]))
        #                 achou = 1

        # achou = 0
        # for j in range(0, len(vetor_percentil_6_racional)):
        #     if achou == 0:
        #         for i in range(0, M):
        #             if vetor_total_racional[i] == vetor_percentil_6_racional[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
        #                 # print("Maquina %d selecionada para alpha 6 racional"%(i+1))
        #                 # print("Score: %f"%(vetor_total_racional[i]))
        #                 # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
        #                 # print("########################################")
        #                 print("Alpha 06 racional; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_racional[i]))
        #                 achou = 1

        # achou = 0
        # for j in range(0, len(vetor_percentil_7_racional)):
        #     if achou == 0:
        #         for i in range(0, M):
        #             if vetor_total_racional[i] == vetor_percentil_7_racional[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
        #                 # print("Maquina %d selecionada para alpha 7 racional"%(i+1))
        #                 # print("Score: %f"%(vetor_total_racional[i]))
        #                 # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
        #                 #print("########################################")
        #                 print("Alpha 07 racional; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_racional[i]))
        #                 achou = 1

        # achou = 0
        # for j in range(0, len(vetor_percentil_8_racional)):
        #     if achou == 0:
        #         for i in range(0, M):
        #             if vetor_total_racional[i] == vetor_percentil_8_racional[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
        #                 # print("Maquina %d selecionada para alpha 8 racional"%(i+1))
        #                 # print("Score: %f"%(vetor_total_racional[i]))
        #                 # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
        #                 # print("########################################")
        #                 print("Alpha 08 racional; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_racional[i]))
        #                 achou = 1

        # achou = 0
        # for j in range(0, len(vetor_percentil_9_racional)):
        #     if achou == 0:
        #         for i in range(0, M):
        #             if vetor_total_racional[i] == vetor_percentil_9_racional[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
        #                 # print("Maquina %d selecionada para alpha 9 racional"%(i+1))
        #                 # print("Score: %f"%(vetor_total_racional[i]))
        #                 # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
        #                 # print("########################################")
        #                 print("Alpha 09 racional; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_racional[i]))
        #                 achou = 1


        # achou = 0
        # for j in range(0, len(vetor_percentil_10_racional)):
        #     if achou == 0:
        #         for i in range(0, M):
        #             if vetor_total_racional[i] == vetor_percentil_10_racional[j] and m[i][0]>=o[0] and m[i][1]>=o[1] and m[i][2]>=o[2] and m[i][3]<=o[3]:
        #                 # print("Maquina %d selecionada para alpha 10 racional"%(i+1))
        #                 # print("Score: %f"%(vetor_total_racional[i]))
        #                 # print("Diferença: CPU %f, Memoria %f, Storage %f, Latencia %f, Availability %d, Autonomy %d, Reliability %d, Mobility %d"%((m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3])))
        #                 # print("########################################")
        #                 print("Alpha 10 racional; Dataset %d; %d; %d; %d; %d; %d; %d; %d; %d; %f"%(dataset, (m[i][0]-o[0]), (m[i][1]-o[1]), (m[i][2]-o[2]), (m[i][3]-o[3]), (m[i][4]-s[0]), (m[i][5]-s[1]), (m[i][6]-s[2]), (m[i][7]-s[3]), vetor_total_racional[i]))
        #                 #print("######################################## FIM DA EXECUÇÃO ######################################## ")
        #                 achou = 1
    
   
    
solution()