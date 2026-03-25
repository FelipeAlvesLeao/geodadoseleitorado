import folium
import pandas as pd
from src.database import DatabaseManager

class MapGenerator:
    def __init__(self):
        self.db = DatabaseManager()
        self.coordenadas_zonas = {
            1: [-16.6799, -49.2550],
            2: [-16.6733, -49.2789],
            127: [-16.6800, -49.2100],
            133: [-16.7022, -49.2661],
            134: [-16.6911, -49.3000],
            135: [-16.6200, -49.2300],
            136: [-16.6111, -49.3050],
            146: [-16.7411, -49.3100],
            147: [-16.7100, -49.2300],
        }

    def generate_map(self):
        print("A gerar mapa com as zonas...")
        query = """
            SELECT NR_ZONA, SUM(QT_ELEITORES_PERFIL) as total_eleitores
            FROM eleitorado_goiania
            GROUP BY NR_ZONA
        """
        
        try:
            df = self.db.execute_query(query)
        except Exception as e:
            print(f"Erro ao aceder ao banco: {e}")
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
                color="#3186cc",
                fill=True,
                fill_color="#3186cc"
            ).add_to(mapa)

            folium.Marker(
                location=coords,
                icon=folium.DivIcon(
                    icon_size=(150, 36),
                    icon_anchor=(75, 30),
                    html=f'<div style="font-size: 14px; font-weight: bold; color: black; text-shadow: 2px 2px 4px white, -2px -2px 4px white, 2px -2px 4px white, -2px 2px 4px white; text-align: center;">Zona {zona}</div>'
                )
            ).add_to(mapa)

        mapa.save("outputs/mapa_eleitorado.html")
        print("Mapa guardado com sucesso!")