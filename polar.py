import polars as pl


health_data = pl.read_csv('datasets/health.csv')

# print(health_data.head(10))

health_data = health_data.rename({
    'Prevalence Rate (%)': 'Prevalence Rate',
    'Incidence Rate (%)': 'Incidence Rate',
    'Mortality Rate (%)': 'Mortality Rate',
    'Healthcare Access (%)': 'Healthcare Access',
    'Recovery Rate (%)': 'Recovery Rate',
    'Urbanization Rate (%)': 'Urbanization Rate',
    'Improvement in 5 Years (%)': 'Improvement in 5 Years'
})

unique_countries = health_data['Country'].n_unique()


print(unique_countries)


unique_diseases = health_data['Disease Name'].n_unique()
print(unique_diseases)



# test1_data = health_data.group_by('Country').agg([
#          pl.col('Prevalence Rate').mean().alias('Prevalence Rate mean'),
#          pl.col('Prevalence Rate').min().alias('Prevalence Rate min'),
#          pl.col('Prevalence Rate').max().alias('Prevalence Rate max'),
#          pl.col('Mortality Rate').mean().alias('Mortality Rate mean'),
#          pl.col('Mortality Rate').min().alias('Mortality Rate min'),
#          pl.col('Mortality Rate').max().alias('Mortality Rate max')])

# print(test1_data.head(10))


test2_data = health_data.filter(pl.col('Prevalence Rate') > 10).sort('Prevalence Rate', descending=True).select('Country', 'Prevalence Rate')
print(test2_data.head(10))