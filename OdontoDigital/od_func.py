import sqlite3
import datetime
data = datetime.datetime.now()
meses_31 = [ 1, 3, 5, 7, 8, 10, 12] #Lista de meses com 31 dias para a checagem de datas na parte de consultas.

#Funções dos Dentistas
def cadastrarDentista():
    '''Realiza o cadastro de dentistas no banco de dados.'''
    nome = input("Nome: ")
    rg = input("RG: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    crm = input("CRM: ")
    sql = "INSERT INTO dentistas (nome, rg, cpf, telefone, email, crm) VALUES (?,?,?,?,?,?)"
    con = sqlite3.connect("odonto.db")
    cursor = con.cursor()
    cursor.execute(sql, [nome, rg, cpf, telefone, email, crm])
    con.commit()
    con.close()

def listarDentista():
    '''Lista todos os dentistas cadastrados.'''
    con = sqlite3.connect("odonto.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dentistas;")
    dentistas = cursor.fetchall()
    con.commit()
    con.close()
    print('\nLISTA DE DENTISTAS:\n')
    for i in dentistas:
        print(f'ID: {i[0]} | Nome: {i[1]} | RG: {i[2]} | CPF: {i[3]} | Telefone: {i[4]} | E-mail: {i[5]} | CRM: {i[6]} ')
    print()

def pesquisarDentista(idDentista):
    '''Retorna somente o registro especificado pelo ID.'''
    con = sqlite3.connect("odonto.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dentistas WHERE ID=?;", [idDentista])
    dentistas = cursor.fetchall()
    for i in dentistas:
        print(f'ID: {i[0]} | Nome: {i[1]} | RG: {i[2]} | CPF: {i[3]} | Telefone: {i[4]} | E-mail: {i[5]} | CRM: {i[6]}')
    con.commit()
    con.close()

def atualizarDentista():
    '''Atualiza um registro específico no Banco.'''
    listarDentista()
    idDentista = int(input('\nInsira o ID do registro que deseja atualizar: '))
    pesquisarDentista(idDentista)
    print('---------------------------------------------------------------------------------------------------------------------------------')
    nome = input("Nome: ")
    rg = input("RG: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    crm = input("CRM: ")
    con = sqlite3.connect("odonto.db")
    cursor = con.cursor()
    cursor.execute("UPDATE dentistas SET nome=?,rg=?,cpf=?,telefone=?,email=?,crm=? WHERE ID=?", 
    [nome, rg, cpf, telefone, email, crm, idDentista])
    con.commit()
    con.close()
    print()
    listarDentista()

def excluirDentista():
    '''Deleta um registro específico no banco.'''
    listarDentista()
    idDentista = int(input('\nInsira o ID do registro que deseja excluir: '))
    pesquisarDentista(idDentista)
    r = int(input('Tem certeza que deseja excluir esse registro? [1- Sim / 2- Não]: '))
    if r == 1:
        con = sqlite3.connect("odonto.db")
        cursor = con.cursor()
        cursor.execute("DELETE FROM dentistas WHERE ID=?", [idDentista])
        con.commit()
        con.close()
        print('Registro deletado com sucesso!')
        listarDentista()

#Funções dos Pacientes
def cadastrarPacientes():
    nome = input("Nome: ")
    rg = input("RG: ")
    cpf = input("CPF: ")
    endereco = input ('Endereço: (Rua, Número, Bairro, Cidade-UF): ')
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    sql = "INSERT INTO pacientes (nome, rg, cpf, telefone, email, endereco) VALUES (?,?,?,?,?,?)"
    con = sqlite3.connect("odonto.db")
    cursor = con.cursor()
    cursor.execute(sql, [nome, rg, cpf, telefone, email, endereco])
    con.commit()
    con.close()
    print('\nCadastro realizado com sucesso!\n')

def listarPacientes():
    con = sqlite3.connect("odonto.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM pacientes;")
    pacientes = cursor.fetchall()
    con.commit()
    con.close()
    print('\nLISTA DE Pacientes:\n')
    for i in pacientes:
        print(f'ID: {i[0]} | Nome: {i[1]} | RG: {i[2]} | CPF: {i[3]} | Telefone: {i[4]} | E-mail: {i[5]} | Endereço: {i[6]} ')
    print()

def pesquisarPacientes(idPacientes):
    con = sqlite3.connect("odonto.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM pacientes WHERE ID=?;", [idPacientes])
    Pacientes = cursor.fetchall()
    for i in Pacientes:
        print(f'ID: {i[0]} | Nome: {i[1]} | RG: {i[2]} | CPF: {i[3]} | Telefone: {i[4]} | E-mail: {i[5]} | Endereço: {i[6]}')
    con.commit()
    con.close()

def atualizarPacientes():
    listarPacientes()
    idPaciente = int(input('\nInsira o ID do registro que deseja atualizar: '))
    pesquisarPacientes(idPaciente)
    print('---------------------------------------------------------------------------------------------------------------------------------')
    nome = input("Nome: ")
    rg = input("RG: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    endereco = input("Endereço: ")
    con = sqlite3.connect("odonto.db")
    cursor = con.cursor()
    cursor.execute("UPDATE pacientes SET nome=?,rg=?,cpf=?,telefone=?,email=?,endereco=? WHERE ID=?", 
    [nome, rg, cpf, telefone, email, endereco, idPaciente])
    con.commit()
    con.close()
    listarPacientes()

def excluirPacientes():
    listarPacientes()
    idPaciente = int(input('\nInsira o ID do registro que deseja excluir: '))
    pesquisarPacientes(idPaciente)
    r = int(input('Tem certeza que deseja excluir esse registro? [1- Sim / 2- Não]: '))
    if r == 1:
        con = sqlite3.connect("odonto.db")
        cursor = con.cursor()
        cursor.execute("DELETE FROM dentistas WHERE ID=?", [idPaciente])
        con.commit()
        con.close()
        print('\nRegistro deletado com sucesso!')
        listarPacientes()
  
#Funções das consultas
def validar_data(mes, dia, ano):
    '''Função que checa se a data é existente.'''
    if int(mes) in meses_31: #Verifica se o mês tem ou não tem 31 dias.
        if int(dia) > 31:
            return False
        else:
            return True
    elif int(mes) == 2: #No caso do mês ser Fevereiro, verifica se o ano é bissexto, onde fevereiro tem 29 dias.
        if (int(ano) % 4) == 0:
            if (int(ano) % 100) != 0:
                if int(dia) > 29:
                    return False
                else:
                    return True
            elif (int(ano) % 400) == 0:
                if int(dia) > 29:
                    return False
                else:
                    return True
        else:
            if int(dia) > 28:
                return False
            else:
                return True
    elif int(mes) > 12 or int(mes) < 1:
        return False
    else:
        if int(dia) > 30:
            return False
        else:
            return True

def checar_data(mes, dia, ano): 
    '''Função que checa se é possível marcar uma consulta na data escolhida.'''
    if int(ano) < data.year:
        print('[ERRO] Impossível marcar consultas para esta data!')
        return False
    elif int(ano) == data.year:
            if int(mes) < int(data.month):
                print('[ERRO] Impossível marcar consultas para esta data!')
                return False
            elif int(mes) == int(data.month):
                if int(dia) <= int(data.day):
                    print('[ERRO] Impossível marcar consultas para esta data!')
                    return False
            else:
                if validar_data(mes, dia, ano) == True:
                    return True
                else:
                    print('[ERRO] Essa data é inválida.')
                    return False
    else:
        if validar_data(mes, dia, ano) == True:
            return True
        else:
            print('[ERRO] Essa data é inválida.')
            return False

def checar_horario(hora, minuto):
    '''Função que checa se o horário é válido.'''
    if int(hora) > 18 or int(hora) < 7 or int(hora) == 12:
        print('[ERRO] Este horário não corresponde ao horário de funcionamento.')
        return False
    elif int(minuto) != 00 and int(minuto) != 30:
        print('[ERRO] As consultas só podem ser marcadas de meia em meia hora.')
        return False
    else:
        return True

def checarDentista(dentista, data, hora):
    '''Função que checa se o dentista já tem consulta marcada para a data e horário ou se o paciente já tem uma consulta pendente.'''
    con = sqlite3.connect("odonto.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM consultas WHERE nomeDentista=?", [dentista])
    den = cursor.fetchall()
    if len(den) > 0:
        for i in den:
            if i[3] == data and i[4] == hora:
                print('\nEsse dentista já tem consulta marcada nesta data e horário.')
                return False
    con.commit()
    con.close()
    return True

def checarPaciente(paciente):
    con = sqlite3.connect("odonto.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM consultas WHERE nomePaciente=?", [paciente])
    pac = cursor.fetchall()
    con.commit()
    con.close()
    if len(pac) > 0:
        print('\nEsse paciente já tem uma consulta marcada.')
        return False
    return True

def cadastrarConsulta():
    '''Função para cadastrar uma nova consulta.'''
    while True:
        listarDentista()
        idDentista = int(input('Id do(a) dentista: '))
        listarPacientes()
        idPaciente = int(input('Id do(a) paciente: '))
        dataCompleta = input('Data da Consulta (dia/mês/ano): ')
        dia, mes, ano = dataCompleta.split('/')
        while checar_data(mes, dia, ano) == False:
            dataCompleta = input('Data da Consulta (dia/mês/ano): ')
            dia, mes, ano = dataCompleta.split('/')
        horario = input('Horário (hh:00 ou hh:30): ')
        hora, minuto = horario.split(':')
        while checar_horario(hora, minuto) == False:
            horario = input('Horário (hh:00 ou hh:30): ')
            hora, minuto = horario.split(':')
        con = sqlite3.connect("odonto.db")
        cursor = con.cursor()
        cursor.execute("SELECT Nome FROM dentistas WHERE ID=?;", [idDentista])
        dentistas = cursor.fetchone()
        dentista = dentistas[0]
        cursor.execute("SELECT Nome FROM pacientes WHERE ID=?;", [idPaciente])
        pacientes = cursor.fetchone()
        paciente = pacientes[0]
        if checarDentista(dentista, dataCompleta, horario) == True and checarPaciente(paciente) == True:
            cursor.execute("INSERT INTO consultas (NomeDentista, NomePaciente, Data, Hora) VALUES(?,?,?,?)", [dentista, paciente, dataCompleta, horario])
            print('Cadastro realizado com sucesso!')
        else:
            print('\nNão foi possível cadastrar.')
        con.commit()
        con.close()
        r = int(input('\nContinuar Cadastrando? [1 - Sim / 2 - Não]: '))
        print()
        if r == 2:
            break

def listarConsulta():
    '''Lista todas as consultas cadastradas.'''
    con = sqlite3.connect("odonto.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM consultas;")
    consultas = cursor.fetchall()
    con.commit()
    con.close()
    print('\nLISTA DE CONSULTAS:\n')
    for i in consultas:
        print(f'ID: {i[0]} | Dentista: {i[1]} | Paciente: {i[2]} | Data: {i[3]} | Hora: {i[4]}')
    print()

def pesquisaConsultaDentista():
    '''Lista as consultas que um determinado dentista tem marcadas. Pesquisa feita através do nome.'''
    d= input('Nome do(a) dentista: ')
    print()
    dentista = f'%{d}%'
    con = sqlite3.connect('odonto.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM consultas WHERE nomeDentista LIKE ?", [dentista])
    consultas = cursor.fetchall()
    for i in consultas:
        print(f'ID: {i[0]} | Dentista: {i[1]} | Paciente: {i[2]} | Data: {i[3]} | Hora: {i[4]}')
    print()
    con.commit()
    con.close()

def pesquisaConsultaPaciente():
    '''Lista a consulta que um determinado paciente tem marcada. Pesquisa feita através do nome.'''
    p = input('Nome do(a) paciente: ')
    print()
    paciente = f'%{p}%'
    con = sqlite3.connect('odonto.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM consultas WHERE nomePaciente LIKE ?", [paciente])
    consultas = cursor.fetchall()
    for i in consultas:
        print(f'ID: {i[0]} | Dentista: {i[1]} | Paciente: {i[2]} | Data: {i[3]} | Hora: {i[4]}')
    print()
    con.commit()
    con.close()

def pesquisaConsultaId(idConsulta):
    '''Função que destaca um cadastro específico através do id'''
    con = sqlite3.connect('odonto.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM consultas WHERE id=?", [idConsulta])
    consultas = cursor.fetchall()
    for i in consultas:
        print(f'ID: {i[0]} | Dentista: {i[1]} | Paciente: {i[2]} | Data: {i[3]} | Hora: {i[4]}')
    print()
    con.commit()
    con.close()

def atualizarConsulta():
    listarConsulta()
    idConsulta = int(input('Digite o ID da consulta que será atualizada: '))
    print('---------------------------------------------------------------------------------------------------------------------------------')
    pesquisaConsultaId(idConsulta)
    r = int(input('Deseja atualizar este cadastro? [1- Sim / 2- Não]: '))
    if r == 1:
        listarDentista()
        idDentista = int(input('Id do Dentista: '))
        idPaciente = int(input('Id do Paciente: '))
        dataCompleta = input('Data da Consulta (dia/mês/ano): ')
        dia, mes, ano = dataCompleta.split('/')
        while checar_data(mes, dia, ano) == False:
            dataCompleta = input('Data da Consulta (dia/mês/ano): ')
            dia, mes, ano = dataCompleta.split('/')
        horario = input('Horário (hh:00 ou hh:30): ')
        hora, minuto = horario.split(':')
        while checar_horario(hora, minuto) == False:
            horario = input('Horário (hh:00 ou hh:30): ')
            hora, minuto = horario.split(':')
        con = sqlite3.connect("odonto.db")
        cursor = con.cursor()
        cursor.execute("SELECT Nome FROM dentistas WHERE ID=?;", [idDentista])
        dentistas = cursor.fetchone()
        dentista = dentistas[0]
        cursor.execute("SELECT Nome FROM pacientes WHERE ID=?;", [idPaciente])
        pacientes = cursor.fetchone()
        paciente = pacientes[0]
        if checarDentista(dentista, dataCompleta, horario) == True:
            cursor.execute("UPDATE consultas SET nomeDentista=?,nomePaciente=?,data=?,hora=? WHERE ID=?", [dentista, paciente, dataCompleta, horario, idConsulta])
            print('Cadastro atualizado com sucesso!')
        else:
            print('\nNão foi possível atualizar.')
        con.commit()
        con.close()
        print()

def excluirConsulta():
    listarConsulta()
    idConsulta = int(input('Digite o ID da consulta que será excluída: '))
    pesquisaConsultaId(idConsulta)
    r = int(input('Deseja mesmo excluir esse cadastro? [1- Sim / 2- Não]: '))
    if r == 1:
        con = sqlite3.connect('odonto.db')
        cursor = con.cursor()
        cursor.execute('DELETE FROM consultas WHERE id=?', [idConsulta])
        con.commit()
        con.close()
        print('\nConsulta deletada com sucesso!\n')

# Funções de Clínicas
def cadastrarClinica():
    nome = input("Nome da clínica: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone de contato: ")
    cnpj = input("CNPJ: ")
    sobre = input("Descrição breve: ")
    con = sqlite3.connect('odonto.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO clinicas (nome, endereco, telefone, cnpj, sobre) VALUES (?,?,?,?,?)", [nome, endereco, telefone, cnpj, sobre])
    con.commit()
    con.close()

def listarClinicas():
    con = sqlite3.connect('odonto.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM clinicas')
    clinicas = cursor.fetchall()
    con.commit()
    con.close()
    print('\nLISTA DE CLÍNICAS\n')
    for t in clinicas:
        print(f'ID: {t[0]} | Nome: {t[1]} | Endereço: {t[2]} | Telefone: {t[3]} | CNPJ: {t[4]} \nSobre: {t[5]}')
    print()

def pesquisarClinicasNome():
    n = input('Informe o nome da clínica: ')
    nome = f'%{n}%'
    con = sqlite3.connect('odonto.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM clinicas WHERE nome LIKE ?', [nome])
    clinicas = cursor.fetchall()
    con.commit()
    con.close()
    for t in clinicas:
        print(f'ID: {t[0]} | Nome: {t[1]} | Endereço: {t[2]} | Telefone: {t[3]} | CNPJ: {t[4]} \nSobre: {t[5]}')
    print()

def pesquisarClinicasID(idClinica):
    con = sqlite3.connect('odonto.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM clinicas WHERE id = ?', [idClinica])
    clinicas = cursor.fetchall()
    con.commit()
    con.close()
    for t in clinicas:
        print(f'ID: {t[0]} | Nome: {t[1]} | Endereço: {t[2]} | Telefone: {t[3]} | CNPJ: {t[4]} \nSobre: {t[5]}')
    print()

def atualizarClinica():
    listarClinicas()
    idClinica = 'Digite o ID da clínica que você deseja atualizar: '
    print('---------------------------------------------------------------------------------------------------------------------------------')
    pesquisarClinicasID(idClinica)
    r = int(input('Deseja atualizar este cadastro? [1- Sim / 2- Não]: '))
    if r == 1:
        nome = input("Nome da clínica: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone de contato: ")
        cnpj = input("CNPJ: ")
        sobre = input("Descrição breve: ")
        con = sqlite3.connect('odonto.db')
        cursor = con.cursor()
        cursor.execute('UPDATE clinicas SET nome=?, endereco=?, telefone=?, cnpj=?, sobre=? WHERE id=?', [nome, endereco, telefone, cnpj, sobre, idClinica])
        con.commit()
        con.close()
        listarClinicas()

def excluirClinica():
    listarClinicas()
    idClinica = int(input('Digite o ID da clínica que será excluída: '))
    pesquisarClinicasID(idClinica)
    r = int(input('Deseja mesmo excluir este cadastro? [1- Sim / 2- Não]: '))
    if r == 1:
        con = sqlite3.connect('odonto.db')
        cursor = con.cursor()
        cursor.execute('DELETE FROM clinicas WHERE id = ?', [idClinica])
        con.commit()
        con.close()
        print('\nRegistro deletado com sucesso!')
        listarClinicas()
