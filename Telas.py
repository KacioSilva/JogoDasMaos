from xml.dom.minidom import Element
import PySimpleGUI as sg
import Img_Maos
import random

p1_mao_direita_g, p1_mao_esquerda_g, p2_mao_direita_g, p2_mao_esquerda_g, vez_jogador, contador_vez = 0, 0, 0, 0, 1, 0
p2_mao_esquerda_visivel, p2_mao_direita_visivel, p1_mao_esquerda_visivel, p1_mao_direita_visivel = True, True, True, True
p1m_dedo_mao_esquerda, p1m_dedo_mao_direita, p2m_dedo_mao_esquerda, p2m_dedo_mao_direita, p1_vencedor, p2_vencedor, pontos = False, False, False, False, False, False, 0


def vencedor():
    global pontos
    c = 1
    try:
        jogadores = open("rank.txt", "r")
        for linha in jogadores:
            if jogador1+'\n' == linha:

                jogadores.close()
            c += 1
    except:
        if p1_vencedor == True:
            jogadores = open("rank.txt", "a")
            pontos += 1
            jogadores.writelines([str(jogador1) + "\n" + str(pontos)])
            jogadores.close()


def janela_dois_jogadores():

    global p1_mao_direita_g, p1_mao_esquerda_g, p2_mao_direita_g, p2_mao_esquerda_g, vez_jogador, contador_vez, p2_mao_esquerda_visivel, p2_mao_direita_visivel, p1_mao_esquerda_visivel, p1_mao_direita_visivel, p1m_dedo_mao_esquerda, p1m_dedo_mao_direita, p2m_dedo_mao_esquerda, p2m_dedo_mao_direita, nome_jogador1, nome_jogador2

    sg.theme('bluemono')

    # IMAGEM DAS MÃOS PLAYER 1
    if p1_mao_direita_g == 0: #g = global
        p1_img_mao_d = Img_Maos.mao0
    if p1_mao_esquerda_g == 0:
        p1_img_mao_e = Img_Maos.mao0

    if p1_mao_direita_g == 1:
        p1_img_mao_d = Img_Maos.mao1
    if p1_mao_esquerda_g == 1:
        p1_img_mao_e = Img_Maos.mao1

    if p1_mao_direita_g == 2:
        p1_img_mao_d = Img_Maos.mao2
    if p1_mao_esquerda_g == 2:
        p1_img_mao_e = Img_Maos.mao2

    if p1_mao_direita_g == 3:
        p1_img_mao_d = Img_Maos.mao3
    if p1_mao_esquerda_g == 3:
        p1_img_mao_e = Img_Maos.mao3

    if p1_mao_direita_g == 4:
        p1_img_mao_d = Img_Maos.mao4
    if p1_mao_esquerda_g == 4:
        p1_img_mao_e = Img_Maos.mao4

    if p1_mao_direita_g == 5:
        p1_img_mao_d = Img_Maos.mao5
    if p1_mao_esquerda_g == 5:
        p1_img_mao_e = Img_Maos.mao5

    # IMAGEM DAS MÃOS PLAYER 2
    if p2_mao_direita_g == 0:
        p2_img_mao_d = Img_Maos.mao0
    if p2_mao_esquerda_g == 0:
        p2_img_mao_e = Img_Maos.mao0

    if p2_mao_direita_g == 1:
        p2_img_mao_d = Img_Maos.mao1
    if p2_mao_esquerda_g == 1:
        p2_img_mao_e = Img_Maos.mao1

    if p2_mao_direita_g == 2:
        p2_img_mao_d = Img_Maos.mao2
    if p2_mao_esquerda_g == 2:
        p2_img_mao_e = Img_Maos.mao2

    if p2_mao_direita_g == 3:
        p2_img_mao_d = Img_Maos.mao3
    if p2_mao_esquerda_g == 3:
        p2_img_mao_e = Img_Maos.mao3

    if p2_mao_direita_g == 4:
        p2_img_mao_d = Img_Maos.mao4
    if p2_mao_esquerda_g == 4:
        p2_img_mao_e = Img_Maos.mao4

    if p2_mao_direita_g == 5:
        p2_img_mao_d = Img_Maos.mao5
    if p2_mao_esquerda_g == 5:
        p2_img_mao_e = Img_Maos.mao5

    # Contagem para vez de cada jogador 
    if vez_jogador == 1:
        p1_vez_jogador_nao_jogar = False
        p2_vez_jogador_nao_jogar = True



    
        if contador_vez == 1:
            p1_vez_jogador_nao_jogar = True
            p2_vez_jogador_nao_jogar = False
        contador_vez += 1
        if contador_vez == 2:
            vez_jogador = 2
            contador_vez = 0

    elif vez_jogador == 2:
        p1_vez_jogador_nao_jogar = True
        p2_vez_jogador_nao_jogar = False
        if contador_vez == 1:
            p1_vez_jogador_nao_jogar = False
            p2_vez_jogador_nao_jogar = True
        contador_vez += 1
        if contador_vez == 2:
            vez_jogador = 1
            contador_vez = 0

    # Posicionamento do quadrado das Mãos
    if p2_mao_esquerda_g == 1:
        p2_me_altura = 170
        p2_me_largura = 140
        esp_meio = 1
        esp_alto = 3
    else:
        p2_me_altura = 350
        p2_me_largura = 140
        esp_meio = 1
        esp_alto = 1

    if p2_mao_direita_g == 1:
        p2_md_altura = 170
        p2_md_largura = 140
        esp_meio = 1
        esp_alto = 3
    else:
        p2_md_altura = 350
        p2_md_largura = 140
        esp_meio = 1
        esp_alto = 1

    if p1_mao_esquerda_g == 1:
        p1_me_altura = 170
        p1_me_largura = 140
        esp_meio = 1
        esp_alto = 3
    else:
        p1_me_altura = 350
        p1_me_largura = 140
        esp_meio = 1
        esp_alto = 1

    if p1_mao_direita_g == 1:
        p1_md_altura = 170
        p1_md_largura = 140
        esp_meio = 1
        esp_alto = 3
    else:
        p1_md_altura = 350
        p1_md_largura = 140
        esp_meio = 1
        esp_alto = 1

    if p1_mao_esquerda_g == 6:
        p1_me_altura = 350
        p1_me_largura = 245
        esp_meio = 1
        esp_alto = 3
    else:
        p1_me_altura = 350
        p1_me_largura = 245
        esp_meio = 1
        esp_alto = 1

    if p1_mao_direita_g == 6:
        p1_md_altura = 350
        p1_md_largura = 245
        esp_meio = 1
        esp_alto = 3
    else:
        p1_md_altura = 350
        p1_md_largura = 245
        esp_meio = 1
        esp_alto = 1

    if p2_mao_esquerda_g == 6:
        p2_me_altura = 350
        p2_me_largura = 245
        esp_meio = 1
        esp_alto = 3
    else:
        p2_me_altura = 350
        p2_me_largura = 245
        esp_meio = 1
        esp_alto = 1

    if p2_mao_direita_g == 6:
        p2_md_altura = 350
        p2_md_largura = 245
        esp_meio = 1
        esp_alto = 3
    else:
        p2_md_altura = 350
        p2_md_largura = 245
        esp_meio = 1
        esp_alto = 1

    layout_dois_jogador = [[(sg.Text('', size=[40, esp_alto]))],
                           [(sg.Text('{}'.format(jogador2),visible = p1_vez_jogador_nao_jogar, size=[31, 0],
                             justification='r', font='ARIAL 16'))],
                           [sg.Button('', visible=p2_mao_esquerda_visivel, disabled=p2_vez_jogador_nao_jogar, image_data=p2_img_mao_e, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_size=(p2_me_largura, p2_me_altura), border_width=0, key='-p2_me-'),
                            (sg.Text('', size=[20, 0])),
                            sg.Button('', visible=p2_mao_direita_visivel, disabled=p2_vez_jogador_nao_jogar, image_data=p2_img_mao_d, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_size=(p2_md_largura, p2_md_altura), border_width=0, key='-p2_md-')],
                           [(sg.Text('', size=[40, esp_meio]))],
                           [sg.Button('', visible=p1_mao_esquerda_visivel, disabled=p1_vez_jogador_nao_jogar, image_data=p1_img_mao_e, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_size=(p1_me_largura, p1_me_altura), border_width=0, key='-p1_me-'),
                            (sg.Text('', size=[20, 0])),
                            sg.Button('', visible=p1_mao_direita_visivel, disabled=p1_vez_jogador_nao_jogar, image_data=p1_img_mao_d, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_size=(p1_md_largura, p1_md_altura), border_width=0, key='-p1_md-')],
                           [(sg.Text('{}'.format(jogador1),visible = p2_vez_jogador_nao_jogar ,size=[31, 0],
                             justification='r', font='ARIAL 16'))],
                           [(sg.Text('', size=[40, esp_alto]))]]

    layout = [[sg.Column(layout_dois_jogador, justification='c')]]

    tela_dois_jogadores = sg.Window(
        'Game', layout, size=(800, 900), location=(350, 0))
    global contador_jogar, p1_vencedor, p2_vencedor
    while True: # Fechar quando algum dos jogadores deixar as 2 mãos do adversário desabilitadas
        if p1_mao_esquerda_visivel == False and p1_mao_direita_visivel == False:
            tela_dois_jogadores.close()
            p1_vencedor = True
            vencedor()
        elif p2_mao_esquerda_visivel == False and p2_mao_direita_visivel == False:
            tela_dois_jogadores.close()
            p2_vencedor = True
            vencedor()
        event, values = tela_dois_jogadores.read()

        if event == sg.WIN_CLOSED or event == 'Sair':
            break


        if comeco_jogador == 1: # começo_jogador = vez_jogador porque essa variável atribui a vez do jogador de forma que ela não altere o valor contido nela
            contador_jogar += 1
            if contador_jogar <= 2:
                global p1_mao_esquerda_clicked, p1_mao_direita_clicked, menos_um_dedo

                if event == '-p1_me-': #mão esquerda do player 1 -- Se o usuário clicar na mão esquerda do player 1, a mão esquerda vai atribuir como True
                    p1_mao_esquerda_clicked = True 
                    tela_dois_jogadores.close() #fecha pra tela recarregar
                    janela_dois_jogadores() #chama a função para voltar pra tela carregada

                if event == '-p2_me-' and p1_mao_esquerda_clicked == True: # p1 mao clicked é quando a mão já está selecionada
                    p2_mao_esquerda_g += p1_mao_esquerda_g
                    if p1_mao_esquerda_g == 0:
                        p2_mao_esquerda_g += 1
                    if p2_mao_esquerda_g == 5:
                        p2_mao_esquerda_visivel = False #vai se tornar invisível
                    elif p2_mao_esquerda_g > 5:
                        p2_mao_esquerda_g -= 5
                    tela_dois_jogadores.close()
                    p1_mao_esquerda_clicked = False # pra não entrar nessa função de novo
                    janela_dois_jogadores()

                if event == '-p2_md-' and p1_mao_esquerda_clicked == True:
                    p2_mao_direita_g += p1_mao_esquerda_g
                    if p1_mao_esquerda_g == 0:
                        p2_mao_direita_g += 1
                    if p2_mao_direita_g == 5:
                        p2_mao_direita_visivel = False
                    elif p2_mao_direita_g > 5:
                        p2_mao_direita_g -= 5
                    tela_dois_jogadores.close()
                    p1_mao_esquerda_clicked = False
                    janela_dois_jogadores()

                if event == '-p1_md-':
                    p1_mao_direita_clicked = True
                    tela_dois_jogadores.close()
                    janela_dois_jogadores()

                if event == '-p2_me-' and p1_mao_direita_clicked == True:
                    p2_mao_esquerda_g += p1_mao_direita_g
                    if p1_mao_direita_g == 0:
                        p2_mao_esquerda_g += 1
                    if p2_mao_esquerda_g == 5:
                        p2_mao_esquerda_visivel = False
                    elif p2_mao_esquerda_g > 5:
                        p2_mao_esquerda_g -= 5
                    tela_dois_jogadores.close()
                    p1_mao_direita_clicked = False
                    janela_dois_jogadores()

                if event == '-p2_md-' and p1_mao_direita_clicked == True:
                    p2_mao_direita_g += p1_mao_direita_g
                    if p1_mao_direita_g == 0:
                        p2_mao_direita_g += 1
                    if p2_mao_direita_g == 5:
                        p2_mao_direita_visivel = False
                    elif p2_mao_direita_g > 5:
                        p2_mao_direita_g -= 5
                    tela_dois_jogadores.close()
                    p1_mao_direita_clicked = False
                    janela_dois_jogadores()

            elif contador_jogar >= 3 and contador_jogar <= 4:
                if contador_jogar == 4:
                    contador_jogar = 0
                global p2_mao_esquerda_clicked, p2_mao_direita_clicked
                if event == '-p2_me-':
                    p2_mao_esquerda_clicked = True
                    tela_dois_jogadores.close()
                    janela_dois_jogadores()

                if event == '-p1_me-' and p2_mao_esquerda_clicked == True:
                    p1_mao_esquerda_g += p2_mao_esquerda_g
                    if p2_mao_esquerda_g == 0:
                        p1_mao_esquerda_g += 1
                    if p1_mao_esquerda_g == 5:
                        p1_mao_esquerda_visivel = False
                    elif p1_mao_esquerda_g > 5:
                        p1_mao_esquerda_g -= 5
                    tela_dois_jogadores.close()
                    p2_mao_esquerda_clicked = False
                    janela_dois_jogadores()

                if event == '-p1_md-' and p2_mao_esquerda_clicked == True:
                    p1_mao_direita_g += p2_mao_esquerda_g
                    if p2_mao_esquerda_g == 0:
                        p1_mao_direita_g += 1
                    if p1_mao_direita_g == 5:
                        p1_mao_direita_visivel = False
                    elif p1_mao_direita_g > 5:
                        p1_mao_direita_g -= 5
                    tela_dois_jogadores.close()
                    p2_mao_esquerda_clicked = False
                    janela_dois_jogadores()

                if event == '-p2_md-':
                    p2_mao_direita_clicked = True
                    tela_dois_jogadores.close()
                    janela_dois_jogadores()

                if event == '-p1_me-' and p2_mao_direita_clicked == True:
                    p1_mao_esquerda_g += p2_mao_direita_g
                    if p2_mao_direita_g == 0:
                        p1_mao_esquerda_g += 1
                    if p1_mao_esquerda_g == 5:
                        p1_mao_esquerda_visivel = False
                    elif p1_mao_esquerda_g > 5:
                        p1_mao_esquerda_g -= 5
                    tela_dois_jogadores.close()
                    p2_mao_direita_clicked = False
                    janela_dois_jogadores()

                if event == '-p1_md-' and p2_mao_direita_clicked == True:
                    p1_mao_direita_g += p2_mao_direita_g
                    if p2_mao_direita_g == 0:
                        p1_mao_direita_g += 1
                    if p1_mao_direita_g == 5:
                        p1_mao_direita_visivel = False
                    elif p1_mao_direita_g > 5:
                        p1_mao_direita_g -= 5
                    tela_dois_jogadores.close()
                    p2_mao_direita_clicked = False
                    janela_dois_jogadores()
        if comeco_jogador == 2:
            contador_jogar += 1
            if contador_jogar <= 2:
                if event == '-p2_me-':
                    p2_mao_esquerda_clicked = True
                    tela_dois_jogadores.close()
                    janela_dois_jogadores()

                if event == '-p1_me-' and p2_mao_esquerda_clicked == True:
                    p1_mao_esquerda_g += p2_mao_esquerda_g
                    if p2_mao_esquerda_g == 0:
                        p1_mao_esquerda_g += 1
                    if p1_mao_esquerda_g == 5:
                        p1_mao_esquerda_visivel = False
                    elif p1_mao_esquerda_g > 5:
                        p1_mao_esquerda_g -= 5
                    tela_dois_jogadores.close()
                    p2_mao_esquerda_clicked = False
                    janela_dois_jogadores()

                if event == '-p1_md-' and p2_mao_esquerda_clicked == True:
                    p1_mao_direita_g += p2_mao_esquerda_g
                    if p2_mao_esquerda_g == 0:
                        p1_mao_direita_g += 1
                    if p1_mao_direita_g == 5:
                        p1_mao_direita_visivel = False
                    elif p1_mao_direita_g > 5:
                        p1_mao_direita_g -= 5
                    tela_dois_jogadores.close()
                    p2_mao_esquerda_clicked = False
                    janela_dois_jogadores()

                if event == '-p2_md-':
                    p2_mao_direita_clicked = True
                    tela_dois_jogadores.close()
                    janela_dois_jogadores()

                if event == '-p1_me-' and p2_mao_direita_clicked == True:
                    p1_mao_esquerda_g += p2_mao_direita_g
                    if p2_mao_direita_g == 0:
                        p1_mao_esquerda_g += 1
                    if p1_mao_esquerda_g == 5:
                        p1_mao_esquerda_visivel = False
                    elif p1_mao_esquerda_g > 5:
                        p1_mao_esquerda_g -= 5
                    tela_dois_jogadores.close()
                    p2_mao_direita_clicked = False
                    janela_dois_jogadores()

                if event == '-p1_md-' and p2_mao_direita_clicked == True:
                    p1_mao_direita_g += p2_mao_direita_g
                    if p2_mao_direita_g == 0:
                        p1_mao_direita_g += 1
                    if p1_mao_direita_g == 5:
                        p1_mao_direita_visivel = False
                    elif p1_mao_direita_g > 5:
                        p1_mao_direita_g -= 5
                    tela_dois_jogadores.close()
                    p2_mao_direita_clicked = False
                    janela_dois_jogadores()

            elif contador_jogar >= 3 and contador_jogar <= 4:
                if contador_jogar == 4:
                    contador_jogar = 0
                if event == '-p1_me-':
                    p1_mao_esquerda_clicked = True
                    tela_dois_jogadores.close()
                    janela_dois_jogadores()

                if event == '-p2_me-' and p1_mao_esquerda_clicked == True:
                    p2_mao_esquerda_g += p1_mao_esquerda_g
                    if p1_mao_esquerda_g == 0:
                        p2_mao_esquerda_g += 1
                    if p2_mao_esquerda_g == 5:
                        p2_mao_esquerda_visivel = False
                    elif p2_mao_esquerda_g > 5:
                        p2_mao_esquerda_g -= 5
                    tela_dois_jogadores.close()
                    p1_mao_esquerda_clicked = False
                    janela_dois_jogadores()

                if event == '-p2_md-' and p1_mao_esquerda_clicked == True:
                    p2_mao_direita_g += p1_mao_esquerda_g
                    if p1_mao_esquerda_g == 0:
                        p2_mao_direita_g += 1
                    if p2_mao_direita_g == 5:
                        p2_mao_direita_visivel = False
                    elif p2_mao_direita_g > 5:
                        p2_mao_direita_g -= 5
                    tela_dois_jogadores.close()
                    p1_mao_esquerda_clicked = False
                    janela_dois_jogadores()

                if event == '-p1_md-':
                    p1_mao_direita_clicked = True
                    tela_dois_jogadores.close()
                    janela_dois_jogadores()

                if event == '-p2_me-' and p1_mao_direita_clicked == True:
                    p2_mao_esquerda_g += p1_mao_direita_g
                    if p1_mao_direita_g == 0:
                        p2_mao_esquerda_g += 1
                    if p2_mao_esquerda_g == 5:
                        p2_mao_esquerda_visivel = False
                    elif p2_mao_esquerda_g > 5:
                        p2_mao_esquerda_g -= 5
                    tela_dois_jogadores.close()
                    p1_mao_direita_clicked = False
                    janela_dois_jogadores()

                if event == '-p2_md-' and p1_mao_direita_clicked == True:
                    p2_mao_direita_g += p1_mao_direita_g
                    if p1_mao_direita_g == 0:
                        p2_mao_direita_g += 1
                    if p2_mao_direita_g == 5:
                        p2_mao_direita_visivel = False
                    elif p2_mao_direita_g > 5:
                        p2_mao_direita_g -= 5
                    tela_dois_jogadores.close()
                    p1_mao_direita_clicked = False
                    janela_dois_jogadores()

    tela_dois_jogadores.close()


def nome_jogadores():
    global jogador1, jogador2
    jogador1 = ''
    jogador2 = ''
    sg.theme('dark blue 3')

    layout_nome = [[(sg.Text('Nome dos Jogadores:', justification='c', font='Arial 15'))],
                   [(sg.Text('Jogador 1:')), sg.InputText()],
                   [(sg.Text('Jogador 2:')), sg.InputText()],
                   [sg.Button('Voltar', border_width='3'), sg.Button('Avançar', border_width='3')]]
    tela_nome = sg.Window('Nome dos Jogadores', layout_nome)

    while True:
        event, values = tela_nome.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Voltar':
            tela_nome.close()
            tela_principal()
        elif event == 'Avançar':
            tela_nome.close()
            jogador1 = values[0]
            jogador2 = values[1]
            janela_dois_jogadores()


def janela_regras():
    sg.theme('dark blue 3')
    col = [[sg.Text('O programa consiste, basicamente, num jogo entre duas pessoas ou uma partida entre um homem e uma máquina em que quem eliminar as duas mãos primeiro, vence.', font="Arial 13")],
           [sg.Text('Regra número 1 - O participante que fará a primeira jogada será selecionado aleatoriamente pelo computador;', font="Arial 11")],
           [sg.Text('Regra número 2 - Quando a mão completar os 5 dedos, essa mão será eliminada do jogo, sem a opção de poder voltar;', font="Arial 11")],
           [sg.Text('Regra número 3 - Quando a soma entre os dedos for maior do que 5, será feita a diferença entre o total menos 5; o resto será o resultado', font="Arial 11")],
           [sg.Text(
               'Regra número 4 - Em hipótese alguma o participante poderá passar a vez sem jogar;', font="Arial 11")],
           [sg.Text(
               'Regra número 5 - Ganha aquele que conseguir eliminar as duas mãos do oponente', font="Arial 11")],
           [sg.Text('Bom jogo! :D''', font="ARIAL 14")]]
        

    layout_regras = [[sg.Button('Voltar', size=(40, 2)),
                      [sg.Column(col)]]]

    tela_regras = sg.Window('Regras', layout_regras)

    while True:
        event, values = tela_regras.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Voltar':
            tela_regras.close()
            tela_principal()

    tela_regras.close()


def tela_principal():
    global p1_mao_esquerda_clicked, p1_mao_direita_clicked, p2_mao_direita_clicked, p2_mao_esquerda_clicked, vez_jogador, comeco_jogador, contador_jogar, menos_um_dedo
    p1_mao_direita_clicked, p1_mao_esquerda_clicked, p2_mao_direita_clicked, p2_mao_esquerda_clicked, contador_jogar, menos_um_dedo = False, False, False, False, 0, False
    vez_jogador = random.randint(1, 2) # Para escolher qual jogador vai começar
    comeco_jogador = vez_jogador

    sg.theme('dark blue 3')

        # ------------- BOTÕES DA TELA INICIAL -------------
    layout_menu = [[(sg.Text('Jogo das Mãos', size=[60, 1], justification='c', font='courier 65'))],
                   [(sg.Text(' ', size=[40, 5]))],
                   [sg.Button('Dois Jogadores', font='corrier',
                              size=(50, 5), border_width='8')],  #(largura, espessura) 
                   [sg.Button('Regras', font='corrier',
                              size=(50, 5), border_width='8')],
                   [sg.Button('Sair', font='corrier',
                              size=(50, 5), border_width='8')]]
    menu_principal = sg.Window(
        'Joguinho das mãos', layout_menu, element_justification='c', size=(750, 650))

    while True:
        event, values = menu_principal.read()   # Manter a tela aberta
        if event == sg.WIN_CLOSED or event == 'Sair':  # Criando o botão para fechar a janela
            break
        elif event == 'Dois Jogadores':
            menu_principal.close()
            nome_jogadores()
            janela_dois_jogadores()
        elif event == 'Rank':
            menu_principal.close()
            janela_rank()
        elif event == 'Regras':
            menu_principal.close()
            janela_regras()
    menu_principal.close()


tela_principal()
