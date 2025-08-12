tarefa = []

def add_tarefas():
    print('Digite a nova Tarefa: ')
    tarefa.append(input())
    
def lista_vazia():
    if not tarefa:
            print('Não há tarefas adicionadas!')
            simounao = input('\nDeseja adicionar uma tarefa? s/n')
            if simounao.lower() == 's':
                add_tarefas()
    else:
        print(tarefa)

    

while True:
    print('Bem-vindo a Gerenciador de TAREFAS!')
    print('Opções 1 a 4:')
    print('1. Adicionar Tarefa')
    print('2. Ver tarefas')
    print('3. Remover uma Tarefa')
    print('4. Sair')
    
    
    try:
        resp = int(input('Escolha uma opção: '))
        
        # Addicionar Tarefas
        if resp == 1:
            add_tarefas()
            
        # Ver Tarefas
        elif resp == 2:
            lista_vazia()
                
        # Remover Tarefas
        elif resp == 3:
            while True:
                lista_vazia()       
                print('Digite o item que deseja remover?')
                item_rem = input()
                if item_rem in tarefa:
                    tarefa.remove(item_rem)
                else:
                    print('Item não encontrado!')
                    simounao = input('Deseja digitar novamente? s/n')
                    if simounao.lower() == 's':
                        continue
                    else:
                        break
        # Sair
        elif resp == 4:
            sair = input('Deseja realmente sair? s/n')
            if sair.lower() == 'n':
                print('Obrigado por usar o Gerenciador de Tarefas!')
                break
        
        else:
            print('Opção Inválida!')
        
        
    except ValueError:
     print('Isso não é um opção válida. Por favor, digite uma das opções.')
        