# Programa convertidor de tipo de cambio.

# mensaje de bienvenida

print("""Programa que imprimie el tipo de cambio en las monedas: 
    1.- Dolarés.
    2.- Euros. 
    3.- Yuan. 
    """);


# Pedir el monto de pesos a cambiar: 

pesos = float (input("Ingrese la cantidad pesos a cambiar:  "));

# convertidor: 

dolares = (pesos / 20.22);
euros = pesos / 21.33;
yuanes =  pesos / 3.04;


#imprimir resultados 

print(" Convertidor: cambiar " + str(pesos) + " a dolares es igual a " + str(round(dolares,2)) +" dolarés.");

print(" Convertidor: cambiar " + str(pesos) + " a euros es igual a " + str(round(euros,2)) +" euros.");

print(" Convertidor: cambiar " + str(pesos) + " a yuanes es igual a " + str(round(yuanes,2)) +" yuanes.");


# Atajo para emojis:
# Windows: windows + .
# Mac: ctrl + command + space
# Linux: hay que descargar una aplicación de tercero (e.g EmojiOne Picker)

