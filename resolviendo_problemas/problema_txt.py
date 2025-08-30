
#aqui tendremos uan lista que viene de algun lado la cual sera pintada ewn un archivo txt

nombres = ["Mauricio","Marcos","Pedro","Pablo"]
apellidos = ["S","M","P","P2"]

with open("resolviendo_problemas\\nombres_y_apellidos.txt","w") as archivito:
    archivito.writelines("Los datos son los siguientes: \n\n")
    #aqui corremos en una linea el FOR dentro del [], y ocupamos el comando zip.
    #ZIP: empareja listas distintas para poder ser recorridas por el for
    [archivito.writelines(f"Nombres: {n}\nApellido: {a} \n-------------\n") for n,a in zip(nombres,apellidos)]
    
