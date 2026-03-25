import os
from src.etl import ETLProcessor
from src.map_gen import MapGenerator

def main():
    os.makedirs("outputs", exist_ok=True)
    
    print("Iniciando pipeline do projeto NIE...")
    
    etl = ETLProcessor()
    etl.run()
    
    map_gen = MapGenerator()
    map_gen.generate_map()
    
    print("Tudo pronto.")

if __name__ == "__main__":
    main()