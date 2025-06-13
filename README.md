# 🔬 Predição de Propriedades Físico-Químicas com Aprendizado de Máquina

Este projeto utiliza Python e bibliotecas científicas para prever propriedades físico-químicas de moléculas com base em seus descritores moleculares. O foco está na predição de ponto de fusão a partir de representações SMILES, com aplicação em química computacional e desenvolvimento de materiais.

## 🚀 Tecnologias Utilizadas

- Python 3.x
- RDKit
- Scikit-learn
- Pandas, NumPy, Matplotlib

## 📁 Estrutura do Projeto

- `predictor.py`: script principal de treinamento e avaliação do modelo.
- `notebooks/`: análises exploratórias e visualizações em Jupyter.
- `data/`: base de dados exemplo (pequena, para fins didáticos).
- `requirements.txt`: dependências do projeto.

## 🔧 Como Executar

```bash
# Clone o repositório
git clone https://github.com/seuusuario/ml-predicao-propriedades.git
cd ml-predicao-propriedades

# Crie um ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o script principal
python predictor.py
