# FastAPI Model

Um modelo inicial para uma API escrita em FastAPI

### 📖 sobre

Uma configuração inicial para rodar um backend com FastAPI, com separação de rotas, dependencies e arquivos iniciais 
necessaries para iniciar uma instância de banco de dados com SQLAlchemy

### 📋 pré-requisitos

```
Python 3.10 ou superior
Pip 22.0.2 ou superior
virtualenv 20.13 ou superior
```

### 🔧 Instalação

Para fazer a instalação do requirements é necessario primeiramente criar um ambiente virtual para podermos utilizar o app.

**Linux**
instalação do virtualenv:
```
sudo apt-get install python3-venv
```
criando o ambiente virtual:
```
python3 -m venv nome_do_ambiente
```
para ativar o ambiente virtual :
```
source nome_do_ambiente/bin/activate
```
Com o ambiente devidamente ativado instalamos os requerimentos com o seguinte código:
```
pip3 install -r requirements.txt
```
Mude a rota do banco de dados de sua preferência e com as bibliotecas 
instaladas, Rode o programa com o seguinte código:
```
uvicorn main:app --reload
```

Com isso vá até *http://127.0.0.1:8000/docs* para ver a documentação interativa e fazer os testes das rotas

## 🛠️  Construído com

Ferramentas que Usei na criação deste Modelo



<a style="display: inline_block" href="https://fastapi.tiangolo.com">
<img align="center" alt="Python" src="https://img.shields.io/badge/FastAPI-%23009688?style=for-the-badge&logo=fastapi&logoColor=white" />
</a><br/><br>
<a style="display: inline_block" href="https://docs.sqlalchemy.org/en/14/">
<img align="center" alt="Python" src="https://img.shields.io/badge/sqlalchemy-%234479A1?style=for-the-badge&logo=mysql&logoColor=white" />
</a><br/><br>





## ✒️ Desenvolvedores

* **Bruno Alves** - *Desenvolvedor Fullstack* - [Bruno Azzireluto](https://github.com/Brunoazzireluto)

---
Feito com ❤️ por [N2bit](https://github.com/N2Bit)