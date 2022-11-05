import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime as dt
import pandas as pd



############################################### função para abrir janela de produção ##########################################################
def menu_producao():
    produtos_cadastrados = pd.read_csv('lista_produtos.csv')
    lista_produtos_cadastrados = produtos_cadastrados.CODIGO.to_list()

    janela_producao = tk.Toplevel()
    janela_producao.title('Produção')
    

    def refresh():
        entry_produto.delete(0,'end')
        entry_quantidade.delete(0,'end')

    def confirmar_producao():
        produto = entry_produto.get()
        quantidade = entry_quantidade.get()
        data_producao = (dt.datetime.now()).strftime("%d/%m/%Y")

        if  produto and quantidade is not None:
            lista_producao = open('lista_producao.csv', 'a+t', encoding='utf-8')
            lista_producao.write( produto + ',' + quantidade +','+ data_producao +  "\n")
            messagebox.showinfo(title='Produção', message='Entrada realizada com sucesso!')
            refresh()
        else:
            messagebox.showwarning(title='Produção',message='Preencha todos os campos!')



    label_produto = tk.Label(janela_producao,text='PRODUTO:')
    label_produto.grid(row=1, column=0, padx=10, pady=10)
    entry_produto = ttk.Combobox(janela_producao,values=lista_produtos_cadastrados)
    entry_produto.grid(row=1,column=1, padx=10, pady=10)

    label_quantidade = tk.Label(janela_producao,text='QUANTIDADE:')
    label_quantidade.grid(row=1,column=2,padx=10, pady=10)
    entry_quantidade = tk.Entry(janela_producao)
    entry_quantidade.grid(row=1, column=3, padx=10, pady=10)

    botao_producao = tk.Button(janela_producao,text='Confirmar Produção', command=confirmar_producao)
    botao_producao.grid(row=2, column=3, padx=10, pady=10)
    


########################################### função para abrir janela de entradas ####################################################################
def entradas():
    # lista de materiais
    materiais_cadastrados = pd.read_csv('lista_materiais.csv') 
    lista_materiais_cadastrados = materiais_cadastrados.CODIGO.to_list()
    # lista de fornecedores
    fornecedores_cadastrados = pd.read_csv('lista_stakeholders.csv')
    lista_fornecedores_cadastrados = fornecedores_cadastrados.query('CLASSE == "FORNECEDOR"').NOME.to_list()

    janela_entrada = tk.Toplevel()

    janela_entrada.title('Entrada de Materiais')

    def refresh():
        entry_material.delete(0,'end')
        entry_quantidade.delete(0,'end')
        entry_unidade.delete(0,'end')
        entry_fornecedor.delete(0,'end')
        entry_nf.delete(0,'end')


    def entrada_material():
        material = entry_material.get().upper()
        quantidade = entry_quantidade.get()
        unidade = entry_unidade.get().upper()
        forncedor = entry_fornecedor.get().upper()
        nf = entry_nf.get().upper()
        data_entrada = (dt.datetime.now()).strftime("%d/%m/%Y")

        if  material and quantidade and unidade and forncedor is not None:
            lista_clientes = open('lista_entrada.csv', 'a+t', encoding='utf-8')
            lista_clientes.write(material + ',' + quantidade + ',' + unidade +','+ forncedor + ',' + nf + ','+ data_entrada + "\n")
            messagebox.showinfo(title='Entrada de Materiais', message='Entrada realizada com sucesso!')
            refresh()
        
        else:
            messagebox.showwarning(title='Entrada de Materiais',message='Preencha todos os campos!')



    label_material = tk.Label(janela_entrada,text='MATERIAL:')
    label_material.grid(row=1, column=0, padx=10, pady=10)
    entry_material = ttk.Combobox(janela_entrada,values=lista_materiais_cadastrados)
    entry_material.grid(row=1, column=1, padx=10, pady=10)

    label_quantidade = tk.Label(janela_entrada,text='QUANTIDADE:')
    label_quantidade.grid(row=2,column=0, padx=10, pady=10)
    entry_quantidade = tk.Entry(janela_entrada)
    entry_quantidade.grid(row=2, column=1, padx=10, pady=10)

    label_unidade = tk.Label(janela_entrada,text='UNIDADE')
    label_unidade.grid(row=2, column=3, padx=10, pady=10)
    entry_unidade = ttk.Combobox(janela_entrada,values=['PÇ','PCT','KG'])
    entry_unidade.grid(row=2, column=4)

    label_fornecedor = tk.Label(janela_entrada,text='FORNECEDOR:')
    label_fornecedor.grid(row=3,column=0,padx=10,pady=10)
    entry_fornecedor = ttk.Combobox(janela_entrada,values = lista_fornecedores_cadastrados)
    entry_fornecedor.grid(row=3, column=1, padx=10, pady=10)

    label_nf = tk.Label(janela_entrada,text='NF:')
    label_nf.grid(row=3, column=3, padx=10, pady=10)
    entry_nf = tk.Entry(janela_entrada)
    entry_nf.grid(row=3, column=4, padx=10, pady=10)

    botao_entrada_material = tk.Button(janela_entrada,text='Confirmar Entrada', command=entrada_material)
    botao_entrada_material.grid(row=4, column=4, padx=15, pady=15, columnspan=5)

################################################## função para abrir janela de saidas ################################################################

def saidas():
    # lista clientes
    clientes_cadastrados = pd.read_csv('lista_stakeholders.csv')
    lista_clientes_cadastrados = clientes_cadastrados.query('CLASSE == "CLIENTE"').NOME.to_list()

    #lista produtos
    produtos_cadastrados = pd.read_csv('lista_produtos.csv')
    lista_produtos_cadastrados = produtos_cadastrados.CODIGO.to_list()

    janela_saidas = tk.Toplevel()
    janela_saidas.title('Saída')

    def refresh():
        entry_cliente.delete(0,'end')
        entry_produto.delete(0,'end')
        entry_quantidade.delete(0,'end')

    def confirmar_saida():
        cliente = entry_cliente.get()
        produto = entry_produto.get()
        quantidade = entry_quantidade.get()
        data_saida = (dt.datetime.now()).strftime("%d/%m/%Y")

        if cliente and produto and quantidade is not None:
            lista_saida = open('lista_saida.csv', 'a+t', encoding='utf-8')
            lista_saida.write(cliente + ',' + produto + ',' + quantidade +','+ data_saida +  "\n")
            messagebox.showinfo(title='Saída', message='Saída realizada com sucesso!')
            refresh()
        else:
            messagebox.showwarning(title='Saída',message='Preencha todos os campos!')


    label_cliente = tk.Label(janela_saidas,text='Cliente:')
    label_cliente.grid(row=1, column=0, padx=10, pady=10)
    entry_cliente = ttk.Combobox(janela_saidas,values=lista_clientes_cadastrados)
    entry_cliente.grid(row=1,column=1, padx=10, pady=10)

    label_produto = tk.Label(janela_saidas,text='PRODUTO:')
    label_produto.grid(row=2, column=0, padx=10, pady=10)
    entry_produto = ttk.Combobox(janela_saidas,values=lista_produtos_cadastrados)
    entry_produto.grid(row=2,column=1, padx=10, pady=10)

    label_quantidade = tk.Label(janela_saidas,text='QUANTIDADE:')
    label_quantidade.grid(row=2,column=2,padx=10, pady=10)
    entry_quantidade = tk.Entry(janela_saidas)
    entry_quantidade.grid(row=2, column=3, padx=10, pady=10)

    botao_saida = tk.Button(janela_saidas,text='Confirmar Saída', command=confirmar_saida)
    botao_saida.grid(row=3, column=3, padx=10, pady=10)

######################################### função para abrir menu de cadastros #############################################################


def abre_menu_cadastros():

    janela_menu_cadastros = tk.Toplevel()
    janela_menu_cadastros.title('Menu de Cadastros')

#######################################################################
    def cadastro_stakeholder():
        lista_estados_brasil = ['SP','PR','SC','RS','MS','RO','AC','AM','RR','PA','AP','MA','RN','PB','PE','AL','SE','BA','MG','RJ','MT','GO','DF','PI','CE','ES']


        janela_clientes = tk.Toplevel()


        # função para resetar labels
        def refresh():
            entry_bairro.delete(0,'end')
            entry_cidade.delete(0,'end')
            entry_cliente.delete(0,'end')
            entry_cnpj_cpf.delete(0,'end')
            entry_email.delete(0,'end')
            entry_estado.delete(0,'end')
            entry_numero.delete(0,'end')
            entry_rua.delete(0,'end')
            entry_tipo_pessoa.delete(0,'end')
            entry_telefone.delete(0,'end')
            entry_classe.delete(0,'end')

        # função de cadastro
        def cadastrar_cliente():

            nome = str(entry_cliente.get()).upper()
            classe = str(entry_classe.get())
            tipo = str(entry_tipo_pessoa.get())
            cnpj_cpf = str(entry_cnpj_cpf.get())
            if tipo == 'PJ':
                cnpj_cpf = cnpj_cpf[0:3] + '.' + cnpj_cpf[3:6] + '/' + cnpj_cpf[6:10] + '-' + cnpj_cpf[10:12] 
            else:
                cnpj_cpf = cnpj_cpf[0:3] + '.' + cnpj_cpf[3:6] + '.' + cnpj_cpf[6:9] + '-' + cnpj_cpf[9:11]

            rua = str(entry_rua.get()).upper()
            bairro = str(entry_bairro.get()).upper()
            cidade = str(entry_cidade.get()).upper()
            estado = str(entry_estado.get())
            telefone = str(entry_telefone.get())
            email = str(entry_email.get()).lower()
            data_cadastro = (dt.datetime.now()).strftime("%d/%m/%Y")



            if  nome and tipo and cidade and cnpj_cpf and telefone is not None:
                    lista_clientes = open('lista_stakeholders.csv', 'a+t', encoding='utf-8')
                    lista_clientes.write(nome + ',' + classe + ',' + tipo + ',' + cnpj_cpf +','+ rua + ',' + bairro + ',' + cidade + ',' + estado + ',' + telefone + ',' + email + ',' + data_cadastro +"\n")
                    messagebox.showinfo(title='Cadastro de Stakeholder', message='Cadastro realizado com sucesso!')
                    refresh()
                    
            else:
                messagebox.showwarning(title='Cadastro de Stakeholder',message='Preencha todos os campos!')



        # Título da janela
        janela_clientes.title('Cadastro de Stakeholder')

        # nome cliente
        label_cliente = tk.Label(janela_clientes,text='Nome:')
        label_cliente.grid(row=1, column=0, padx=10, pady=10)

        entry_cliente = tk.Entry(janela_clientes)
        entry_cliente.grid(row=1, column=2, padx=10, pady=10)

        # dados cliente

        label_classe = tk.Label(janela_clientes,text='Classe')
        label_classe.grid(row=1, column=3, padx=10,pady=10)
        entry_classe = ttk.Combobox(janela_clientes,values=['CLIENTE','FORNECEDOR'])
        entry_classe.grid(row=1, column=4, padx=10, pady=10)

        label_tipo_pessoa = tk.Label(janela_clientes,text='Tipo:')
        label_tipo_pessoa.grid(row=2, column=3, padx=10, pady=10)
        entry_tipo_pessoa = ttk.Combobox(janela_clientes,values=['PJ','PF'])
        entry_tipo_pessoa.grid(row=2, column=4,padx=10, pady=10)

        label_cnpj_cpf = tk.Label(janela_clientes,text='CNPJ/CPF')
        label_cnpj_cpf.grid(row=2, column=0, padx=10, pady=10)
        entry_cnpj_cpf = tk.Entry(janela_clientes)
        entry_cnpj_cpf.grid(row=2, column=2, padx=10, pady=10)

        # endereço cliente
        label_rua = tk.Label(janela_clientes,text='Rua:')
        label_rua.grid(row=3, column=0,  pady=10)
        entry_rua = tk.Entry(janela_clientes)
        entry_rua.grid(row=3, column=2, padx=10, pady=10)

        label_numero = tk.Label(janela_clientes,text='Número:')
        label_numero.grid(row=3, column=3)
        entry_numero = tk.Entry(janela_clientes)
        entry_numero.grid(row=3, column=4, padx=10, pady=10)

        label_bairro = tk.Label(janela_clientes,text='Bairro:')
        label_bairro.grid(row=4, column=0)
        entry_bairro = tk.Entry(janela_clientes)
        entry_bairro.grid(row=4, column=2, padx=10, pady=10)

        label_cidade = tk.Label(janela_clientes,text='Cidade:')
        label_cidade.grid(row=5, column=0)
        entry_cidade = tk.Entry(janela_clientes)
        entry_cidade.grid(row=5, column=2, padx=10, pady=10)

        label_estado = tk.Label(janela_clientes,text='UF:')
        label_estado.grid(row=5, column=3)
        entry_estado = ttk.Combobox(janela_clientes,values=lista_estados_brasil)
        entry_estado.grid(row=5, column=4)

        # contato cliente
        label_telefone = tk.Label(janela_clientes,text='Telefone:')
        label_telefone.grid(row=6, column=0)
        entry_telefone = tk.Entry(janela_clientes)
        entry_telefone.grid(row=6, column=2)

        label_email = tk.Label(janela_clientes,text='Email:')
        label_email.grid(row=7, column=0, padx=10, pady=10)
        entry_email = tk.Entry(janela_clientes)
        entry_email.grid(row=7, column=2, padx=10, pady=10)

        # botao cadastro
        botao_cadastro_cliente = tk.Button(janela_clientes,text='Cadastrar Stakeholder', command=cadastrar_cliente)
        botao_cadastro_cliente.grid(row=8, column=0, padx=15, pady=15, columnspan=5)
#######################################################################################

    def cadastro_materiais():

        janela_materiais = tk.Toplevel()

        def refresh():
            entry_codigo.delete(0,'end')
            entry_tipo.delete(0,'end')
            entry_item.delete(0,'end')
            entry_medida.delete(0,'end')
            entry_descricao.delete(0,'end')
            entry_unidade.delete(0,'end')


        def cadastrar_material():
            codigo = entry_codigo.get().upper()
            tipo = entry_tipo.get().upper()
            item = entry_item.get().upper()
            medida = entry_medida.get().upper()
            descricao = entry_descricao.get().upper()
            unidade = entry_unidade.get().upper()
            data_cadastro = (dt.datetime.now()).strftime("%d/%m/%Y")

            if  codigo and tipo and item and unidade is not None:
                lista_clientes = open('lista_materiais.csv', 'a+t', encoding='utf-8')
                lista_clientes.write(codigo + ',' + item + ',' + tipo +','+ medida + ',' + descricao + ',' + unidade + ',' + data_cadastro + "\n")
                messagebox.showinfo(title='Cadastro de Materiais', message='Cadastro realizado com sucesso!')
                refresh()
            
            else:
                messagebox.showwarning(title='Cadastro de Clientes',message='Preencha todos os campos!')



        janela_materiais.title('Cadastro de Materiais')


        label_codigo = tk.Label(janela_materiais,text='CÓDIGO:')
        label_codigo.grid(row=1, column=0, padx=10, pady=10)
        entry_codigo = tk.Entry(janela_materiais)
        entry_codigo.grid(row=1, column=1, padx=10, pady=10)

        label_tipo = tk.Label(janela_materiais,text='TIPO:')
        label_tipo.grid(row=1, column=2, padx=10, pady=10)
        entry_tipo = ttk.Combobox(janela_materiais,values=['Materia Prima','Ferramenta','Material Escritorio'])
        entry_tipo.grid(row=1, column=3, padx=10, pady=10)

        label_item = tk.Label(janela_materiais,text='ITEM:')
        label_item.grid(row=2, column=0, padx=10, pady=10)
        entry_item = tk.Entry(janela_materiais)
        entry_item.grid(row=2,column=1, padx=10, pady=10)

        label_medida = tk.Label(janela_materiais,text='MEDIDA(mm)')
        label_medida.grid(row=2, column=2, padx=10, pady=10)
        entry_medida = tk.Entry(janela_materiais)
        entry_medida.grid(row=2, column=3, padx=10, pady=10)

        label_descricao = tk.Label(janela_materiais,text='DESCRIÇÃO')
        label_descricao.grid(row=3, column=0, padx=10, pady=10)
        entry_descricao = tk.Entry(janela_materiais)
        entry_descricao.grid(row=3, column=1, padx=10, pady=10)

        label_unidade = tk.Label(janela_materiais,text='UNIDADE:')
        label_unidade.grid(row=3, column=2, padx=10, pady=10)
        entry_unidade = ttk.Combobox(janela_materiais,values=['PCT','PÇ','KG','L','UN.'])
        entry_unidade.grid(row=3, column=3, padx=10, pady=10)


        botao_cadastro_material = tk.Button(janela_materiais,text='Cadastrar Material', command=cadastrar_material)
        botao_cadastro_material.grid(row=4, column=3, padx=15, pady=15, columnspan=5)
###################################################################################################
    def cadastro_produtos():

        janela_produtos = tk.Toplevel()

        def refresh():
            entry_codigo_produto.delete(0,'end')
            entry_tipo.delete(0,'end')
            entry_chanfro.delete(0,'end')
            entry_fehcamento1.delete(0,'end')
            entry_liga_toco1.delete(0,'end')
            entry_fehcamento2.delete(0,'end')
            entry_liga_toco2.delete(0,'end')
            entry_toco.delete(0,'end')
            entry_descricao.delete(0,'end')

        def cadastrar_produto():
            
            codigo = entry_codigo_produto.get()
            tipo = entry_tipo.get()
            chanfro = entry_chanfro.get()
            fech1 = entry_fehcamento1.get()
            liga1 = entry_liga_toco1.get()
            fech2 = entry_fehcamento2.get()
            liga2 = entry_liga_toco2.get()
            toco = entry_toco.get()
            descricao = entry_descricao.get()
            data_cadastro = (dt.datetime.now()).strftime("%d/%m/%Y")

            if  codigo and tipo and chanfro and fech1 and liga1 and fech2 and liga2 and toco is not None:
                lista_clientes = open('lista_produtos.csv', 'a+t', encoding='utf-8')
                lista_clientes.write(codigo + ',' + tipo + ',' + chanfro +','+ fech1 + ',' + liga1 + ','+ fech2 + ',' + liga2 + ',' + toco + ',' + descricao + ',' + data_cadastro + "\n")
                messagebox.showinfo(title='Entrada de Materiais', message='Entrada realizada com sucesso!')
                refresh()
            
            else:
                messagebox.showwarning(title='Entrada de Materiais',message='Preencha todos os campos!')


        # labels e widgets
        label_codigo_produto = tk.Label(janela_produtos,text='CÓDIGO:')
        label_codigo_produto.grid(row=1, column=0, padx=10, pady=10)
        entry_codigo_produto = tk.Entry(janela_produtos)
        entry_codigo_produto.grid(row=1, column=1, padx=10, pady=10)

        label_tipo = tk.Label(janela_produtos,text='TIPO:')
        label_tipo.grid(row=1,column=2, padx=10, pady=10)
        entry_tipo = ttk.Combobox(janela_produtos,values=['PALLET'])
        entry_tipo.grid(row=1, column=3, padx=10, pady=10)

        label_qtde_pecas = tk.Label(janela_produtos,text='QUANTIDADE DE PEÇAS POR PALLET')
        label_qtde_pecas.grid(row=2, column=0, padx=10, pady=10, columnspan=4)

        label_chanfro = tk.Label(janela_produtos,text='CHANFRO:')
        label_chanfro.grid(row=3, column=0, padx=10, pady=10)
        entry_chanfro = tk.Entry(janela_produtos)
        entry_chanfro.grid(row=3, column=1, padx=10, pady=10)

        label_fechamento1 = tk.Label(janela_produtos,text='FECHAMENTO 1:')
        label_fechamento1.grid(row=3, column=2, padx=10, pady=10)
        entry_fehcamento1 = tk.Entry(janela_produtos)
        entry_fehcamento1.grid(row=3, column=3, padx=10, pady=10)

        label_liga_toco1 = tk.Label(janela_produtos,text='LIGA-TOCO 1:')
        label_liga_toco1.grid(row=4, column=0, padx=10, pady=10)
        entry_liga_toco1 = tk.Entry(janela_produtos)
        entry_liga_toco1.grid(row=4, column=1, padx=10, pady=10)

        label_fechamento2 = tk.Label(janela_produtos,text='FECHAMENTO 2:')
        label_fechamento2.grid(row=4, column=2, padx=10, pady=10)
        entry_fehcamento2 = tk.Entry(janela_produtos)
        entry_fehcamento2.grid(row=4, column=3, padx=10, pady=10)

        label_liga_toco2 = tk.Label(janela_produtos,text='LIGA-TOCO 2:')
        label_liga_toco2.grid(row=5, column=0, padx=10, pady=10)
        entry_liga_toco2 = tk.Entry(janela_produtos)
        entry_liga_toco2.grid(row=5, column=1, padx=10, pady=10)

        label_toco = tk.Label(janela_produtos,text='TOCO CORTADO:')
        label_toco.grid(row=5, column=2, padx=10, pady=10)
        entry_toco = tk.Entry(janela_produtos)
        entry_toco.grid(row=5, column=3, padx=10, pady=10)

        label_descricao = tk.Label(janela_produtos,text='DESCRIÇÃO:')
        label_descricao.grid(row=6, column=0, padx=10, pady=10)
        entry_descricao = tk.Entry(janela_produtos)
        entry_descricao.grid(row=6,column=1, padx=10, pady=10)

        botao_cadastro_produto = tk.Button(janela_produtos,text='Cadastrar Produto', command=cadastrar_produto)
        botao_cadastro_produto.grid(row=6, column=3, padx=10, pady=10)

#######################################################################################################


    botao_cadastro_stakeholders = tk.Button(janela_menu_cadastros, text='STAKEHOLDERS', command=cadastro_stakeholder)
    botao_cadastro_stakeholders.grid(row=1,column=0, padx=10, pady=10)

    botao_cadastro_material = tk.Button(janela_menu_cadastros, text='MATERIAIS', command=cadastro_materiais)
    botao_cadastro_material.grid(row=1, column=1, padx=10, pady=10)

    botao_cadastro_produtos = tk.Button(janela_menu_cadastros, text='PRODUTOS', command=cadastro_produtos)
    botao_cadastro_produtos.grid(row=1, column=2, padx=10, pady=10)


####################################função janela de estoque####################################################
def estoque():
    #produtos cadastrados
    produtos_cadastrados = pd.read_csv('lista_produtos.csv')
    lista_produtos_cadastrados = produtos_cadastrados.CODIGO.to_list()
    #materiais cadastrados
    materiais_cadastrados = pd.read_csv('lista_materiais.csv') 
    lista_materiais_cadastrados = materiais_cadastrados.CODIGO.to_list()

    # calcula estoque de produtos
    def calcula_estoque_produtos():
        item_produto = entry_produtos.get()
        producoes = pd.read_csv('lista_producao.csv')
        vendas = pd.read_csv('lista_saida.csv')
        soma_produto = producoes.query(f'COD_PRODUTO == "{item_produto}"').QUANTIDADE.sum()
        soma_vendas = vendas.query(f'COD_PRODUTO == "{item_produto}"').QUANTIDADE.sum()
        estoque_produtos = soma_produto - soma_vendas
        ##messagebox.showinfo(title=f'Estoque de Produto', message=f'Você possui {estoque_produtos} unidades de {item_produto} em estoque!')
        label_estoque_produto = tk.Label(janela_estoque, text=f'Há {estoque_produtos} unidades de {item_produto} em estoque!')
        label_estoque_produto.grid(row=4,column=0,padx=10,pady=10)



    janela_estoque = tk.Toplevel()
    janela_estoque.title('Estoque')

    label_produtos = tk.Label(janela_estoque,text='PRODUTOS')
    label_produtos.grid(row=1, column=0,padx=10,pady=10)

    entry_produtos = ttk.Combobox(janela_estoque, values=lista_produtos_cadastrados)
    entry_produtos.grid(row=2,column=0,padx=10, pady=10)

    botao_estoque_produto = tk.Button(janela_estoque,text='CALCULAR',command=calcula_estoque_produtos)
    botao_estoque_produto.grid(row=3,column=0, padx=10, pady=10)


##################################################################################################################

janela_menu = tk.Tk()
janela_menu.title('DURAPALLETS - MENU')



#botao cadastros
botao_cadastros = tk.Button(janela_menu, text='CADASTROS', command=abre_menu_cadastros)
botao_cadastros.grid(row=1,column=0, padx=10, pady=10)

#botao entradas
botao_entradas = tk.Button(janela_menu, text='ENTRADAS', command=entradas)
botao_entradas.grid(row=1,column=1,padx=10, pady=10)

#botao saidas
botao_saidas = tk.Button(janela_menu, text='SAÍDAS', command=saidas)
botao_saidas.grid(row=1,column=2,padx=10, pady=10)

#botao producao
botao_producao = tk.Button(janela_menu, text='PRODUÇÃO', command=menu_producao)
botao_producao.grid(row=1,column=3,padx=10, pady=10)

#botao estoque
botao_estoque = tk.Button(janela_menu, text='ESTOQUE', command=estoque)
botao_estoque.grid(row=1,column=4,padx=10, pady=10)


janela_menu.mainloop()