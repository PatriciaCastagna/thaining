
array = []
cont = 0
while (cont < 5):
    numeroUser = input(f'Digite 5 numeros que deseja organizar:'.format(cont))
   
    cont+=1
       
    array.append(numeroUser)

             

def escolher():
    
    escolha = input(str(f'Digite [1] crescente\[2] decrescente:'))
    
    if escolha == "1":
        
        insertion_sort(array)
        print(f'lista ordenada decrescente{array}')
        
                     
    if escolha == "2":
        
        ordenar_crescente(array)
        print(f'lista ordenada crescente{array}')
        
    
    return escolha        
        
        
          

def insertion_sort (array:list):
   for percorrer in range(1,len(array)):
      atual = array[percorrer]
      anterior = percorrer-1
 
      
      while anterior >= 0 and atual > array[anterior]:
         array[anterior+1]=array[anterior]
         anterior=anterior-1
         
      
      array[anterior+1]=atual 
      
      
                                        
def ordenar_crescente (array:list):
    
    for percorrer in range(1,len(array)):
     for ver in range(len(array)-percorrer):
        if array[ver] > array [ver+1]:
         guardar = array[ver]
         array[ver] = array[ver+1]
         array[ver+1] = guardar
      
    
            
escolher()


 