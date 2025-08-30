
#agregarndo el permiso a
with open('archivos\\text_en_txt.txt','a',encoding='UTF-8') as archivito:
       
    archivito.write("\n")
    #recordar que range con un aprametro empiecea dse 0
    for i in range(5):        
        archivito.write(f"wena linea {i+1} agregada \n")
    

    
    
    