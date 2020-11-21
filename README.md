# Ejercicio-biopython
Descripción del funcionamiento del scrip.py: importamos las bibliotecas necesarias para utilizar biopython, se definen variasfunciones:  
-**summarize_contents**: imprime un resumen del contenido de un archivo en formato .gbk (genbank), el output de esta función es un diccionario con el siguiente formato: file: [nombre de archivo] path: [ruta al archivo] num_records: [numero de registros] records: - id: [id del primer registro] name: [nombre] description: [descripción] - id: [id del segundo registro] name: [nombre] description: [descripción] - ...   
-**concatenate_and_get_reverse_of_complement**: recibe como entrada dos secuencias de ADN, y que regresa como salida una cadena con el complemento inverso de su concatenación.   
-**print_protein_and_codons_using_standard_table**: recibe una secuencia de DNA,  y regresa un diccionario que incluye la secuencia de RNA mensajero y la secuencia de la(s) proteína(s) correspondientes, así como los codones de paro, de acuerdo a la tabla de traducción estándar.    
-**print_protein_and_codons_using_mitocondrial_yeast_table**:recibe una secuencia de DNA,  y regresa un diccionario que incluye la secuencia de RNA mensajero y la secuencia de la(s) proteína(s) correspondientes, así como los codones de paro, de acuerdo a la tabla de traducción del código mitocondrial de levadura.     
-**extract_sequences**:recibe 2 argumentos, el primero corresponde al nombre de un archivo que se asume está en formato .fasta. La función debe leer las secuencias contenidas en él y generar N archivos FASTA de secuencia única (sólo una secuencia en cada archivo generado). El segundo parametro es el nombre del formato de los archivos de salida (solo admite formato genbank)     
-**extract_sequences_revcomp**: recibe un archivo FASTA obtiene otro archivo de tipo FASTA donde cada secuencia es el complemente inverso.      

