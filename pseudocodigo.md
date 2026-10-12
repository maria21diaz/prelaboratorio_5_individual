# Pseudocodigo - Pedido de Impresion

INICIO

    // Definicion de constantes y lista de paquetes
    CONSTANTE PRECIO_PAGINA = 2
    paquetes = ["Apuntes", "Guia de ejercicios", "Material de consulta"]
    
    // Acumuladores 
    paquetes_aceptados = 0
    total_paginas = 0

    // Funcion para el subtotal
    FUNCION calcular_subtotal(paginas, precio)
        RETORNAR paginas * precio
    FIN FUNCION

    // Recorrido de la lista de paquetes por indice
    PARA indice DESDE 0 HASTA LONGITUD(paquetes)- 1 HACER
        nombre_paquete = paquetes[indice]
        MOSTRAR "Ingrese la cantidad de paginas para: " + nombre_paquete
        LEER entrada

        //  conversion a numero entero
        INTENTAR
            paginas = CONVERTIR_A_ENTERO(entrada)
        SI FALLA_CONVERSION ENTONCES
            MOSTRAR "Entrada invalida. Se omite el paquete."
            CONTINUAR // Salta a la siguiente iteracion del ciclo for
        FIN INTENTAR

        // Validar el rango permitido (1 a 50)
        SI paginas < 1 O  paginas > 50 ENTONCES
            MOSTRAR "Paginas fuera de rango (1-50). Se omite el paquete."
            CONTINUAR // Salta a la siguiente iteracion del ciclo for
        FINSI

        // Si pasa ambas validaciones, se acumula
        paquetes_aceptados = paquetes_aceptados + 1
        total_paginas = total_paginas + paginas

    FIN PARA

    // Calculo del subtotal llamando a la funcion
    subtotal = LLAMAR calcular_subtotal(total_paginas, PRECIO_PAGINA)

    // Descuento del 10% solo si supera las 100 paginas
    SI total_paginas > 100 ENTONCES
        descuento = subtotal * 0.10
    SINO
        descuento = 0.0
    FIN SI

    total_pagar = subtotal - descuento

    // Reporte final de resultados
    SI paquetes_aceptados == 0 ENTONCES
        MOSTRAR "No se genero un pedido."
        MOSTRAR "Paquetes aceptados: 0"
        MOSTRAR "Total paginas: 0"
        MOSTRAR "Subtotal: 0"
        MOSTRAR "Descuento: 0"
        MOSTRAR "Total a pagar: 0"
    SINO
        MOSTRAR "Paquetes aceptados: " + paquetes_aceptados
        MOSTRAR "Total paginas: " + total_paginas
        MOSTRAR "Subtotal: " + subtotal
        MOSTRAR "Descuento: " + descuento
        MOSTRAR "Total a pagar: " + total_pagar
    FIN SI

FIN