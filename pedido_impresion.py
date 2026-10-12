

PRECIO_PAGINA = 2

def calcular_subtotal(total_paginas, precio_pagina): #Calcula el subtotal multiplicando las paginas aceptadas por el precio unitario
    return total_paginas * precio_pagina

def main():
    paquetes = ["Apuntes", "Guia de ejercicios", "Material de consulta"]
    paquetes_aceptados = 0
    total_paginas = 0

    for i in range(len(paquetes)):
        nombre_paquete = paquetes[i]
        entrada = input(f"Ingrese la cantidad de paginas para '{nombre_paquete}': ")
        
        try:
            paginas = int(entrada)
            if paginas < 1 or paginas > 50:
                print(f"Paginas fuera de rango (1-50) para {nombre_paquete}. Se omite.")
                continue
        except ValueError:
            print(f"Entrada invalida para {nombre_paquete}. Se omite.")
            continue

        paquetes_aceptados += 1
        total_paginas += paginas

    subtotal = calcular_subtotal(total_paginas, PRECIO_PAGINA)
    
    if total_paginas > 100:
        descuento = subtotal * 0.10
    else:
        descuento = 0.0

    total_a_pagar = subtotal - descuento

    print("\n -- RESUMEN DEL PEDIDO --")
    
    if paquetes_aceptados == 0:
        print("No se genero un pedido.")
        print("Paquetes aceptados: 0")
        print("Total paginas: 0")
        print("Subtotal: 0")
        print("Descuento: 0")
        print("Total a pagar: 0")
    else:
        print(f"Paquetes aceptados: {paquetes_aceptados}")
        print(f"Total paginas: {total_paginas}")
        print(f"Subtotal: {subtotal}")
        print(f"Descuento: {descuento}")
        print(f"Total a pagar: {total_a_pagar}")


main()