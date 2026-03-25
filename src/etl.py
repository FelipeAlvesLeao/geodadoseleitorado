import pandas as pd
from src.database import DatabaseManager

class ETLProcessor:
    def __init__(self, raw_data_path="data/raw/perfil_eleitorado.csv"):
        self.raw_data_path = raw_data_path
        self.db_manager = DatabaseManager()

    def extract(self):
        print("Lendo o arquivo CSV do TSE...")
        return pd.read_csv(self.raw_data_path, sep=';', encoding='latin1', low_memory=False)

    def transform(self, df):
        print("Limpando e filtrando dados para Goiânia...")
        df_goiania = df[df['NM_MUNICIPIO'] == 'GOIÂNIA'].copy()
        
        colunas = ['NR_ZONA', 'NM_BAIRRO', 'DS_GENERO', 'DS_GRAU_ESCOLARIDADE', 'QT_ELEITORES_PERFIL']
        colunas_existentes = [c for c in colunas if c in df_goiania.columns]
        
        df_clean = df_goiania[colunas_existentes].dropna()
        return df_clean

    def load(self, df):
        print("Salvando dados limpos no SQLite...")
        self.db_manager.save_dataframe(df, "eleitorado_goiania")
        print("Pipeline ETL finalizado com sucesso!")

    def run(self):
        df_raw = self.extract()
        df_transformed = self.transform(df_raw)
        self.load(df_transformed)