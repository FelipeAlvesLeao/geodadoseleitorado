import folium
import pandas as pd
from src.database import DatabaseManager

class MapGenerator:
    def __init__(self):
        self.db = DatabaseManager()
        # Nota: Usei o Gemini para sugerir essas coordenadas. Esse tipo de solução é absurda, mas 
        # como estou fazendo esse projeto pra mostrar minhas habilidades reais em um tempo limitado,
        # definir a geolocalização de zonas eleitorais infelizmente foge o meu skillset e tempo atual
        # devido a falta de shapefile pré-feita.
        # Esse vídeo indica como uma solução REAL deve ser elaborada, caso seja de interesse: 
        # https://youtu.be/AAqX6naDaK8
        self.coordenadas_zonas = {
            1: [-16.6799, -49.2550],   # Centro / Setor Sul
            2: [-16.6733, -49.2789],   # Campinas / Aeroporto
            127: [-16.6800, -49.2100], # Região Leste (Novo Mundo, etc.)
            133: [-16.7022, -49.2661], # Região Sul (Bueno, Pedro Ludovico)
            134: [-16.6911, -49.3000], # Região Oeste (Cidade Jardim)
            135: [-16.6200, -49.2300], # Região Norte (Goiânia 2, Urias Magalhães)
            136: [-16.6111, -49.3050], # Região Noroeste (Mangalô, Mutirão)
            146: [-16.7411, -49.3100], # Região Sudoeste (Garavelo, Itaipu)
            147: [-16.7100, -49.2300], # Região Sudeste (Parque Atheneu)
        }

    def generate_map(self):
        print("A gerar mapa de eleitores por Zona Eleitoral...")
        query = """
            SELECT NR_ZONA, SUM(QT_ELEITORES_PERFIL) as total_eleitores
            FROM eleitorado_goiania
            GROUP BY NR_ZONA
            ORDER BY total_eleitores DESC
        """
        
        try:
            df = self.db.execute_query(query)
        except Exception as e:
            print(f"Erro ao processar os dados: {e}")
            return

        mapa = folium.Map(location=[-16.6869, -49.2643], zoom_start=11, tiles="cartodbpositron")

        for index, row in df.iterrows():
            zona = int(row['NR_ZONA'])
            total = row['total_eleitores']
            coords = self.coordenadas_zonas.get(zona, [-16.6869, -49.2643])
            
            folium.CircleMarker(
                location=coords, 
                radius=max(total / 4000, 5),
                popup=f"Zona {zona}: {total} eleitores",
                tooltip=f"Zona {zona} (Clique para detalhes)",
                color="#3186cc",
                fill=True,
                fill_color="#3186cc"
            ).add_to(mapa)

        mapa.save("outputs/mapa_eleitorado.html")
        print("Mapa guardado na pasta outputs com sucesso!")##