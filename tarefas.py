tarefas_concluidas = []
tarefas_pendentes = []
tarefas_removidas = []

def add_task():
    
    """
    Função que serve de 'base' para a função 'adicionar_tarefa'. Serve como forma de reduzir o boilerplate coding.
    Ainda que sejam de certa forma 'independentes' uma complementa a outra.
    """
    
    adicionando_tarefa = input("Qual tarefa você quer adicionar: ")   
    tarefas_pendentes.append(adicionando_tarefa)
    
    print('-' * 30)
    print("Tarefa adicioanda com sucesso! ")
    ...
...
    
# falta só escrever aqui
def adicionar_tarefa():
    
        adicionar_tarefa = input("Gostaria de adicionar uma tarefa?  [s] / [n] ")

        if adicionar_tarefa == 's': add_task()
               
        while True: 
            adicionar_outra = input("Vai querer adicionar outra ?  ")
        
            if adicionar_outra == 's': add_task()                         
            
            if adicionar_outra == 'n': 
                print("-" * 30)
                print("Lista de tarefas fechada por hora. ")                
                break
...            
                   
def pendentes():
    
    """
    Função que enumera e retorna as tarefas, baseadas na ordem de criação, indo da primeira a ultima.
    """
    
    for numero_tarefa, tarefa in enumerate(tarefas_pendentes): print(f"Numero da tarefa {numero_tarefa +1}, tarefa: {tarefa}")
                         

def listar_tarefas(): 
    
    """
    Função que permite ao usuário fazer a listagem das tarefas concluidas e/ou pendentes.
    """
    
    resposta = input("Voce quer ver as tarefas pendentes ou as concluidas:  [pendentes] / [concluidas]  ")

    if resposta == 'pendentes': pendentes()
                    
    if resposta == 'concluidas': print([tarefa_concluida for tarefa_concluida in tarefas_concluidas])            


def remover_tarefa():
    
    """
    Função que permite ao usuário deletar tarefas da lista baseado no index da mesma.
    Ao final desta, é retornado ao usuário a lista atualizada sem a tarefa recem deletada.
    
    Existe um bug nesta função que a não ser que tenha apenas 1 tarefa, um erro vai ser disparado e encerrar o programa,
   de resto funciona corretamente.
    """
    
    
    print("Listando abaixo as tarefas pendentes:") 
    print("=" * 30)
    pendentes()


    print("Escreva apenas o index. ")
    print("-" * 15)

    remover = int(input("Qual tarefa voce quer remover "))
 
    tarefas_pendentes.pop(remover)
    
    print("=" * 10)
    print("Tarefa removida com sucesso!")    

    print(f"A quantidade de tarefas na sua lista é {tarefas_pendentes}")    
...    

def atualizar_tarefa():
    
    """
    Função que se inicia listando as tarefas caracterizadas como 'pendentes', com o intuito de que o usuário possa visualizar as mesmas,
    para que assim possa atualizar o estado da mesma para 'concluida'.

    Ao final desta função é retornado ao usuário quais ainda estão pendentes e a listagem das concluidas
    
    """
    
    pendentes()
    resposta = input("Escreva o nome da tarefa que voce concluiu:  ")
    
    tarefas_concluidas.append(resposta)
    tarefas_pendentes.remove(resposta)
    
    print(f"listagem das concluidas: {tarefas_concluidas}")
    print("-" * 30)
    print(f"Listagem das pendentes {tarefas_pendentes}")


def menu_usuario():

    """
    Função que tem como objetivo disponibilizar uma "interface gráfica" para o usuário, de forma que ele possa realizar o CRUD.
    Esta função é criada inspirada no sistema de switch case com o intuito de fazer o código menos repetitivo e mais limpo.
    
    O loop desta função se mantém para que o usuário possa realizar todas as operações e sair quando escrever 'x', devido ao 'break'.
    """

    while True:

        operacao = input("O que deseja fazer:  [1] Adicionar tarefa, [2] Listar tarefas [3] Alterar o estado de uma tarefa [4] Deletar uma tarefa , [x] para sair ")

        match operacao:
            case '1':
                adicionar_tarefa()
            case '2':
                listar_tarefas()
            case '3':
                atualizar_tarefa()
            case '4':
                remover_tarefa()
            case 'x':
                print("Obrigado por utilizar este sistema!")
                break
            case _:
                print("Operacao inválida.")