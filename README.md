# Fashion Image Classification

## Descrição do Projeto

Este projeto é uma aplicação fullstack para classificação de imagens de moda, desenvolvida como parte do trabalho final da disciplina de Engenharia de Sistemas de Software Inteligentes do curso de Engenharia de Software da Pontifícia Universidade Católica do Rio de Janeiro (PUC-Rio).

A aplicação permite que usuários enviem imagens de itens de moda e recebam a classificação correspondente, utilizando um modelo de machine learning treinado previamente.

## Estrutura do Projeto

O projeto é dividido em três partes principais:

1. **Web**: Desenvolvido em HTML e JavaScript, responsável pela interface do usuário.
2. **Server**: Desenvolvido em Python, responsável por receber as imagens, processá-las e retornar a predição de categoria.
3. **Machine Learning**: Desenvolvido em Python, contém o modelo de machine learning treinado para classificação das imagens.

## Pré-requisitos

- Python 3.8 ou superior

## Inicialização do Projeto

1. Clone o repositório:

```bash
git clone https://github.com/robertheory/mvp-essi.git
cd mvp-essi
```

2. (Opcional, mas recomendado) Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicie o servidor:

```bash
cd server
flask run --host 0.0.0.0 --port 5000
```

5. Abra o arquivo [`web/index.html`](web/index.html) no navegador para acessar a interface do usuário.

Com o servidor em execução, você pode enviar imagens pela interface web e receber a classificação prevista pelo modelo de machine learning.
