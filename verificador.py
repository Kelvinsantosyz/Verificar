nome = input("Digite o seu nome: ")
senha = input("Digite sua senha: ")
cpf = input("Digite o seu CPF (no formato 123.456.789-01): ")

def verificar_cpf_repetido(cpf):
    if len(cpf) < 2:
        return False
    for i in range(len(cpf)-1):
        if cpf[i] == cpf[i+1]:
            return True
    return False

def validar_dados(nome, senha, cpf):
    if not nome.replace(' ','').isalpha() or len(nome) == 0:
        return False, "Nome inválido"
    
    if senha == nome or senha == senha[0] * len(senha):
        return False, "Senha inválida"
    
    if len(cpf) != 14 or (cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-'):
        for i in range(14):
            if i not in [3, 7, 11]:
                c = cpf[i]
                if not c.isnumeric():
                    return False, "CPF inválido"
        
    if verificar_cpf_repetido(cpf):
        return False, "CPF inválido: contém números repetidos"
    
    return True, ""


try:
    valida, erro = validar_dados(nome,senha,cpf)
    if valida:
        print("Dados valido")
    else:
        print("Dados invalidos", erro)
    
except Exception:
    print("Ocorreu erro inesperado, tente novamente")
    
    
