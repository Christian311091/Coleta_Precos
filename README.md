# 🛒 Web Scraping Buscapé

Este projeto realiza **coleta automatizada de preços** no site [Buscapé](https://www.buscape.com.br), extraindo informações de produtos específicos e salvando os dados em arquivos **CSV** para análise posterior.

---

## 📌 Funcionalidades

- Busca automática por produtos pré-definidos (ex: *iPad 9* e *Apple Watch SE*)
- Captura **nome, preço, link e data/hora da coleta**
- Armazena os resultados em arquivos CSV para fácil manipulação
- Garante headers simulando um navegador real para evitar bloqueios

---

## 🗂 Estrutura

O projeto possui duas versões principais:

1. **Versão com histórico (primeira parte)**  
   - Cria uma pasta `dados/`  
   - Salva o arquivo CSV com a **data da coleta no nome** (ex.: `buscape_2025-09-20.csv`)
2. **Versão simples (segunda parte)**  
   - Gera apenas um arquivo único `buscape_resultados.csv`  
   - Inclui a **data e hora exata** no conteúdo de cada linha

---

## 🛠 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Requests](https://docs.python-requests.org/)
- [lxml](https://lxml.de/)
- [CSV](https://docs.python.org/3/library/csv.html)
- [Datetime](https://docs.python.org/3/library/datetime.html)

---

## ▶️ Como Executar

1. Clone este repositório:  
   git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git  
   cd SEU-REPOSITORIO
2. Crie e ative um ambiente virtual (opcional, mas recomendado):  
   python -m venv venv  
   source venv/bin/activate  # Linux/Mac  
   venv\Scripts\activate     # Windows
3. Instale as dependências:  
   pip install -r requirements.txt
4. Execute o script:  
   python buscape_scraper.py
