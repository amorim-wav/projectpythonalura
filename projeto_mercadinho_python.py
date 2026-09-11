# Projeto final - Introdução a Python: desafios de programação
# Sistema de mercado simples

produtos = {
    "1": {"nome": "Maçã", "preco": 3.50},
    "2": {"nome": "Pão", "preco": 1.50},
    "3": {"nome": "Leite", "preco": 5.00},
    "4": {"nome": "Arroz", "preco": 22.90},
    "5": {"nome": "Feijão", "preco": 8.90}
}

saldo = 50.00
carrinho = []

def mostrar_produtos():
    print("\n=== PRODUTOS ===")
    for codigo, produto in produtos.items():
        print(f"{codigo} - {produto['nome']} - R$ {produto['preco']:.2f}")

def mostrar_carrinho():
    print("\n=== CARRINHO ===")
    if not carrinho:
        print("Seu carrinho está vazio.")
        return

    total = 0
    for item in carrinho:
        subtotal = item["preco"] * item["quantidade"]
        total += subtotal
        print(
            f"{item['nome']} x{item['quantidade']} "
            f"- R$ {subtotal:.2f}"
        )

    print(f"Total gasto: R$ {total:.2f}")
    print(f"Saldo restante: R$ {saldo:.2f}")

print("Bem-vindo ao Mercadinho Python!")
print(f"Seu saldo inicial é de R$ {saldo:.2f}")

while True:
    print("\n=== MENU ===")
    print("1 - Ver produtos")
    print("2 - Comprar produto")
    print("3 - Ver carrinho")
    print("4 - Ver saldo")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_produtos()

    elif opcao == "2":
        mostrar_produtos()
        codigo = input("Digite o código do produto: ")

        if codigo not in produtos:
            print("Produto inválido.")
            continue

        try:
            quantidade = int(input("Digite a quantidade: "))
        except ValueError:
            print("Digite um número inteiro para a quantidade.")
            continue

        if quantidade <= 0:
            print("A quantidade precisa ser maior que zero.")
            continue

        produto = produtos[codigo]
        valor_compra = produto["preco"] * quantidade

        if valor_compra > saldo:
            print("Saldo insuficiente para realizar essa compra.")
            continue

        saldo -= valor_compra

        encontrado = False
        for item in carrinho:
            if item["nome"] == produto["nome"]:
                item["quantidade"] += quantidade
                encontrado = True
                break

        if not encontrado:
            carrinho.append({
                "nome": produto["nome"],
                "preco": produto["preco"],
                "quantidade": quantidade
            })

        print(
            f"Compra realizada: {quantidade}x {produto['nome']} "
            f"por R$ {valor_compra:.2f}"
        )
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "3":
        mostrar_carrinho()

    elif opcao == "4":
        print(f"\nSaldo atual: R$ {saldo:.2f}")

    elif opcao == "5":
        print("\n=== RESUMO FINAL ===")
        mostrar_carrinho()
        print("Obrigado por usar o Mercadinho Python!")
        break

    else:
        print("Opção inválida. Tente novamente.")
