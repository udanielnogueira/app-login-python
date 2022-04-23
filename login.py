from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme('Reddit')

layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))], # linha com campo texto e campo input
    [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

# janela
janela = sg.Window('Tela de login', layout)

# eventos
while True:
    eventos, valores = janela.read() # lendo eventos e inputs da janela
 
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'daniel' and valores['senha'] == '1234':
            print('Bem vindo ao sistema!')
