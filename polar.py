import polars as pl


health_data = pl.read_csv('datasets/health.csv')

# print(health_data.head(10))


unique_countries = health_data['Country'].n_unique()


print(unique_countries)


unique_diseases = health_data['Disease Name'].n_unique()
print(unique_diseases)