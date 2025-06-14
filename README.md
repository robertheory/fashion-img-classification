# MVP Engenharia de Sistemas de Software Inteligentes

Trabalho final da disciplina de Engenharia de Sistemas de Software Inteligentes do curso de Engenharia de Software da Pontifícia Universidade Católica do Rio de Janeiro (PUC-Rio).

## Instalação e Execução da API

### Pré-requisitos

- [Python](https://www.python.org/downloads/) (versão 3.8 ou superior)
- Virtualenv (opcional, mas recomendado)

### Passos para Instalação

Clone o repositório:

```bash
git clone https://github.com/robertheory/mvp-essi.git
cd mvp-essi
```

Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Executando a API

Para iniciar a API, execute o seguinte comando no diretório raiz do projeto:

```bash
flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento, utilize o modo reload para que as mudanças no código sejam refletidas automaticamente:

```bash
flask run --host 0.0.0.0 --port 5000 --reload
```

Acesse `http://localhost:5000/#/` no navegador para visualizar a documentação da API e testar os endpoints.
