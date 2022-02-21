import matplotlib.pyplot as plt

tamanho = []
cor = []

#mudar o nome da tabela a ser usada
arquivo = open('Galaxia 8\tabela questao4\tabela_bv_tamanho_8.txt','r')
arquivo.close

for linha in arquivo:
  linha = linha.replace(',','.')
  tamanho.append(float(linha.split()[0]))
  cor.append(float(linha.split()[1]))

x = tamanho
y = cor

plt.scatter(x,y)
plt.title ('índice de cor x tamanho') #título
plt.xlabel('raio da galáxia (kpc)') #título do eixo x
plt.ylabel('B-V') #título do eixo y
#plt.xlim(max(x)+0.5,min(x)-0.5)
plt.savefig('Galaxia 8\grafico_cor_tamanho_8.png',format='png')
plt.show()