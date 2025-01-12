import pandas

env = 'test'
env_series = pandas.Series(env)
print(env_series)
another_env = 'dev'
indexes=[1]
result = env_series._append(pandas.Series(another_env,indexes))
print(result)
