# Ejercicio 1: Imprimir en cursiva la estrofa de la canción "Bendita tierra" de Kime

# Código ANSI para activar cursiva (I) y para restablecer el formato (R)
I = "\033[3m"
R = "\033[0m"

# Primera línea en cursiva
print(f"{I}Vivo enamorado de este suelo,{R}")

# Segunda línea en cursiva
print(f"{I}No me canso de tu luna y de tu cielo,{R}")

# Tercera línea en cursiva
print(f"{I}Porque yo elegí aquí sembrar mis sueños{R}")

# Cuarta línea en cursiva
print(f"{I}Porque Dios llenó de magia este pueblo{R}")

# Quinta línea en cursiva (respetando las comillas internas alrededor de la palabra yerba)
print(f"{I}Voy desde cipote entre \"la yerba\"{R}")

# Sexta línea en cursiva
print(f"{I}En mi sangre llevo todos tus paisajes{R}")