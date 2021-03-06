from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

# Alterando a coluna "PERFIL"
def transforme_coluna(value):
        if value == "EXCELENTE":
            return float(0)
        elif value == "MUITO BOM":
            return float(1)
        elif value == "HUMANAS":
            return float(2)
        elif value == "EXATAS":
            return float(3)
        elif value == "DIFICULDADE":
            return float(4)
        elif isinstance(value, str) == False:
            return float(value)



# excluirá linhas e retornará um novo dataframe
def excluir_Desistentes(df):

    df.drop(df.loc[(df["H_AULA_PRES"] == 0) & (df["TAREFAS_ONLINE"] == 0) & (df["NOTA_DE"] == 0) & (df["NOTA_EM"] == 0) 
                    & (df["NOTA_MF"] == 0) & (df["NOTA_GO"] == 0)].index, inplace=True)

    return df


