# ☕ Sistema de Preparo de Bebidas Quentes (POO em Python)

Projeto desenvolvido como parte dos meus estudos avançados em **Python (Mundo 4 - Curso em Vídeo)**, com foco em **Programação Orientada a Objetos (POO)**. 

O objetivo deste projeto foi praticar e consolidar conceitos fundamentais da orientação a objetos, criando uma estrutura flexível e reutilizável.

## 🚀 Conceitos Aplicados
- **Classes Abstratas (`abc`):** Uso da classe base (`BebidaQuente`) para definir um contrato que obrigatoriamente deve ser seguido pelas subclasses.
- **Herança e Abstração:** As classes filhas (`Cafe`, `Cha`, `Leite`) herdam os comportamentos comuns e implementam os seus próprios métodos específicos de preparo.
- **Template Method (Padrão de Projeto):** A lógica estrutural do método `preparar()` é centralizada na classe mãe, enquanto os passos intermediários são delegados às subclasses.
- **Biblioteca `Rich`:** Utilizada para estilizar a saída no terminal, exibindo painéis formatados e coloridos (`Panel`).

## 🛠️ Tecnologias Utilizadas
- Python 3.x
- Biblioteca `rich`

## 📦 Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone [https://github.com/FrancielyRebeca/poo-bebidas-python.git](https://github.com/FrancielyRebeca/desafio-bebidas-poo-python.git)
2. Acesse a pasta do projeto:
   cd desafios-bebidas-poo-python
3. Instale as dependências necessárias:
   pip install -r requirements.txt
4. Execute o script principal:
   main.py

**Desenvolvido por Franciely Rebeca/FrancielyRebeca durante a jornada de aprendizado em Programação Orientada a Objetos com Pyhton.**
