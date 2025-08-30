#con el permiso "w" si no exiete el archivo lo crea automaticamente
with open('archivos\\text_en_txt.txt','w',encoding='UTF-8') as archivito:
    #sobreescribiendo el archivo
    #archivito.write("Hola empece de nuevo")
    
    #whitelines resive un parametro por lo que si deseamos mandar mas de 1 cadena de texto, mandamos una lista
    #whitelines a diferencia de white, va agregando texto dentro del archivo
    
    #ejemlo agregando 2 iguales
    archivito.writelines(["Hola Hola nuevamente \n","Hola hola hola hola \n"])
    archivito.writelines(["pikachu \n","charmander \n"])
    
    
    
    

    
    