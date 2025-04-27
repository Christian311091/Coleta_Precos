import requests
from lxml import html
import csv
from datetime import datetime
import os

# URLs das páginas de busca do Buscapé
urls = {
    "iPad 9": "https://www.buscape.com.br/search?q=ipad%209",
    "Apple Watch SE": "https://www.buscape.com.br/search?q=apple%20watch%20se"
}

# Cabeçalho para simular um navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

# Pasta de dados
os.makedirs("dados", exist_ok=True)

# Nome do arquivo baseado na data
data_atual = datetime.now().strftime("%Y-%m-%d")
nome_arquivo = f"dados/buscape_{data_atual}.csv"

# Abrir o arquivo CSV para escrita
with open(nome_arquivo, "w", newline="", encoding="utf-8-sig") as arquivo:
    escritor = csv.writer(arquivo, delimiter=";")
    escritor.writerow(["Data", "Produto", "Nome", "Preço", "Link"])  # Cabeçalho

    for produto, url in urls.items():
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            tree = html.fromstring(response.content)

            # Capturar os nomes dos produtos
            nomes = tree.xpath('//a[contains(@class, "ProductCard_ProductCard_Inner__gapsh")]//h2/text()')

            # Capturar apenas os preços corretos
            precos = tree.xpath('//p[contains(@class, "Text_MobileHeadingS__HEz7L")]/text()')

            # Capturar os links dos produtos
            links = tree.xpath('//a[contains(@class, "ProductCard_ProductCard_Inner__gapsh")]/@href')
            links_completos = ["https://www.buscape.com.br" + link for link in links]

            # Escrever os dados no arquivo
            for nome, preco, link in zip(nomes, precos, links_completos):
                preco = preco.strip() if preco else "Preço não encontrado"
                escritor.writerow([data_atual, produto, nome.strip(), preco, link])

            print(f"Dados do {produto} salvos com sucesso!")
        except Exception as e:
            print(f"Erro ao coletar dados de {produto}: {e}")
