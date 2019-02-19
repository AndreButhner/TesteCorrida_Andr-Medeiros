from datetime import datetime, timedelta

#Faz a leitura das linhas que estão no arquivo de texto e os insere em uma lista
arq_lista = open('info.txt', 'r')
info = arq_lista.readlines()
arq_lista.close()

string_aux = ''
lista = []
lista2 = []

for x in range(0, len(info)):
	lista = []
	for i in info[x].strip().replace('\t', ''): #Retirando \n e \t do arquivo

		if i != ' ':
			string_aux = string_aux + i

		if i == ' ':
			if string_aux != '':
				lista.append(string_aux)
				string_aux = ''
	lista.append(string_aux)
	string_aux = ''
	
	lista2.append(lista)
	lista = []



###################################### Resultado Esperado ######################################

tempoTotal = timedelta(minutes = 0, seconds = 0, microseconds = 0)
posicao = 1
for x in lista2:
	if x[4] == '4':
		for y in lista2:
			if y[1] == x[1]:
				tempoTotal = tempoTotal + timedelta(minutes = int(y[5][0]), seconds = int(y[5][2:4]), microseconds= int(y[5][5:]))
		print('O piloto '+ x[1] + x[2] + x[3] + ' foi o ' + str(posicao) + 'º' ' a finalizar a corrida completando ' + x[4] + ' voltas em ' + str(tempoTotal) + '\n')
		posicao +=1
		tempoTotal = timedelta(minutes = 0, seconds = 0, microseconds = 0)



###################################### Bônus ######################################

# - Melhor volta de cada piloto
def MelhorVoltaPiloto():
	piloto = []
	for y in lista2:
		if y[3] not in piloto:
			piloto.append(y[3])
	lista_tempo = []
	for z in piloto:
		for k in lista2:
			if z == k[3]:
				lista_tempo.append(timedelta(minutes = int(k[5][0]), seconds = int(k[5][2:4]), microseconds= int(k[5][5:])))
		print('A melhor volta do piloto ' + z + ' foi em ' + str(min(lista_tempo)) + '\n')
		lista_tempo = []
MelhorVoltaPiloto()


# - Melhor volta da corrida
def MelhorVoltaCorrida():
	melhorVoltaCorrida = timedelta(minutes = int(lista2[0][5][0]), seconds = int(lista2[0][5][2:4]), microseconds= int(lista2[0][5][5:]))
	nomePiloto = ''
	for n in lista2:
		if timedelta(minutes = int(n[5][0]), seconds = int(n[5][2:4]), microseconds= int(n[5][5:])) < melhorVoltaCorrida:
			nomePiloto = n[3]
			melhorVoltaCorrida = timedelta(minutes = int(n[5][0]), seconds = int(n[5][2:4]), microseconds= int(n[5][5:]))
	print('A melhor volta da corrida foi feita pelo piloto ' + nomePiloto + ' em ' + str(melhorVoltaCorrida) + '\n')
MelhorVoltaCorrida()


# - Velocidade Media de cada piloto
def VelocidadeMedia():
	velMedia = []
	piloto = []
	for y in lista2:
		if y[3] not in piloto:
			piloto.append(y[3])

	for x in piloto:
		for y in lista2:
			if x == y[3]:
				velMedia.append(float(y[6].replace(',', '.')))
		print('A velocidade media do piloto ' + x + ' na corrida foi ' + '%.1f' % round(sum(velMedia) / len(velMedia),1) + '\n')
VelocidadeMedia()


# - Tempo de chegada após o vencedor
def TempoChegada():
	vencedor = 0
	tempoVencedor = timedelta(minutes = 0, seconds = 0, microseconds = 0)

	for x in lista2:
		if x[4] == '4':
			if vencedor == 0:
				vencedor = 1
				tempoVencedor = timedelta(hours = int(x[0][0:2]), minutes = int(x[0][3:5]), seconds = int(x[0][6:8]), microseconds = int(x[0][9:]))

	tempoPerdedor = timedelta(minutes = 0, seconds = 0, microseconds = 0)
	for y in lista2:
		if y[4] == '4':
		    tempoPerdedor = timedelta(hours = int(y[0][0:2]), minutes = int(y[0][3:5]), seconds = int(y[0][6:8]), microseconds = int(y[0][9:]))
		    if  tempoPerdedor > tempoVencedor:
		    	print('O Piloto ' + y[3] + ' chegou ' + str(tempoPerdedor - tempoVencedor) + ' após o vencedor')
TempoChegada()

