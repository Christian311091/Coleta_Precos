import requests
from lxml import html

# URL do produto no Mercado Livre
url = "https://www.mercadolivre.com.br/apple-ipad-wifi-9th-geraco-cinza-espacial-a2602-64gb-102-/p/MLB18498456?pdp_filters=item_id%3AMLB3914713473&from=gshop&matt_tool=61921241&matt_word=&matt_source=google&matt_campaign_id=22090354535&matt_ad_group_id=173090632476&matt_match_type=&matt_network=g&matt_device=c&matt_creative=727882734705&matt_keyword=&matt_ad_position=&matt_ad_type=pla&matt_merchant_id=735098639&matt_product_id=MLB18498456-product&matt_product_partition_id=2389562549930&matt_target_id=aud-1966981570049:pla-2389562549930&cq_src=google_ads&cq_cmp=22090354535&cq_net=g&cq_plt=gp&cq_med=pla&gad_source=4&gclid=CjwKCAiAqfe8BhBwEiwAsne6gSY3_cYl0htgFSt-5B2hQVSs1Yd8WWVc6Ko5Q880qdGEiPpagZCBGRoCn38QAvD_BwE"

# Cabeçalhos para simular um navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

# Fazer a requisição HTTP para a página do produto
response = requests.get(url, headers=headers)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    tree = html.fromstring(response.content)
    
    # Usar o XPath fornecido para encontrar o preço
    preco = tree.xpath('//*[@id="price"]/div/div[1]/div[1]/span/span/span[2]/text()')
    
    if preco:
        print(f"Preço encontrado: R$ {preco[0].strip()}")
    else:
        print("Preço não encontrado!")
else:
    print(f"Erro ao acessar a página: {response.status_code}")
