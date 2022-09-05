from distutils import core
import random

def escolher(bolinha: str):
    if bolinha == "1":
        corEscolhida = "azul"
    elif bolinha == "2":
        corEscolhida = "verde"
    elif bolinha == "3":
        corEscolhida = "amarela"
    elif bolinha == "4":
        corEscolhida = "vermelhas"  
    elif bolinha == "5":
        corEscolhida = "laranjas" 
    
    return corEscolhida        
                
            
def separar(escolhida):
    list = createList(50)
    tentativas = 0
    azul = 0
    verde = 0
    amarela = 0
    vermelhas = 0
    laranjas = 0
    corEscolhida = escolher(escolhida)
    
    while (True): 
        numeroSorteado = (random.choice(list))
        list.remove(numeroSorteado)
        tentativas+=1
        
        
        if numeroSorteado >=1 and numeroSorteado <=10:
            azul+=1
            if corEscolhida == "azul":    
                break
        elif numeroSorteado >=11 and numeroSorteado <=20:
            verde+=1
            if corEscolhida == "verde":
                break
        elif numeroSorteado >=21 and numeroSorteado <=30:
            amarela+=1
            if corEscolhida == "amarela":
                break
        elif numeroSorteado >=31 and numeroSorteado <=40:
            vermelhas+=1
            if corEscolhida == "vermelhas":
                break
        elif numeroSorteado >=41 and numeroSorteado <=50:
            laranjas+=1
            if corEscolhida == "laranjas":
                break 
               
    return tentativas

def ultimoSobrevivente (escolhida):
    
    list = createList(50)
    dicionario = {}
    dicionario["azul"] = 0
    dicionario["verde"] = 0
    dicionario["amarela"] = 0
    dicionario["vermelhas"] = 0
    dicionario["laranjas"] = 0
    corEscolhida = escolher(escolhida)
    
    while (True): 
        numeroSorteado = (random.choice(list))
        list.remove(numeroSorteado)
        
        
        
        if numeroSorteado >=1 and numeroSorteado <=10:
            dicionario["azul"] +=1
            
        elif numeroSorteado >=11 and numeroSorteado <=20:
           dicionario["verde"] +=1
        elif numeroSorteado >=21 and numeroSorteado <=30:
           dicionario["amarela"]+=1
        elif numeroSorteado >=31 and numeroSorteado <=40:
            dicionario["vermelhas"]+=1
        elif numeroSorteado >=41 and numeroSorteado <=50:
            dicionario["laranjas"]+=1
        
        resultado = valida_fim_jogo(dicionario)
        if(resultado):
            if corEscolhida in resultado.keys():
                return f"O ultimo sobrevivente foi {corEscolhida}, com {resultado[corEscolhida]} bolinhas!"
            else:
                return "não sobreviveu!" 
                
               
            
def valida_fim_jogo(dicionario):
    soma = 0
    novo_dicionario = dicionario.copy()
    for cor in dicionario.keys():
        if(dicionario[cor]==10):
            soma += 10
            novo_dicionario.pop(cor)
    
        
    if soma >=40:
        return novo_dicionario        
    else:
        return None
    

            
      
def createList(n):
    lst = []
    for i in range(n+1):
        lst.append(i)
    return(lst)
        
          
    
corEscolhida = input(f'Agora voce pode escolher uma cor, digite [1] azul\[2] verde\[3] amarela\[4] vermelhas\[5] laranjas:')
#separado = separar(corEscolhida)
#print (f"foram necessarias {separado} tentativa(s) cor escolhida {corEscolhida}.")
print (ultimoSobrevivente(corEscolhida))
