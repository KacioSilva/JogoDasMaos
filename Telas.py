import PySimpleGUI as sg
import Img_Maos
import Img_Maos, random #IMPORTANDO ALGUMAS BIBLIOTECAS/OUTROS ARQUIVOS


p1_mao_direita_g, p1_mao_esquerda_g, p2_mao_direita_g, p2_mao_esquerda_g, vez_jogador, contador_vez = 0, 0, 0, 0, 1, 0 #DECLARAÇÃO DE VARIÁVEIS A SER UTILIZADOS NO CÓDIGO
p2_mao_esquerda_visivel, p2_mao_direita_visivel, p1_mao_esquerda_visivel, p1_mao_direita_visivel = True, True, True, True #DECLARAÇÃO DE VARIÁVEIS A SER UTILIZADOS NO CÓDIGO
p1m_dedo_mao_esquerda, p1m_dedo_mao_direita,p2m_dedo_mao_esquerda, p2m_dedo_mao_direita, p1_vencedor, p2_vencedor = False, False, False, False, False, False #DECLARAÇÃO DE VARIÁVEIS A SER UTILIZADOS NO CÓDIGO

def p1_vencedor(): #FUNÇÃO A SER CHAMADA QUANDO O JOGADOR 1 VENCE O JOGO
    sg.theme('Dark Blue 3')

    p1_layout_tela_vencedor = [[(sg.Text('Vencedor(a):', size=(15,1),justification='c', font='courier 50'))], #LAYOUT DA TELA DO VENCEDOR
                   [(sg.Text('{}'.format(jogador1), size=(15,1), justification='c', font='Arial 50'))],
                   [(sg.Text('', size=[15, 12]))],
                   [sg.Button('Sair', border_width='3', size=(20,7))]]
    p1_tela_vencedor = sg.Window('Jogador Vencedor',p1_layout_tela_vencedor, element_justification='c', size=(500,500), location = (350,0)) #FAZENDO A TELA ABRIR

    while True:
        event, values = p1_tela_vencedor.read() #PEGANDO OS EVENTOS E VALORES COLOCADOS NA TELA
        if event == sg.WIN_CLOSED or event == 'Sair': #CONDIÇÃO ONDE SE O USUARIO CLICAR EM "FECHAR" OU NO BOTÃO "SAIR" ACONTECE TAL SITUAÇÃO
            quit()

def p2_vencedor(): #FUNÇÃO A SER CHAMADA QUANDO O JOGADOR 2 VENCE O JOGO
    sg.theme('Dark Blue 3')

    p2_layout_tela_vencedor = [[(sg.Text('Vencedor(a):', size=(15,1), justification='c', font='courier 50'))],
                   [(sg.Text('{}'.format(jogador2), size=(15,1), justification='c', font='Arial 50'))],
                   [(sg.Text('', size=[15, 12]))],
                   [sg.Button('Sair', border_width='3', size=(20,7))]]
    p2_tela_vencedor = sg.Window('Jogador Vencedor', p2_layout_tela_vencedor, element_justification='c', size=(500,500), location = (350,0))

    while True:
        event, values = p2_tela_vencedor.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            quit()

def empate():
    sg.theme('Dark Blue 3')

    empate_layout = [[sg.Text('EMPATE!', size=(17,2), justification='c', font='Arial 50')],
                    [sg.Text('', size=(0,3))],
                    [sg.Text('Tente novamente!', font='arial 15')],
                    [sg.Button('Sair', border_width='3', font="arial 15", size=(40,2))]]
                    


    tela_empate = sg.Window('Empate', empate_layout, element_justification='c', size=(500,500), location=(300,0))
    tela_empate.read()

    while True:
        event, values = tela_empate.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            quit()
        
def janela_dois_jogadores(): #FUNÇÃO A SER CHAMADA QUANDO O USUARIO CLICA EM DOIS JOGADORES NO MENU PRINCIPAL

    global p1_mao_direita_g, p1_mao_esquerda_g, p2_mao_direita_g, p2_mao_esquerda_g, vez_jogador, contador_vez, p2_mao_esquerda_visivel, p2_mao_direita_visivel, p1_mao_esquerda_visivel, p1_mao_direita_visivel, p1m_dedo_mao_esquerda, p1m_dedo_mao_direita,p2m_dedo_mao_esquerda, p2m_dedo_mao_direita 

    sg.theme('bluemono')

    if p1_mao_direita_g == 0: #CONDIÇÕES PARA FAZER ALTERAÇÃO DA IMAGEM DAS MÃOS NA TELA DO JOGO
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

    global p1_nome_visivel, p2_nome_visivel

    if vez_jogador == 1: #CONDIÇÃO SOBRE QUEM VAI SER A VEZ DE JOGAR, NESTA CONDIÇÃO VAI SER O JOGADOR 1
        p1_nome_visivel = True #VARIÁVEL PARA COLOCAR SE O NOME VAI FICAR INVISIVEL PARA DETERMINAR QUEM VAI SER A VEZ DE JGOAR
        p2_nome_visivel = False 
        p1_vez_jogador_nao_jogar = False #VARIAVEL PARA O BOTAO DA MAO FICAR HABILITADO OU DESABILITADO
        p2_vez_jogador_nao_jogar = True
        if contador_vez == 1:
            p1_vez_jogador_nao_jogar = True
            p2_vez_jogador_nao_jogar = False
        contador_vez += 1
        if contador_vez == 2:
            vez_jogador = 2
            contador_vez = 0
    elif vez_jogador == 2: #CONDIÇÃO SOBRE QUEM VAI SER A VEZ DE JOGAR, NESTA CONDIÇÃO VAI SER O JOGADOR 2
        p1_nome_visivel = False #VARIÁVEL PARA COLOCAR SE O NOME VAI FICAR INVISIVEL PARA DETERMINAR QUEM VAI SER A VEZ DE JGOAR
        p2_nome_visivel = True
        p1_vez_jogador_nao_jogar = True #VARIAVEL PARA O BOTAO DA MAO FICAR HABILITADO OU DESABILITADO
        p2_vez_jogador_nao_jogar = False
        if contador_vez == 1:
            p1_vez_jogador_nao_jogar = False
            p2_vez_jogador_nao_jogar = True
        contador_vez += 1
        if contador_vez == 2:
            vez_jogador = 1
            contador_vez = 0

    if p2_mao_esquerda_g == 1: #CONDIÇÕES PARA AJUSTAR A LARGURA E ALTURA DO BOTAO DE ACORDO COM A IMAGEM A SER COLOCADA
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
    
    layout_dois_jogador = [[(sg.Text('', size=[40, esp_alto]))], #LAYOUT DA TELA DE DOIS JOGADORES
                            [(sg.Text('Jogador: {}'.format(jogador2),visible=p2_nome_visivel, size=[31, 0], justification='r', font='ARIAL 16'))],
                           [sg.Button('',visible=p2_mao_esquerda_visivel ,disabled=p2_vez_jogador_nao_jogar, image_data=p2_img_mao_e, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_size=(p2_me_largura, p2_me_altura), border_width=0, key='-p2_me-'),
                            (sg.Text('', size=[20, 0])),
                            sg.Button('',visible=p2_mao_direita_visivel, disabled=p2_vez_jogador_nao_jogar, image_data=p2_img_mao_d, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_size=(p2_md_largura, p2_md_altura), border_width=0, key='-p2_md-')],
                           [(sg.Text('', size=[40, esp_meio]))],
                           [sg.Button('',visible=p1_mao_esquerda_visivel, disabled=p1_vez_jogador_nao_jogar, image_data=p1_img_mao_e, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_size=(p1_me_largura, p1_me_altura), border_width=0, key='-p1_me-'),
                            (sg.Text('', size=[20, 0])),
                            sg.Button('',visible=p1_mao_direita_visivel, disabled=p1_vez_jogador_nao_jogar, image_data=p1_img_mao_d, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_size=(p1_md_largura, p1_md_altura), border_width=0, key='-p1_md-')],
                            [(sg.Text('Jogador: {}'.format(jogador1),visible=p1_nome_visivel, size=[31, 0], justification='r', font='ARIAL 16'))],
                           [(sg.Text('', size=[40, esp_alto]))]]

    layout = [[sg.Column(layout_dois_jogador, justification='c')]]

    tela_dois_jogadores = sg.Window('Dois Jogadores', layout, size=(800, 900), location = (350,0))

    global contador_jogar, p1_vencedor, p2_vencedor

    while True: #LAÇO DE REPETIÇÃO SOBRE OS EVENTOS

        if p1_mao_esquerda_visivel == False and p1_mao_direita_visivel == False: #CONDIÇÃO VENCEDOR 
            tela_dois_jogadores.close()
            p2_vencedor() #ABRE A TELA DO JOGADOR 2 QUE VAI SER O VENCEDOR
        elif p2_mao_esquerda_visivel == False and p2_mao_direita_visivel == False:
            tela_dois_jogadores.close()
            p1_vencedor()
        event, values = tela_dois_jogadores.read()

        if event == sg.WIN_CLOSED:
            quit()
   #-----------------------------------------------------------------------  CONDIÇÃO DE EMPATE   p1_mao_direita_g == 0 p1_mao_direita_g
        if p1_mao_direita_visivel == False and p2_mao_direita_visivel == False and p1_mao_direita_g == 2 and p2_mao_direita_g == 4:
            tela_dois_jogadores.close()
            empate()
        if p1_mao_direita_visivel == False and p2_mao_direita_visivel == False and p1_mao_esquerda_g == 4 and p2_mao_esquerda_g == 2:
            tela_dois_jogadores.close()
            empate()

        if p1_mao_esquerda_visivel == False and p2_mao_esquerda_visivel == False and p1_mao_direita_g == 2 and p2_mao_direita_g == 4:
            tela_dois_jogadores.close()
            empate()
        if p1_mao_esquerda_visivel == False and p2_mao_esquerda_visivel == False and p1_mao_direita_g == 4 and p2_mao_direita_g == 2:
            tela_dois_jogadores.close()
            empate()

        if p1_mao_direita_visivel == False and p2_mao_esquerda_visivel == False and p1_mao_esquerda_g == 4 and p2_mao_direita_g == 2:
            tela_dois_jogadores.close()
            empate()
        if p1_mao_direita_visivel == False and p2_mao_esquerda_visivel == False and p1_mao_esquerda_g == 2 and p2_mao_direita_g == 4:
            tela_dois_jogadores.close()
            empate()

        if p1_mao_esquerda_visivel == False and p2_mao_direita_visivel == False and p1_mao_direita_g == 4 and p2_mao_esquerda_g == 2:
            tela_dois_jogadores.close()
            empate()
        if p1_mao_esquerda_visivel == False and p2_mao_direita_visivel == False and p1_mao_direita_g == 2 and p2_mao_esquerda_g == 4:
            tela_dois_jogadores.close()
            empate()

        

        

       
        
    
    


        if comeco_jogador == 1: #SE QUEM COMEÇAR É O JOGADOR 1 VAI ENTRAR NESSA CONDIÇÃO
            contador_jogar += 1 #CONTADOR PARA ALTERNAR A VEZ DA MAO CLICADA
            if contador_jogar <= 2:
                global p1_mao_esquerda_clicked, p1_mao_direita_clicked, menos_um_dedo
                if event == '-p1_me-':
                    p1_mao_esquerda_clicked = True
                    tela_dois_jogadores.close()
                    janela_dois_jogadores()

                if event == '-p2_me-' and p1_mao_esquerda_clicked == True:
                    p2_mao_esquerda_g += p1_mao_esquerda_g
                    if p1_mao_esquerda_g == 0:
                        p2_mao_esquerda_g+=1
                    if p2_mao_esquerda_g == 5:
                        p2_mao_esquerda_visivel = False
                    elif p2_mao_esquerda_g > 5:
                        p2_mao_esquerda_g-=5
                    tela_dois_jogadores.close()
                    p1_mao_esquerda_clicked = False
                    janela_dois_jogadores()

                if event == '-p2_md-' and p1_mao_esquerda_clicked == True:
                    p2_mao_direita_g += p1_mao_esquerda_g
                    if p1_mao_esquerda_g == 0:
                        p2_mao_direita_g+=1
                    if p2_mao_direita_g == 5:
                        p2_mao_direita_visivel = False
                    elif p2_mao_direita_g > 5:
                        p2_mao_direita_g-=5
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
                        p2_mao_esquerda_g+=1
                    if p2_mao_esquerda_g == 5:
                        p2_mao_esquerda_visivel = False
                    elif p2_mao_esquerda_g > 5:
                        p2_mao_esquerda_g-=5
                    tela_dois_jogadores.close()
                    p1_mao_direita_clicked = False
                    janela_dois_jogadores()

                if event == '-p2_md-' and p1_mao_direita_clicked == True:
                    p2_mao_direita_g += p1_mao_direita_g
                    if p1_mao_direita_g == 0:
                        p2_mao_direita_g+=1
                    if p2_mao_direita_g == 5:
                        p2_mao_direita_visivel = False
                    elif p2_mao_direita_g > 5:
                        p2_mao_direita_g-=5
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
                        p1_mao_esquerda_g+=1
                    if p1_mao_esquerda_g == 5:
                        p1_mao_esquerda_visivel = False
                    elif p1_mao_esquerda_g > 5:
                        p1_mao_esquerda_g-=5
                    tela_dois_jogadores.close()
                    p2_mao_esquerda_clicked = False
                    janela_dois_jogadores()

                if event == '-p1_md-' and p2_mao_esquerda_clicked == True:
                    p1_mao_direita_g += p2_mao_esquerda_g
                    if p2_mao_esquerda_g == 0:
                        p1_mao_direita_g+=1
                    if p1_mao_direita_g == 5:
                        p1_mao_direita_visivel = False
                    elif p1_mao_direita_g > 5:
                        p1_mao_direita_g-=5
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
                        p1_mao_esquerda_g+=1
                    if p1_mao_esquerda_g == 5:
                        p1_mao_esquerda_visivel = False
                    elif p1_mao_esquerda_g > 5:
                        p1_mao_esquerda_g-=5
                    tela_dois_jogadores.close()
                    p2_mao_direita_clicked = False
                    janela_dois_jogadores()

                if event == '-p1_md-' and p2_mao_direita_clicked == True:
                    p1_mao_direita_g += p2_mao_direita_g
                    if p2_mao_direita_g == 0:
                        p1_mao_direita_g+=1
                    if p1_mao_direita_g == 5:
                        p1_mao_direita_visivel = False
                    elif p1_mao_direita_g > 5:
                        p1_mao_direita_g-=5
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
                        p1_mao_esquerda_g+=1
                    if p1_mao_esquerda_g == 5:
                        p1_mao_esquerda_visivel = False
                    elif p1_mao_esquerda_g > 5:
                        p1_mao_esquerda_g-=5
                    tela_dois_jogadores.close()
                    p2_mao_esquerda_clicked = False
                    janela_dois_jogadores()

                if event == '-p1_md-' and p2_mao_esquerda_clicked == True:
                    p1_mao_direita_g += p2_mao_esquerda_g
                    if p2_mao_esquerda_g == 0:
                        p1_mao_direita_g+=1
                    if p1_mao_direita_g == 5:
                        p1_mao_direita_visivel = False
                    elif p1_mao_direita_g > 5:
                        p1_mao_direita_g-=5
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
                        p1_mao_esquerda_g+=1
                    if p1_mao_esquerda_g == 5:
                        p1_mao_esquerda_visivel = False
                    elif p1_mao_esquerda_g > 5:
                        p1_mao_esquerda_g-=5
                    tela_dois_jogadores.close()
                    p2_mao_direita_clicked = False
                    janela_dois_jogadores()

                if event == '-p1_md-' and p2_mao_direita_clicked == True:
                    p1_mao_direita_g += p2_mao_direita_g
                    if p2_mao_direita_g == 0:
                        p1_mao_direita_g+=1
                    if p1_mao_direita_g == 5:
                        p1_mao_direita_visivel = False
                    elif p1_mao_direita_g > 5:
                        p1_mao_direita_g-=5
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
                        p2_mao_esquerda_g+=1
                    if p2_mao_esquerda_g == 5:
                        p2_mao_esquerda_visivel = False
                    elif p2_mao_esquerda_g > 5:
                        p2_mao_esquerda_g-=5
                    tela_dois_jogadores.close()
                    p1_mao_esquerda_clicked = False
                    janela_dois_jogadores()

                if event == '-p2_md-' and p1_mao_esquerda_clicked == True:
                    p2_mao_direita_g += p1_mao_esquerda_g
                    if p1_mao_esquerda_g == 0:
                        p2_mao_direita_g+=1
                    if p2_mao_direita_g == 5:
                        p2_mao_direita_visivel = False
                    elif p2_mao_direita_g > 5:
                        p2_mao_direita_g-=5
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
                        p2_mao_esquerda_g+=1
                    if p2_mao_esquerda_g == 5:
                        p2_mao_esquerda_visivel = False
                    elif p2_mao_esquerda_g > 5:
                        p2_mao_esquerda_g-=5
                    tela_dois_jogadores.close()
                    p1_mao_direita_clicked = False
                    janela_dois_jogadores()

                if event == '-p2_md-' and p1_mao_direita_clicked == True:
                    p2_mao_direita_g += p1_mao_direita_g
                    if p1_mao_direita_g == 0:
                        p2_mao_direita_g+=1
                    if p2_mao_direita_g == 5:
                        p2_mao_direita_visivel = False
                    elif p2_mao_direita_g > 5:
                        p2_mao_direita_g-=5
                    tela_dois_jogadores.close()
                    p1_mao_direita_clicked = False
                    janela_dois_jogadores()

    tela_dois_jogadores.close()

def nome_jogadores():
    global jogador1, jogador2
    jogador1 = ''
    jogador2 = ''
    sg.theme('Dark Blue 3')

    layout_nome = [[(sg.Text('Nome dos Jogadores:', justification='c', font='Arial 15'))],
                   [(sg.Text('Jogador 1:')), sg.InputText()],
                   [(sg.Text('Jogador 2:')), sg.InputText()],
                   [sg.Button('Voltar', border_width='3'), sg.Button('Avançar', border_width='3')]]
    tela_nome = sg.Window('Nome dos Jogadores', layout_nome)

    while True:
        event, values = tela_nome.read()
        if event == sg.WIN_CLOSED:
            quit()
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
    col = [[sg.Text('O programa consiste, basicamente, num jogo entre duas pessoas cujo objetivo é eliminar as duas mãos do oponente primeiro.', font="Arial 13")],
           [sg.Text('Regra Número 1 - O participante que fará a primeira jogada será selecionado, aleatoriamente, pelo computador;', font="Arial 11")],
           [sg.Text('Regra Número 2 - Quando alguma das mãos completar 5 dedos, essa mão será eliminada do jogo, sem a opção de poder voltar;', font="Arial 11")],
           [sg.Text('Regra Número 3 - Quando a soma entre os dedos for maior do que 5, será feita a diferença entre o total menos 5: o resto será o resultado;', font="Arial 11")],
           [sg.Text('Regra Número 4 - Em hipótese alguma o participante poderá passar a vez sem jogar;', font="Arial 11")],
           [sg.Text('Regra Número 5 - Ganha aquele que conseguir eliminar as duas mãos do oponente;', font="Arial 11")],
            [sg.Text('Regra Número 6 - Uma vez selecionada a mão, não tem mais volta. Pense bem antes de selecionar alguma delas! :D', font="Arial 11")],
           [sg.Text('Bom jogo! :D', font="ARIAL 14")]]
        

    layout_regras = [[sg.Button('Voltar', size=(40, 2)),
                      [sg.Column(col)]]]

    tela_regras = sg.Window('Regras', layout_regras)

    while True:
        event, values = tela_regras.read()
        if event == sg.WIN_CLOSED:
            quit()
        if event == 'Voltar':
            tela_regras.close()
            tela_principal()

    tela_regras.close()

def tela_principal():
    global p1_mao_esquerda_clicked, p1_mao_direita_clicked, p2_mao_direita_clicked, p2_mao_esquerda_clicked, vez_jogador, comeco_jogador, contador_jogar, menos_um_dedo
    p1_mao_direita_clicked, p1_mao_esquerda_clicked, p2_mao_direita_clicked, p2_mao_esquerda_clicked, contador_jogar, menos_um_dedo = False, False, False, False, 0, False
    vez_jogador = random.randint(1, 2)
    comeco_jogador = vez_jogador

    sg.theme('Dark Blue 3')

    layout_menu = [[(sg.Text('Jogo das Mãos', size=[40, 1], justification='c',font='Arial 65'))],
                   [(sg.Text(' ', size=[40, 5]))],
                   [sg.Button('Dois Jogadores', font='arial, 16' ,size=(40, 3), border_width='6')],
                   [sg.Button('Regras', font='arial, 16', size=(40, 3), border_width='6')],
                   [sg.Button('Sair', font='arial, 16' , size=(40, 3), border_width='6')]]
    menu_principal = sg.Window(
        'Joguinho das mãos', layout_menu, element_justification='c', size=(750, 550))

    while True:
        event, values = menu_principal.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            quit()
        elif event == 'Dois Jogadores':
            menu_principal.close()
            nome_jogadores()
            janela_dois_jogadores()
        elif event == 'Regras':
            menu_principal.close()
            janela_regras()
    menu_principal.close()


tela_principal()