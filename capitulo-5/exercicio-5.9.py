valor_alvo = 50
lista_vinhos = [
    { 'nome': 'Vinho Tinto Reservado Cabernet Sauvignon - Concha y Toro', 'valor': 29.97 },
    { 'nome': 'Vinho Branco - Casal Garcia', 'valor': 55.99 },
    { 'nome': 'Vinho Tinto Reservado Malbec - Concha y Toro', 'valor': 43.59, },
    { 'nome': 'Vinho Tinto Carménère - Casillero del Diablo', 'valor': 59.00 },
    { 'nome': 'Vinho Espumante Brut Rosé - Casa Perini', 'valor': 59.95 }
    ]

encontrar_vinho_mais_caro = lambda vinho: vinho['valor'] >= valor_alvo 
resultado = list(filter(encontrar_vinho_mais_caro, lista_vinhos))

print(resultado)

