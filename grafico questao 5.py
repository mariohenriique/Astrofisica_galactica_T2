import pandas as pd
import matplotlib.pyplot as plt
arquivo = pd.read_csv('valores.txt')
df_test = pd.DataFrame(arquivo)

print(df_test.Gal)

def fazer_grafico(x,y,titulo,eixox,eixoy,nome):
    plt.scatter(x,y)
    plt.title (titulo) #título
    plt.xlabel(eixox) #título do eixo x
    plt.ylabel(eixoy) #título do eixo y
    plt.savefig(nome,format='png')
    plt.show()

ci_luminosidade = fazer_grafico(df_test.CI,df_test.Flux,'C.I. x Luminosidade','C.I.','Luminosidade','grafico_ci_luminosidade.png')
ci_cor = fazer_grafico(df_test.CI,df_test.Color,'C.I. x Cor','C.I.','Cor (B-V)','grafico_ci_cor.png')
ci_tamanho = fazer_grafico(df_test.CI,df_test.Size,'C.I. x Tamanho','C.I.','Tamanho (kpc)','grafico_ci_tamanho.png')
ai_luminosidade = fazer_grafico(df_test.AI,df_test.Flux,'A.I. x Luminosidade','A.I.','Luminosidade','grafico_ai_luminosidade.png')
ai_tamanho = fazer_grafico(df_test.AI,df_test.Size,'A.I. x Tamanho','A.I.','Tamanho (kpc)','grafico_ai_tamanho.png')
ai_cor = fazer_grafico(df_test.AI,df_test.Color,'A.I. x Cor','A.I.','Cor (B-V)','grafico_ai_cor.png')