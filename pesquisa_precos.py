import requests
from lxml import html
import csv
from datetime import datetime

# URLs das páginas de busca do Buscapé
urls = {
    "iPad 9": "https://www.buscape.com.br/search?q=ipad%209",
    "Apple Watch SE": "https://www.buscape.com.br/search?q=apple%20watch%20se"
}

# Cabeçalho para simular um navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

# Obter a data e hora atual
data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Abrir o arquivo CSV para escrita
with open("buscape_resultados.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo, delimiter=";")
    escritor.writerow(["Data e Hora", "Produto", "Nome", "Preço", "Link"])  # Cabeçalho

    # Iterar sobre as URLs
    for produto, url in urls.items():
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            tree = html.fromstring(response.content)

            # Capturar os nomes dos produtos
            nomes = tree.xpath('//a[contains(@class, "ProductCard_ProductCard_Inner__gapsh")]//h2[@class="Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_DesktopLabelSAtLarge__wWsED ProductCard_ProductCard_Name__U_mUQ"]/text()')

            # Capturar os preços dos produtos
            precos = tree.xpath('//a[contains(@class, "ProductCard_ProductCard_Inner__gapsh")]//p[@class="Text_Text__ARJdp Text_MobileHeadingS__HEz7L"]/text()')

            # Capturar os links dos produtos
            links = tree.xpath('//a[contains(@class, "ProductCard_ProductCard_Inner__gapsh")]/@href')
            links_completos = ["https://www.buscape.com.br" + link for link in links]

            # Escrever os dados no arquivo CSV
            for nome, preco, link in zip(nomes, precos, links_completos):
                escritor.writerow([data_hora_atual, produto, nome.strip(), preco.strip(), link])

            print(f"Dados do {produto} salvos com sucesso!")
        else:
            print(f"Erro ao acessar a página do {produto}: {response.status_code}")
