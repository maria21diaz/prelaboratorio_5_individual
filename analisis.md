# Analisis - Pedido de Impresion




# 1.Entradas y Salidas:

## entradas -->
- *Paginas por paquete:* Tipo `int`. Se piden 3 entradas por consola mediante `input()`, una para cada paquete (Apuntes, Guia de ejercicios, Material de consulta)

## salidas -->
- *Paquetes aceptados:* Tipo `int`. Cantidad de paquetes que cumplieron con el formato valido.
- *Total de paginas:* Tipo `int`. Suma total de paginas de los paquetes aceptados.
- *Subtotal:* Resultado de multiplicar el total de paginas por el precio unitario (2 unidades monetarias).
- *Descuento:* Tipo `float`. Monto correspondiente al 10% de descuento si el total de paginas supera las 100 unidades.
- *Total a pagar:* Tipo `float`. Resultado de restar el descuento al subtotal.
- *Mensaje de estado:* Tipo `str`. Indica si el pedido fue generado o si no se acepto ningun paquete.

----------------------------------------------------------------------------------------------------------------

# 2.Restricciones Explicitas e Implicitas

## Restricciones Explicitas -->
1. El pedido tiene 3 paquetes especificos
2. Cada paquete debe tener entre 1 y 50 paginas incluyendo los limites.
3. cada pagina cuesta 2 unidades monetarias.
4. Se aplica un descuento del 10% sobre el subtotal solo si el total de paginas aceptadas es mayor a 100 (Con exactamente 100 paginas no aplica descuento).
5. Se permite un solo intento por paquete. Si la entrada es invalida, se omite.
6. Si no se acepta ningun paquete, no se genera el pedido y todos los importes deben mostrarse en 0.

## Restricciones Implicitas -->
1. Las entradas que sean de texto (str), simbolos o numeros decimales (float) no se convertiran a `int` y deben ser descartadas por `try-except ValueError`
2. Cantidades negativas o mayores a 50 deben ser rechazadas.
3. El paquete omitido no debe sumar en el contador de paquetes ni en el total de paginas acumuladas.

------------------------------------------------------------------------------------------------------------------------



# 3.Ambiguedades:
No se identificaron ambiguedades en el enunciado. Todas las reglas, limites inclusivos, precios, condiciones de descuento y manejo de errores estan detallados en el texto

------------------------------------------------------------------------------------------------------------------------

# 4.Precondiciones y Postcondiciones:

### Programa Principal

- *Precondicion:* El usuario debe interactuar con la consola para ingresar las cantidades solicitadas de cada paquete.
- *Postcondicion:* Se imprime un informe final en consola indicando la cantidad de paquetes aceptados, total de paginas, subtotal, descuento y total a pagar. Si no hubo paquetes aceptados, se notifica y se muestran valores en cero.


### calcular_subtotal
- *Precondicion:* Recibe un entero `total_paginas` y un entero/float `precio_pagina` 
- *Postcondicion:* Retorna un valor numerico equivalente al producto de `total_paginas * precio_pagina`.


-------------------------------------------------------------------------------------------------------------------------

### Registro de Pruebas 

1. - *Caso exitoso con descuento:* 40, 35, 30 -->  3 paquetes; 105 páginas; subtotal 210; descuento 21; total 189.   
2. - *Caso con texto y limite de 100:* 50, 50, hola --> 2 paquetes; 100 páginas; subtotal 200; descuento 0; total 200.   
3. - *Caso donde falla:* 0, 51, texto --> 0 paquetes; 0 páginas; importes 0; mensaje de que no se generó un pedido.