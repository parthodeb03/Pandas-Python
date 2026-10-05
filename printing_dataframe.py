import pandas
mydataset = {
    'cars' : ["BMW", "Audi", "Ford"],
    'perfumes' : ["Creed", "Pafums de Marly", "Dolce and Gabbana"]
}
df = pandas.DataFrame(mydataset)
print(df.loc[0])
print(df.loc[[0,1]])