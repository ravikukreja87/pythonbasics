import pandas

numbers = [3,6,9]
numbers_as_pandas_series = pandas.Series(numbers) #List of numbers will be converted to pandas series
#and it will be stored in new pandas series 'numbers_as_pandas_series'
print(numbers_as_pandas_series)

colors = ['Red','Green','Blue']
colors_series = pandas.Series(colors)
print(colors_series)