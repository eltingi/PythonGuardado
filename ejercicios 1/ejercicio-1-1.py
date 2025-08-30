
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duracino de videos sin editar (crudo)
crudo_promedio = 5
crudo_dalto = 3.5

#diferencia de duracion / crudo(video sin editar)
diferencia_con_min = 100 -  (dalto_curso / otros_cursos_min * 100)

#primera forma
#diferencia_con_max = 100 -  (dalto_curso / otros_cursos_max * 100) # resultado 78.57142857142857

#segunda forma
# las doble "//" significan que el resulta dedondeando a entero
# de esta forma de la mas numeros al decimal y lo divide en 10 para eliminar los decimales extras
diferencia_con_max = 100 -  (dalto_curso * 1000 // otros_cursos_max / 10) # resultado 78.57142857142857

diferencia_con_promedio = 100 -  (dalto_curso / otros_cursos_promedio * 100)

#calculo el porcentaje de tiempo vacion removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dato = 100 - dalto_curso * 1000 // crudo_dalto / 10


print(f"El curso de Dalto dura un {diferencia_con_min} menos que el mas rapido"  )
print(f"El curso de Dalto dura un {diferencia_con_max} menos que el mas lento"  )
print(f"El curso de Dalto dura un {diferencia_con_promedio} menos que el promedio"  )

print("----------------------------------------------------------")

#mostrando la cantidad de espacios vacios que se remueven (ejercicio B)    
print(f"Un curso promedio elimina  un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"Esta curso elimino el {tiempo_vacio_dato}% de tiempo vacio")

print("----------------------------------------------------------")

#mostrando diferenbcia si los cursos duraran 10 horas
print(f"Ver 10 horas de esta curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos")
print(f"Ver 10 horas de otros curso equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este cursos")


print("----------------------------------------------------------")