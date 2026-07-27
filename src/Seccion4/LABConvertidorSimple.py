#conversor mak-kam

kilometers = 12.25
miles = 7.38

mak = miles*1.6/1
kam = kilometers*1/1.6

print(miles, "millas son", round(mak, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kam, 2), "millas")

#conversor usd-eur eur-usd

usd=200
eur=185

dae=usd*0.88
ead=eur*1.14

print(usd,"dolares son: ", round(dae,2),"euros")
print(eur,"euros son: ",round(ead,2),"dolares")
