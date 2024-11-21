from PySimpleGUI import PySimpleGUI as sg

# Layout do login
sg.theme("Dark Grey 13")
layout = [
    [sg.Text("Usuário"), sg.Input(key="usuario", size=(20, 1))],
    [sg.Text("Senha  "), sg.Input(key="senha", password_char="*", size=(20, 1))],
    [sg.Checkbox("Salvar o login?")],
    [sg.Button("Entrar")],
]

# Janela do login
janela = sg.Window("Login", layout, size=(640, 480))

# Layout do sistema
sg.theme("Dark Grey 13")
layout2 = [
    [sg.Text("Sistema funcionando...")],
]

# Janela do sistema
janela2 = sg.Window("App", layout2, size=(640, 480))

# Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == "Entrar":
        # Dados válidos
        if valores["usuario"] == "daniel" and valores["senha"] == "123":

            # Passagem de valor para variável
            nome = valores["usuario"]

            # Pop-up
            sg.popup(
                "Login realizado com sucesso!",
                f"Bem vindo ao sistema {nome.capitalize()}.",
                title=" ",
            )

            # Fechando janela do login
            janela.close()

            # Abrindo janela do sistema
            while True:
                eventos, valores = janela2.read()
                if eventos == sg.WIN_CLOSED:
                    break

        # Dados inválidos
        else:
            sg.popup("Dados inválidos, tente novamente.", title=" ")

"""
debug output
sg.Print('Error')
"""
