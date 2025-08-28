# Ejercicio 4: Declarar variables de diferentes tipos de datos básicos y mostrar su información

# Declaración de variables
edad = 20                # int
promedio = 8.5           # float
nombre = "Juan"          # str
activo = True            # bool

# Mostrar valor y tipo de cada variable usando type()
print(f"Variable: edad = {edad}, Tipo: {type(edad)}")
print(f"Variable: promedio = {promedio}, Tipo: {type(promedio)}")
print(f'Variable: nombre = "{nombre}", Tipo: {type(nombre)}')
print(f"Variable: activo = {activo}, Tipo: {type(activo)}")

# Operaciones básicas entre variables compatibles
print("\n--- Operaciones Básicas ---")
print(f"Suma de edad + promedio = {edad + promedio}")     # int + float
print(f"Multiplicación de edad * 2 = {edad * 2}")         # int * int
print(f"Concatenación de nombre + ' Pérez' = {nombre + ' Pérez'}")  # str + str
print(f"Negación de activo = {not activo}")               # operación lógica con bool