import pandas as pd


health_data = pd.read_csv('datasets/health.csv', index_col=0)


health_data = health_data.rename(columns={
    'Prevalence Rate (%)': 'Prevalence Rate',
    'Incidence Rate (%)': 'Incidence Rate',
    'Mortality Rate (%)': 'Mortality Rate',
    'Healthcare Access (%)': 'Healthcare Access',
    'DALYs': 'Disability-Adjusted Life Years',
    'Recovery Rate (%)': 'Recovery Rate',
    'Urbanization Rate (%)': 'Urbanization Rate',
    'Improvement in 5 Years (%)': 'Improvement in 5 Years'
})

# print(health_data.head(10))

filter_df = health_data[health_data['Prevalence Rate'] > 10]
filter_df.sort_values('Prevalence Rate', ascending=False, inplace=True)
filter_df.shape
print(filter_df.head(10))

print('-' * 50)

group_df = health_data.groupby('Country')['Prevalence Rate'].mean()

print(group_df.head(10))