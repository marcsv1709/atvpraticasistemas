# Trabalho Prático - Sistemas Distribuídos

## Aluno
- **Marcos Vinicius Silva Andrade**  
- **Matrícula:** 2210372  

---

## Tecnologias Utilizadas
- **Python**
- **Flask** (Framework para API REST)
- **SQLite** (Banco de dados local)

---

## Descrição do Projeto
Este projeto consiste em um servidor de comunicação simples utilizando Flask e SQLite.  
O objetivo principal é receber um **login** e uma **senha** via requisição HTTP (POST) e retornar os mesmos dados como resposta, além de armazená-los no banco de dados.

---

## 📡 Como Utilizar a API

### URL da API
```
http://localhost:5000/api/login
```

#### Body da API
```
{
    "login": "teste",
    "senha": "test2"
}

```

#### Resultado
```
{
  "dados_recebidos": {
    "login": "teste",
    "senha": "test2"
  },
  "data_hora": "2025-03-10 18:37:02",
  "mensagem": "Dados recebidos com sucesso!"
}

```
