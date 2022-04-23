from PySimpleGUI import PySimpleGUI as sg

# Layout do login
sg.theme('Dark Grey 13') # or Reddit
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))], # linha 1
    [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(20,1))], # linha 2
    [sg.Checkbox('Salvar o login?')], # linha 3
    [sg.Button('Entrar')] # linha 4
]

# Janela do Login
janela = sg.Window('Login App', layout)

# Layout do sistema
sg.theme('Dark Grey 13') # Reddit
layout2 = [
    [sg.Text('\n\n')],
    [sg.Text('              Sistema             ')],
    [sg.Text('\n\n')],
]

# Janela do sistema
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
                janela = janela2
                janela.refresh()
                # eventos, valores = janela2.read()
                if eventos == sg.WIN_CLOSED:
                    break
        
        # dados inválidos
        else:
            sg.popup('Dados inválidos', 'Tente novamente', title='Login') 

'''
debug output
sg.Print('Erro')
'''
