import pandas as pd

# Dados de exemplo para uma análise simples com Pandas
dados = {
    "produto": ["Arroz", "Feijão", "Leite", "Pão", "Café", "Arroz", "Leite", "Café"],
    "categoria": ["Alimentos", "Alimentos", "Bebidas", "Padaria", "Bebidas", "Alimentos", "Bebidas", "Bebidas"],
    "preco": [22.90, 8.90, 5.00, 1.50, 18.50, 21.90, 5.50, 19.90],
    "quantidade": [2, 3, 5, 10, 2, 1, 4, 1]
}

# Criando um DataFrame
df = pd.DataFrame(dados)

# Criando a coluna de total por item
df["total"] = df["preco"] * df["quantidade"]

print("=== TABELA DE DADOS ===")
print(df)

print("\n=== RESUMO DOS DADOS ===")
print(df.describe(numeric_only=True))

print("\n=== TOTAL VENDIDO ===")
print(f"R$ {df['total'].sum():.2f}")

print("\n=== MÉDIA DE PREÇO ===")
print(f"R$ {df['preco'].mean():.2f}")

print("\n=== PRODUTO COM MAIOR VALOR TOTAL ===")
maior = df.loc[df["total"].idxmax()]
print(f"{maior['produto']} - R$ {maior['total']:.2f}")

print("\n=== TOTAL POR CATEGORIA ===")
print(df.groupby("categoria")["total"].sum().sort_values(ascending=False))

print("\n=== PRODUTOS COM PREÇO ACIMA DA MÉDIA ===")
media_preco = df["preco"].mean()
print(df[df["preco"] > media_preco][["produto", "preco"]])
