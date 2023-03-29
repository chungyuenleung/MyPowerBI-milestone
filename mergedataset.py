import pandas as pd

amsterdam_weekdays = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\amsterdam_weekdays.csv')
amsterdam_weekends = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\amsterdam_weekends.csv')
athens_weekdays = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\athens_weekdays.csv')
athens_weekends = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\athens_weekends.csv')
barcelona_weekdays = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\barcelona_weekdays.csv')
barcelona_weekends = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\barcelona_weekends.csv')
berlin_weekdays = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\berlin_weekdays.csv')
berlin_weekends = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\berlin_weekends.csv')
budapest_weekdays = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\budapest_weekdays.csv')
budapest_weekends = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\budapest_weekends.csv')
lisbon_weekdays = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\lisbon_weekdays.csv')
lisbon_weekends = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\lisbon_weekends.csv')
london_weekdays = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\london_weekdays.csv')
london_weekends = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\london_weekends.csv')
paris_weekdays = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\paris_weekdays.csv')
paris_weekends = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\paris_weekends.csv')
rome_weekdays = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\rome_weekdays.csv')
rome_weekends = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\rome_weekends.csv')
vienna_weekdays = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\vienna_weekdays.csv')
vienna_weekends = pd.read_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\vienna_weekends.csv')

def combine(csv_1,col_1,csv_2,col_2,city):       # Combine the 2 datasets into a single dataset.
    csv_1['week time'] = col_1
    csv_2['week time'] = col_2
    csv_1.drop(columns = ['Unnamed: 0'],inplace=True)
    csv_2.drop(columns = ['Unnamed: 0'],inplace=True)
    merged = pd.concat([csv_1, csv_2])
    merged['city'] = city
    return merged

amsterdam = combine(amsterdam_weekdays,'weekdays',amsterdam_weekends,'weekends','amsterdam')
athens = combine(athens_weekdays,'weekdays',athens_weekends,'weekends','athens')
barcelona = combine(barcelona_weekdays,'weekdays',barcelona_weekends,'weekends','barcelona')
berlin = combine(berlin_weekdays,'weekdays',berlin_weekends,'weekends','berlin')
budapest = combine(budapest_weekdays,'weekdays',budapest_weekends,'weekends','budapest')
lisbon = combine(lisbon_weekdays,'weekdays',lisbon_weekends,'weekends','lisbon')
london = combine(london_weekdays,'weekdays',london_weekends,'weekends','london')
paris = combine(paris_weekdays,'weekdays',paris_weekends,'weekends','paris')
rome = combine(rome_weekdays,'weekdays',rome_weekends,'weekends','rome')
vienna = combine(vienna_weekdays,'weekdays',vienna_weekends,'weekends','vienna')

cities_names = ['amsterdam', 'athens', 'barcelona', 'berlin', 'budapest', 'lisbon', 'london', 'paris', 'rome', 'vienna']
cities = [amsterdam, athens, barcelona, berlin, budapest, lisbon, london, paris, rome, vienna]

europe_data = pd.concat(cities, ignore_index=True)

europe_data.to_csv(r'C:\Users\cylia\Desktop\DA project\airbnb\eu.csv')