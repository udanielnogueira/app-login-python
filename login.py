from PySimpleGUI import PySimpleGUI as sg

# Layout do login
sg.theme('Dark Grey 13') # Reddit
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))], # linha com campo texto e campo input
    [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
# Janela do Login
janela = sg.Window('Login App', layout)





# layout do Sistema
sg.theme('Dark Grey 13') # Reddit
layout2 = [
    [sg.Text('\n\n')],
    [sg.Text('              Sistema             ')],
    [sg.Text('\n\n')],
]
# Janela do Sistema
janela2 = sg.Window('Sistema', layout2)






# Eventos
while True:
    # lendo eventos e inputs da janela
    eventos, valores = janela.read() 
    
    # botão fechar
    if eventos == sg.WIN_CLOSED:
        break

    # botão entrar
    if eventos == 'Entrar':

        # dados válidos
        if valores['usuario'] == 'daniel' and valores['senha'] == '1234':
            
            # passagem de valor para variável
            nome = valores['usuario']

            # pop up
            sg.popup('Login realizado com sucesso', f'Bem vindo ao sistema {nome}', title='Login') # aceita pop de variáveis
            
            # abrindo janela do sistema
            while True:
                eventos, valores = janela2.read()
                if eventos == sg.WIN_CLOSED:
                    break
        
        # dados inválidos
        else:
            sg.popup('Dados inválidos', 'Tente novamente', title='Login') 

'''
debug output
sg.Print('Erro')
'''
