temp = input("Saisissez la température que vous souhaitez convertir ? (par exemple, 45F, 102C etc.) : ")


if temp[-1] == "F" :
    new_temp = round((float(temp[:-1]) - 32)/1.8,2)
    print(f"La température en Celsius est de {new_temp} degrés.")
elif temp[-1] == "C" :
    new_temp = round(float(temp[:-1])*1.8 + 32,2)
    print (f"La température en Fahrenheit est de {new_temp} degrés.\nN'utilisez jamais les Fahrenheit, vous vous faites du mal.")
else :
    print("Unité non reconnue (F ou C attendus).")
