# Importar e declarar as lib's
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
# Transformar a matplot em janela do tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure


# Criar a janela principal do tinker
root = tk.Tk()


# Declaração das variaveis de escopo global
alunos = []
notas = []
newNotas= ""
qtdAlunos = ""


# Função para criar a janela do exemplo padrão requisitado no exercicio(a parte simples da coisa)
# Precisa ser declarada antes para ser utilizada no código da interface principal
def openExGraphWindow():
        # Criar a janela nova
        exGraphWindow = tk.Toplevel(root)
        exGraphWindow.title("Gráfico do exemplo pronto")
        exGraphWindow.geometry('900x600')
        exGraphWindow.config(bg = 'pink' )
        # Dados
        alunos = ['aluno1', 'aluno2','aluno3','aluno4','aluno5']
        notas = [6.3, 7.5, 9.2, 5.1, 6.8]

        # Calculo da média
        media = sum(notas)/len(notas)

        # Notas acima da média
        contagem = 0
        contagem2 = 0
        for i in range(0, len(notas),1):
                if(notas[i]> media):
                        contagem += 1
                else:
                        contagem2 += 1

        # Criar a figura, necessário para transformar o plot da matplot para uma janela do tkinter
        fig = Figure(figsize=(10,5), dpi= 100)


        # Criar subplots da figura, usado para criar o gráfico da média e o da quantidade de notas acima da média
        ax1 = fig.add_subplot(1,2,1) 
        ax2 = fig.add_subplot(1,2,2)

        # Título e labels do gráfico das notas e média
        ax1.set_xlabel('Alunos')
        ax1.set_ylabel('Notas')
        ax1.set_title('Gráfico da Média dos Alunos')


        # Gráfico da notas e da média
        ax1.bar(alunos,notas,color = 'blue')
        ax1.axhline(y=media, color = 'yellow', linestyle = '--',linewidth = 2,label=f'fmedia: {media:.2f}' )
        ax2.text(len(notas) - 0.5, media + 0.5, f'Media: {media:.2f}', color='red', ha='center', va='bottom')


        # Gráfico de quantas notas estão acima e abaixo da média 
        ax2.bar(['Acima da Média'], [contagem], color='green')
        ax2.bar(['Abaixo da média'],contagem2,color = 'red' )
        ax2.set_title('Quantidade de Notas Abaixo ou Acima da Média')


        # Adicionar o canvas do Matplotlib à janela Tkinter
        canvas = FigureCanvasTkAgg(fig, master=exGraphWindow)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)



# Função para converter as entradas de string para int/float
def dataconverting101():
        global alunos,notas,qtdAlunos,newNotas
        try:
        # Converter a string para int e preparar os arrays pra entrada de dados
                qtdInt = int(qtdAlunos)
                alunos= np.full(qtdInt,'')
                notas = np.full(qtdInt, 0)
        except ValueError:
                # Garantir que não aceite valores sem ser int
                print("The value is not a valid integer.")
        # Variável auxiliar para definir o array "alunos"
        glimmora = np.arange(1, qtdInt +1)
        alunos = np.char.add('aluno',glimmora.astype(str)) 
        # Separar a string que contém as notas da nova média
        tempList = newNotas.split()
        notas = []
        for num in tempList:
                try:
                        notas.append(float(num))
                except:
                        # Garantir que não aceite valores sem ser float
                        print(f"Warning: '{num}' is not a valid number and will be skipped.")        
        return alunos, notas



# Função para criar a janela de algum outro exemplo inserido pelo usuário(a parte que fez eu perder minha sanidade)
# Precisa ser declarada antes para ser utilizada no código da interface principal
def openGraphWindow():

        # Criar a janela nova
        GraphWindow = tk.Toplevel(root)
        GraphWindow.title("Gráfico das entradas do usuário")
        GraphWindow.geometry('900x600')
        GraphWindow.config(bg = 'pink' )

        # Definir os dados
        dataconverting101()


        # Calculo da média
        media = sum(notas)/len(notas)


        # Notas acima da média ou abaixo da média
        contagem = 0
        contagem2 = 0
        for i in range(0, len(notas),1):
                if(notas[i]> media):
                        contagem = contagem + 1
                else:
                        contagem2 = contagem2 +1

        # Criar a figura, necessário para transformar o plot da matplot para uma janela do tkinter
        fig = Figure(figsize=(10,5), dpi= 100)


        # Criar subplots da figura, usado para criar o gráfico da média e o da quantidade de notas acima da média
        ax1 = fig.add_subplot(1,2,1) 
        ax2 = fig.add_subplot(1,2,2)

        # Título e labels do gráfico das notas e média
        ax1.set_xlabel('Alunos')
        ax1.set_ylabel('Notas')
        ax1.set_title('Gráfico da Média dos Alunos')


        # Gráfico da notas e da média
        ax1.bar(alunos,notas,color = 'blue')
        ax1.axhline(y=media, color = 'yellow', linestyle = '--',linewidth = 2,label=f'fmedia: {media:.2f}' )
        ax2.text(len(notas) - 0.5, media + 0.5, f'Media: {media:.2f}', color='red', ha='center', va='bottom')


        # Gráfico de quantas notas estão acima e abaixo da média 
        ax2.bar(['Acima da Média'], [contagem], color='green')
        ax2.bar(['Abaixo da média'],contagem2,color = 'red' )
        ax2.set_title('Quantidade de Notas Abaixo ou Acima da Média')
        

        # Adicionar o canvas do Matplotlib à janela Tkinter
        canvas = FigureCanvasTkAgg(fig, master=GraphWindow)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)



# Criar a janela principal da interface
root.title("Calculadora de média")
root.geometry('900x600')
root.config(bg = 'pink' )

# Criando o layout da interface
lft_frame = tk.Frame(root, width= 200, height= 400, bg= 'skyblue')
lft_frame.grid(row = 0, column= 0, padx= 10, pady=5)

rgth_frame = tk.Frame(root, width= 650,height= 400, bg = 'skyblue')
rgth_frame.grid(row = 0, column= 1, padx= 10, pady = 5)

# Imagem da turtle :D
img = tk.PhotoImage(file="turtle.png")

# Criar as labels
tk.Label(rgth_frame, image= img).grid(row= 0, column= 0, padx=5, pady= 5)

# Toolbar é uma frame que auxilia no layout
tool_bar = tk.Frame(lft_frame,width = 180,height = 185,bg = 'skyblue')
tool_bar.grid(row = 2,column = 0, padx= 5, pady=5 )

# Declaração das entries(campos de texto da entrada de dados)
txt_qtd = tk.Entry(tool_bar, width= 5)
txt_qtd.grid(row=2,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')
txt_notas= tk.Entry(tool_bar, width= 5)
txt_notas.grid(row=4,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')

# Função que coleta os dados para gerar o gráfico novo
def collectData():
        global qtdAlunos,newNotas
        qtdAlunos = txt_qtd.get()
        newNotas = txt_notas.get()
        print(qtdAlunos,newNotas)
        return qtdAlunos, newNotas


# Função que permite 1 botão executar duas funções ao mesmo tempo
def combo():
        collectData()
        openGraphWindow()


# Botoes, e labels de todos os campos da interface
tk.Label(tool_bar,text= "outro exemplo" ,relief= 'raised').grid(row=0, column=0, padx= 5, pady=3, ipadx= 10)
tk.Label(tool_bar,text= "Quantidade de notas: " ,relief= 'raised').grid(row=1, column=0, padx= 5, pady=3, ipadx= 10)
tk.Label(tool_bar,text= "Notas: " ,relief= 'raised').grid(row=3, column=0, padx= 5, pady=3, ipadx= 10)
tk.Label(tool_bar, text="exemplo padrão: notas = [6.3, 7.5, 9.2, 5.1, 6.8]",relief= 'raised').grid(row=0, column=1,padx=5, pady=3, ipadx=10)

btn_padr = tk.Button(tool_bar,text= "rodar", command=openExGraphWindow).grid(row=1,  column=1,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')
btn_padr2 = tk.Button(tool_bar,text= "rodar", command=combo).grid(row=5,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')



# Iniciar o loop principal do Tkinter
root.mainloop()
