#Primer ejercicio en python
nombre = input("por fsvor dime tu nombre: ")
ventas = int(input("Diga sus ventas totales del mes: "))


comisiones = round(ventas * 13 / 100,2)
print(f"Hola {nombre}, tus comisiones de este mes son de {comisiones}")



