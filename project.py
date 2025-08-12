tarefa = []

while True:
    print('Bem-vindo a Gerenciador de TAREFAS!')
    print('Escolha uma opção:')
    print('1. Adicionar Tarefa')
    print('2. Ver tarefas')
    print('3. Remover uma Tarefa')
    print('4. Sair')
    resp = int(input())
    
    # Addicionar Tarefas
    if resp == 1:
        
        print('Digite a nova Tarefa: ')
        tarefa.append(input())
        
    # Ver Tarefas
    elif resp == 2:
        if not tarefa:
            print('Não há tarefas adicionadas!')
            add_tarefa = input('\nDeseja adicionar uma tarefa? s/n')
            if add_tarefa.lower() == 's':
                print('Digite a nova Tarefa: ')
                tarefa.append(input())
        for tarefa in tarefa:
            print(tarefa)
            
    # Remover Tarefas
    elif resp == 3:
        if not tarefa:
            print('Não há tarefas adicionadas!')
            add_tarefa = input('\nDeseja adicionar uma tarefa? s/n')
            if add_tarefa.lower() == 's':
                print('Digite a nova Tarefa: ')
                tarefa.append(input())
            
            
        else:
            print(tarefa)
            print('Digite o item que deseja remover?')
            tarefa.discard(input())
            print(tarefa)

    # Sair
    elif resp == 4:
        sair = input('Deseja realmente sair? s/n')
        if sair.lower() == 'n':
            print('Obrigado por usar o Gerenciador de Tarefas!')
            break
    
    else:
        print('Opção Inválida!')
    