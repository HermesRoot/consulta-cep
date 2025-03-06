# 🔍 Consulta CEP

Este projeto oferece uma API simples para consultar informações de endereço a partir de um CEP (Código de Endereçamento Postal) do Brasil. A API retorna dados como rua, bairro, cidade e estado, utilizando a [Brasil API](https://brasilapi.com.br).

Além da API, também inclui uma interface web simples para realizar consultas diretamente pelo navegador.

## 🖥️ Captura de Tela
![Screenshot do consulta-cep](https://raw.githubusercontent.com/HermesRoot/consulta-cep/refs/heads/main/screenshot.jpg)

## ✨ Funcionalidades

- **Consulta de CEP:** Informe um CEP e obtenha as informações de endereço associadas (rua, bairro, cidade, estado).
- **Interface Web:** Página simples para consultar o CEP diretamente pelo navegador.
- **CORS Habilitado:** Permite o consumo da API por aplicações web de outros domínios.

## 🛠️ Tecnologias Utilizadas

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **API Externa:** [Brasil API](https://brasilapi.com.br)

## 🚀 Como Executar o Projeto

### Pré-requisitos

1. Python 3.x instalado.
2. Dependências listadas em `requirements.txt`.

### Passo 1: Clonar o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/HermesRoot/consulta-cep.git
cd consulta-cep
```

### Passo 2: Instalar Dependências
Instale as dependências necessárias com o pip:

```bash
pip install -r requirements.txt
```
### Passo 3: Executar o Servidor Flask
Execute o servidor Flask:

```bash
python api_cep.py
```

Isso iniciará o servidor localmente na porta 5000:

```bash
Servidor rodando em: http://127.0.0.1:5000
```

### Passo 4: Usar a Interface Web
Abra o arquivo `consulta_cep.html` no seu navegador para acessar a interface de consulta de CEP.

## 📡 Como Usar a API
A API está disponível no endpoint `/consulta-cep`, e você pode fazer uma requisição GET passando o CEP como parâmetro. Exemplo:

```bash
GET http://127.0.0.1:5000/consulta-cep?cep=01001000
```
A resposta será um JSON com as informações do endereço associado ao CEP informado.

Exemplo de resposta:

```bash
{
  "cep": "01001-000",
  "street": "Praça da Sé",
  "neighborhood": "Sé",
  "city": "São Paulo",
  "state": "SP"
}
```

## 📝 Licença

Este projeto está licenciado sob a licença **MIT** — veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👤 Autor

Desenvolvido por **HermesRoot**. 










