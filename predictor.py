import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from rdkit import Chem
from rdkit.Chem import Descriptors

def gerar_descritores(smiles_list):
    descritores = []
    for smi in smiles_list:
        mol = Chem.MolFromSmiles(smi)
        if mol:
            desc = {
                'MolWt': Descriptors.MolWt(mol),
                'MolLogP': Descriptors.MolLogP(mol),
                'NumRotatableBonds': Descriptors.NumRotatableBonds(mol),
                'TPSA': Descriptors.TPSA(mol),
                'NumHDonors': Descriptors.NumHDonors(mol),
                'NumHAcceptors': Descriptors.NumHAcceptors(mol)
            }
            descritores.append(desc)
        else:
            descritores.append(None)
    return pd.DataFrame([d for d in descritores if d is not None])

data = {
    'SMILES': ['CCO', 'CC(=O)O', 'CCN', 'CCC', 'C1=CC=CC=C1', 'CC(C)O', 'C(CCl)Cl'],
    'Ponto_Fusao': [156.0, 289.0, 120.0, 98.0, 279.0, 115.0, 136.0]
}

df = pd.DataFrame(data)
X = gerar_descritores(df['SMILES'])
y = df.loc[X.index, 'Ponto_Fusao']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.2f}")
