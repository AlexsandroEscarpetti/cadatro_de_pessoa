import pymysql
try:

    conecting = pymysql.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'CadastroDePessoas'
    )
except:
    conecting = pymysql.connect(
        host = 'localhost',
        user = 'root',
        passwd = ''
    )
comandsql = conecting.cursor()
try:

    comandsql.execute("create database CadastroDePessoas")
    comandsql.execute("""
    CREATE TABLE `CadastroDePessoas`.`Pessoas` ( `Id` INT NOT NULL AUTO_INCREMENT ,
    `Nome` VARCHAR(50) NOT NULL ,
    `Idade` INT NOT NULL ,
    `Sexo` VARCHAR(2) NOT NULL ,
    PRIMARY KEY (`Id`))
    ENGINE = InnoDB;
    """)

except:
    pass

import PySimpleGUI as sg
sg.theme('LightBlue3')   # cor
layout = [  [sg.Text('Cadastro de usuario')],
            [sg.Text('Nome'), sg.InputText()],
            [sg.Text('idade'), sg.InputText()],
            [sg.Text('Sexo'),sg.Radio ('F','sex'),sg.Radio ('M','sex')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

erros = []
# Janela principal
window = sg.Window('Cadastro de pessoas', layout)
# Janela Erros
# Event Loop to process "events" and get the "values" of the inputs
while True:

    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
   # print('You entered ', values[1])
    nome = values[0]
    idade = values[1]
    sexoF = values[2]
    sexoM = values[3]
    erros = []

    if len(nome) < 5 and not nome.isspace():
        erros.append('È necesário digitar um nome com ao menos 5 caracteres')
    if not idade.isnumeric():
        erros.append("Idade inválida")
    elif int(idade) < 0 and int(idade) > 120:
        erros.append("Idade inválida")
    if [sexoM,sexoF]  == [False,False]:
        erros.append('Selecione o seu sexo')

    if len(erros) == 1:

        while True:

            sg.theme('LightPurple')  # cor
            layout2 = [[sg.Text('Cagadas encontadas!, corrigir:')],
                       [sg.Text(erros[0])],
                       [sg.Button('Voltar')]]
            window2 = sg.Window('ERRO', layout2)
            event, values = window2.read()
           # erros = []
            if event in (None, 'Voltar'):
                window2.close()
                break
            break

    if len(erros) == 2:

        while True:

            sg.theme('LightPurple')  # cor
            layout2 = [[sg.Text('Cagadas encontadas!, corrigir:')],
                       [sg.Text(erros[0])],
                       [sg.Text(erros[1])],
                       [sg.Button('Voltar')]]
            window2 = sg.Window('ERRO', layout2)
            event, values = window2.read()
          #  erros = []
            if event in (None, 'Voltar'):
                window2.close()
                break
            break

    if len(erros) == 3:

        while True:
            sg.theme('LightPurple')  # cor
            layout2 = [[sg.Text('Cagadas encontadas!, corrigir:')],
                       [sg.Text(erros[0])],
                       [sg.Text(erros[1])],
                       [sg.Text(erros[2])],
                       [sg.Button('Voltar')]]
            window2 = sg.Window('ERRO', layout2)
            event, values = window2.read()
            if event in (None, 'Voltar'):
                window2.close()
                break
            break

    if len(erros) == 0:
        idadePessoa = int(idade)
        if sexoF == True:
            sexo = 'F'
        else:
            sexo = 'M'

        comand = """
        INSERT INTO `pessoas` (`Id`, `Nome`, `Idade`, `Sexo`) VALUES (NULL, '{}', '{}', '{}')""".format(nome,idadePessoa,sexo)
        comandsql.execute(comand)
        conecting.commit()

window.close()