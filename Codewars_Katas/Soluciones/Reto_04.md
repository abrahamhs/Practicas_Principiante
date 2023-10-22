# Persistencia Multiplicativa Nivel < 6kyu >

**Palabras clave: persistencia, multiplicativa, algoritmo, Python, descomposición de dígitos**

**Descripción:**

El objetivo de esta función es calcular la persistencia multiplicativa de un número positivo. La persistencia multiplicativa es el número de veces que debes multiplicar los dígitos de un número hasta llegar a un solo dígito.

**Código:**

```python
def persistence(n):
    # Validamos que n no sea de tipo float para poder calcular su persistencia
    if type(n) == float:
        return None
    # Verificamos si el número es positivo
    if type(n) == int:
        if n < 0:
            return None
        
        # Si el número es de un solo dígito, su persistencia es 0
        elif len(str(n)) == 1:
            return 0
        
        # Si el número tiene más de un dígito, procedemos a calcular su persistencia
        elif len(str(n)) > 1:
            
            # Creamos una lista para almacenar los dígitos y la llenamos en un bucle
            # Usamos un bucle for para llenar la lista a partir de los caracteres de n 
            lista = []
            for i in str(n):
                lista.append(int(i))
                
            # Inicializamos una variable para operar las multiplicaciones y obtener su nuevo valor
            resultado  = 0 
            # Inicializamos un contador de iteraciones
            contador = 0

            # Creamos un bucle que se ejecuta hasta que la lista tenga un solo dígito
            while len(lista) > 1:
                
                # Aumentamos el contador por cada iteración
                contador += 1 

                # Asignamos el valor del primer número de la lista como valor inicial
                # de la multiplicación de sus dígitos.
                resultado  = lista[0] 
                
                # Creamos un bucle que se ejecuta por cada número que tenga en la lista
                # a partir de la posición 1 ya que la posición 0 la hemos usado anteriormente
                for i in range(1, len(lista)):
                    resultado  *= lista[i]
                
                # Convertimos el resultado en una cadena para descomponerlo en dígitos    
                my_str = str(resultado )

                # Almacenamos los dígitos del resultado en la lista nuevamente.
                lista = [int(i) for i in my_str]
            

            # Retornamos el contador de iteraciones, que representa la persistencia
            return contador
