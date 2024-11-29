import pandas as pd

data = pd.read_csv('./HarryPotterCharacters.csv')

data.loc[data['surname'].str.endswith(')', na= False), 'name'] += ' ' + data['surname']
data.loc[data['surname'].str.endswith(')', na= False), 'surname'] = ''

data.loc[data['name'].isna() | (data['name'] == ''), 'name'] = data['surname']
data.loc[data['name'] == data['surname'], 'surname'] = ''
data.loc[data['name'] == 'Lily L.', 'name'] = 'Lily Luna'
data.loc[data['name'] == 'James S.', 'name'] = 'James Severus'

data = data[~data['name'].str.endswith(')', na= False)]
data = data[~data['name'].str.startswith('Category', na= False)]
data = data[~data['name'].str.startswith('British', na= False)]
data = data[~data['name'].str.startswith('Department', na= False)]
data = data[~data['surname'].str.startswith('Army', na= False)]

data = data[~data['name'].str.startswith('Gryffindor', na= False)]
data = data[~data['name'].str.startswith('Hogwarts', na= False)]
data = data[~data['name'].str.startswith('Hufflepuff', na= False)]
data = data[~data['name'].str.startswith('Ilvermorny', na= False)]
data = data[~data['name'].str.startswith('List', na= False)]
data = data[~data['name'].str.startswith('Order', na= False)]
data = data[~data['name'].str.startswith('Ravenclaw', na= False)]
data = data[~data['name'].str.startswith('Serpent', na= False)]
data = data[~data['name'].str.startswith('Slytherin', na= False)]
data = data[~data['name'].str.startswith('House', na= False)]

data = data[~data['surname'].str.startswith('Weasleys', na= False)]
data = data[~data['surname'].str.startswith('Potters', na= False)]

data = data[~data['name'].str.startswith('Mr. and Mrs.', na= False)]

grangers = pd.DataFrame({
    'name': ['Mr. Granger', 'Mrs. Granger'],
    'surname': [None, None]
})

data = pd.concat([data, grangers], ignore_index= True)

data = data.rename(columns= {'name': 'character_name', 'surname': 'character_surname'})

data.to_csv('./HarryPotterCharacters.csv', index= False)
