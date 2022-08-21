bio = [{'6b', '7b', '8b', '9b', '10b', '11b', '9d', '10d', '11d', '9f', '10f', '11f'}, #1
{'15b', '16b', '17b', '18b', '19b', '20b', '9d', '10d', '11d', '9f', '10f', '11f'}, #2
{'12d', '13d', '14d', '6e', '7e', '8e', '9e', '10e', '11e', '12f', '13f', '14f'}, #3
{'12d', '13d', '14d', '15e', '16e', '17e', '18e', '19e', '20e', '12f', '13f', '14f'}, #4
{'15c', '16c', '17c', '15e', '16e', '17e', '6f', '7f', '8f', '9f', '10f', '11f'}, #5
{'15c', '16c', '17c', '15e', '16e', '17e', '15f', '16f', '17f', '18f', '19f', '20f'},] #6

chem = [{'10c', '11c', '12c', '13c', '14c', '15c', '9d', '10d', '11d', '9f', '10f', '11f'}, #1
{'16d', '17d', '18d', '19d', '20d', '21d', '9d', '10d', '11d', '9f', '10f', '11f'}, #2
{'3c', '4c', '5c', '3e', '4e', '5e', '6e' '7e', '8e', '3f', '4f', '5f'}, #3
{'3c', '4c', '5c', '10e', '11e', '12e', '13e' '14e', '15e', '3f', '4f', '5f'}, #4
{'12c', '13c', '14c', '16c', '17c', '18c', '19c', '20c', '21c', '12e', '13e', '14e'}, #6
{'9c', '10c', '11c', '9e', '10e', '11e', '16e', '17e', '18e', '19e', '20e', '21e'}, #7
{'9c', '10c', '11c', '9e', '10e', '11e', '14f', '15f', '16f', '17f', '18f', '19f'}, #8
{'3b', '4b', '5b', '6b', '7b', '8b', '18c', '19c', '20c', '18e', '19e', '20e'}, #9
{'3f', '4f', '5f', '6f', '7f', '8f', '18c', '19c', '20c', '18e', '19e', '20e'}] #10

waves = [{'12b', '13b', '14b', '6e', '7e', '8e', '11f', '12f', '13f', '14f'}, #2
{'9c', '10c', '11c', '9e', '10e', '11e', '14d', '15d', '16d', '17d'}, #3
{'15c', '16c', '17c', '8d', '9d', '10d', '11d', '15e', '16e', '17e'}, #4
{'18b', '19b', '20b', '18d', '19d', '20d', '14e', '15e', '16e', '17e'}, #5
{'6c', '7c', '8c', '18d', '19d', '20d', '21d', '6f', '7f', '8f'}, #6
{'2c', '3c', '4c', '5c', '12d', '13d', '14d', '12f', '13f', '14f'}, #7
{'3b', '4b', '5b', '8c', '9c', '10c', '11c', '3d', '4d', '5d'}, #8
{'14b', '15b', '16b', '17b', '9d', '10d', '11d', '9f', '10f', '11f'}, #9
{'15b', '16b', '17b', '15d', '16d', '17d', '8e', '9e', '10e', '11e'} #10
]

for i in range(len(bio)):
	for j in range(len(chem)):
		for k in range(len(waves)):
			a = bio[i].intersection(chem[j])
			b = bio[i].intersection(waves[k])
			c = waves[k].intersection(chem[j])

			if not a and not b and not c:
				print((i+1,j+1,k+2))