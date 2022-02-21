import pandas as pd
import numpy

arquivo = pd.read_csv('valores.txt')
df_test = pd.DataFrame(arquivo)

arquivo2 = pd.read_csv('valores2.txt')
df_test1 = pd.DataFrame(arquivo2)
#print(df_test,'\n',df_test1)
e = 0

for i in df_test.Flux:
    m = df_test1.Magnitude.iloc[e]
    flux = 2.5*numpy.log10(i)
    Mv = -20.6
    resultado = 10**((m-Mv-flux+5)/5)
    print('{:e}'.format(resultado))
    e += 1