import pandas as pd

df = pd.read_csv('final_stars.csv')
print(df.head())

df.drop(['Unnamed: 0'], axis=1, inplace= True)
df["Mass"] = df["Mass"].apply(lambda x:x.replace('$', '').replace(',','')).astype('float')

df['Mass'] = 1.989e+30*df['Mass']
print(df.head())
df['Radius'] = 6.957e+8*df['Radius']

radius = df['Radius'].to_list() 
mass = df['Mass'].to_list() 
gravity =[] 
def convert_to_si(radius,mass): 
    for i in range(0,len(radius)-1): radius[i] = radius[i]*6.957e+8 
    mass[i] = mass[i]*1.989e+30 

convert_to_si(radius,mass)

G = 6.674e-11

for i in range(0,len(mass)):
    g = (mass[i]*G)/((radius[i])**2)
    gravity.append(g)

print(gravity)

df["gravity"] = gravity

