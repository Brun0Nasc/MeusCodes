import od_func

print('\n-----------------ODONTO DIGITAL-------------------')
while True:
    menu = int(input('O que deseja fazer? \n 1- Gerenciar dentistas \n 2- Gerenciar pacientes \n 3- Gerenciar consultas \n 4- Gerenciar clínicas \n 5- Opções de Gerenciadores \n 0- Sair \nR: '))
    print()
    if menu == 0:
        break
    elif menu == 1:
        while True:
            r = int(input('1- Cadastrar Dentista \n2- Listar Dentistas \n3- Atualizar Dentistas \n4- Excluir Dentista \n0- Voltar \nR: '))
            print()
            if r == 0:
                break
            elif r == 1:
                od_func.cadastrarDentista()
            elif r == 2:
                od_func.listarDentista()
            elif r == 3:
                od_func.atualizarDentista()
            elif r == 4:
                od_func.excluirDentista()
    elif menu == 2:
        while True:
            r = int(input('1- Cadastrar Paciente \n2- Listar Pacientes \n3- Atualizar Pacientes \n4- Excluir Pacientes \n0- Voltar \nR: '))
            print()
            if r == 0:
                break
            elif r == 1:
                od_func.cadastrarPacientes()
            elif r == 2:
                od_func.listarPacientes()
            elif r == 3:
                od_func.atualizarPacientes()
            elif r == 4:
                od_func.excluirPacientes()
    elif menu == 3:
        while True:
            r = int(input('1- Cadastrar Nova Consulta \n2- Listar Consultas Marcadas \n3- Pesquisar Consultas de Pacientes \n4- Pesquisar Consultas de Dentistas \n5- Atualizar Consulta Cadastrada \n6- Excluir Consulta Cadastrada \n0- Voltar \nR: '))
            print()
            if r == 0:
                break
            elif r == 1:
                od_func.cadastrarConsulta()
            elif r == 2:
                od_func.listarConsulta()
            elif r == 3:
                od_func.pesquisaConsultaPaciente()
            elif r == 4:
                od_func.pesquisaConsultaDentista()
            elif r == 5:
                od_func.atualizarConsulta()
            elif r == 6:
                od_func.excluirConsulta()
    elif menu == 4:
        while True:
            r = int(input('1- Cadastrar Nova Clínica \n2- Listar Clínicas \n3- Pesquisar Clínica por Nome \n4- Atualizar Clínica Cadastrada \n5- Excluir Clínica Cadastrada \n0- Voltar \nR: '))
            if r == 0:
                break
            elif r == 1:
                od_func.cadastrarClinica()
            elif r == 2:
                od_func.listarClinicas()
            elif r == 3:
                od_func.pesquisarClinicasNome()
            elif r == 4:
                od_func.atualizarClinica()
            elif r == 5:
                od_func.excluirClinica()
    elif menu == 5:
        while True:
            r = int(input('1- Cadastrar Novo Gerenciador \n2- Listar Gerenciadores \n3- Atualizar Gerenciador Cadastrado \n4- Excluir Gerenciador Cadastrado \n0- Voltar \nR: '))
            if r==0:
                break
            elif r==1:
                od_func.cadastrarGerenciadores()
            elif r==2:
                od_func.listarGerenciadores()
            elif r==3:
                od_func.atualizarGerenciadores()
            elif r==4:
                od_func.excluirGerenciadores()
