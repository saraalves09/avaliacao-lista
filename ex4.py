required_fields = []
user_data = []

# Cadastrar usuário
def register_user(required_fields):
    usuario = {}
    for campo in required_fields:
        valor = input(f'Digite um valor para o campo "{campo}": ')
        usuario[campo] = valor
    
    while True:
        novo_campo = input('Digite um campo extra ou "nao" para finalizar: ')
        if novo_campo.lower() == 'nao':
            break
        valor = input(f'Digite um valor para o campo "{novo_campo}": ')
        usuario[novo_campo] = valor
    
    user_data.append(usuario)
    return usuario

# Imprimir usuários
def print_user(*args, **kwargs):
    if not args and not kwargs:
        for usuario in user_data:
            print(usuario)
    elif args:
        for nome in args:
            for usuario in user_data:
                if nome in usuario:
                    print(usuario)
    elif 'campo' in kwargs and 'valor' in kwargs:
        campo = kwargs['campo']
        valor = kwargs['valor']
        for usuario in user_data:
            if campo in usuario and usuario[campo] == valor:
                print(usuario)
    elif 'nomes' in kwargs and 'campos' in kwargs:
        nomes = kwargs['nomes']
        campos = kwargs['campos']
        for usuario in user_data:
            if usuario['nome'] in nomes:
                for campo, valor in campos.items():
                    if campo in usuario and usuario[campo] == valor:
                        print(usuario)

# Principal
def main():
    while True:
        print("Menu:")
        print("1 - Cadastrar usuário")
        print("2 - Imprimir usuários")
        print("0 - Finalizar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            usuario = register_user(required_fields)
            print("Usuário cadastrado:")
            print(usuario)
        elif opcao == '2':
            print("1 - Imprimir todos")
            print("2 - Filtrar por nomes")
            print("3 - Filtrar por campos")
            print("4 - Filtrar por nomes e campos")
            subopction = input("Escolha uma opção: ")
            
            if subopction == '1':
                print_user()
            elif subopction == '2':
                nomes = input("Digite os nomes separados por vírgula: ").split(',')
                print_user(*nomes)
            elif subopction == '3':
                campo = input("Digite o campo que procura: ")
                valor = input(f'Digite o valor para o campo "{campo}": ')
                print_user(campo=campo, valor=valor)
            elif subopction == '4':
                nomes = input("Digite os nomes separados por vírgula: ").split(',')
                campos = {}
                while True:
                    campo = input("Digite um campo para filtrar ou 'nao' para finalizar: ")
                    if campo.lower() == 'nao':
                        break
                    valor = input(f'Digite o valor para o campo "{campo}": ')
                    campos[campo] = valor
                print_user(nomes=nomes, campos=campos)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    required_fields = input("Digite os campos obrigatórios separados por vírgula: ").split(',')
    main()
