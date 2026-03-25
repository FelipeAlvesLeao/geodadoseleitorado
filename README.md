# Análise de Perfil do Eleitorado - Goiânia 

Este projeto foi desenvolvido de uma forma bem crua para mostrar minhas habilidades na área de análise de dados usando código similar a um projeto que trabalhei sobre NDA.

O sistema consiste em um mini pipeline ETL que processa dados do Tribunal Superior Eleitoral (TSE), armazena as informações estruturadas em um banco de dados relacional e gera uma visualização geoespacial interativa.

## Dependências

- Python
- Pandas 
- SQLite3 
- Folium 

## Estrutura do Projeto

```
root/
├── data/
│   ├── raw/             # Arquivo CSV original do TSE dentro dessa pasta
│   └── processed/       
├── src/
│   ├── __init__.py
│   ├── database.py      
│   ├── etl.py           
│   └── map_gen.py       #
├── outputs/             # Arquivos gerado (mapa em HTML)
├── main.py              
└── README.md
```

## Como Executar

1. Instale as dependências necessárias:
   pip install pandas folium

2. Baixe os dados abertos do TSE:
   - Acesse o Portal de Dados Abertos do TSE.
   - Baixe a base de "Perfil do Eleitorado" mais recente.
   - Renomeie o arquivo descompactado para `perfil_eleitorado.csv` e coloque-o dentro da pasta `data/raw/`.

3. Execute o pipeline:
   python main.py

4. O script criará o banco de dados `eleitorado.db` na pasta `data/processed/` e o arquivo interativo `mapa_eleitorado.html` na pasta `outputs/`.

##  Próximos Passos

- Geolocalização das Zonas: A base de "Perfil do Eleitorado" do TSE não contém informações de geolocalização das zonas. Para garantir uma entrega rápida e visualmente funcional do mapa, foi implementado um dicionário estático mapeando o número das zonas de Goiânia para coordenadas centrais aproximadas. Em um ambiente de produção, a evolução natural deste módulo seria a integração da base do SQLite com um Shapefile/GeoJSON oficial das zonas utilizando a biblioteca Geopandas. Um comentário com mais informações pode ser encontrado no arquivo map_gen.py