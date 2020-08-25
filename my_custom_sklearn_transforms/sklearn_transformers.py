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

class OverSample(BaseEstimator, TransformerMixin):
    def __init__(self, column):
        self.column = column
        
    def over_excelent(self, dataset, col):
        intermed = dataset[dataset[col]=='EXCELENTE']
        dataset = pd.concat([dataset, intermed])
        return dataset
    
    def over_good(self, dataset, col):
        intermed = dataset[dataset[col]=='MUITO_BOM']
        dataset = pd.concat([dataset, intermed])
        return dataset
    
    def fit(self,  X, y=None, **fit_params):
        return self
    
    def transform(self, X, **transform_params):
        X = self.over_good(X, self.column)
        dataset = self.over_excelent(X, self.column) 
        return dataset
