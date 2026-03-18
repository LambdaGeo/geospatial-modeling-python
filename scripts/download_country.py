import geopandas as gpd

# URL direta para o dataset cultural (Admin 0 - Países) do Natural Earth
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"

# Carregando os dados
world = gpd.read_file(url)

# No dataset original, as colunas são:
# 'NAME' -> Nome do país
# 'CONTINENT' -> Continente
# 'POP_EST' -> Estimativa de população
# 'GDP_MD' -> PIB (Gross Domestic Product)

# Selecionando e renomeando
world_filtered = world[['NAME', 'CONTINENT', 'POP_EST', 'GDP_MD']]
world_filtered.columns = ['country', 'continent', 'population', 'gdp']

# Salvando em CSV
world_filtered.to_csv("world_data.csv", index=False)

print("Arquivo 'world_data.csv' salvo com sucesso!")
print(world_filtered.head())