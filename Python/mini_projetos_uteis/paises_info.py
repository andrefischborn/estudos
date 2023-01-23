from countryinfo import CountryInfo     # pip install countryinfo no powershell


country = CountryInfo(input('Digite o nome do país: ')) # O NOME DOS PAÍSES DEVEM SER EM INGLES, ex: Finland, Japan, Brazil

print(f'País: {country.name()}')
print(f'Capital: {country.capital()}')
print(f'Moedas: {country.currencies()}')
print(f'Idiomas: {country.languages()}')
print(f'Fazem fronteira: {country.borders()}')
print(f'Código de área: {country.calling_codes()}')
print(f'População Atual: {country.population()}')
