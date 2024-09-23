def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el monto del descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Programa principal
if __name__ == "__main__":
    # Primera llamada a la función con el monto total
    monto1 = 150.00
    descuento1 = calcular_descuento(monto1)
    total_a_pagar1 = monto1 - descuento1
    print(f"Monto total: ${monto1:.2f}, Descuento: ${descuento1:.2f}, Total a pagar: ${total_a_pagar1:.2f}")

    # Segunda llamada a la función con monto total y porcentaje de descuento
    monto2 = 200.00
    porcentaje_descuento2 = 15
    descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
    total_a_pagar2 = monto2 - descuento2
    print(f"Monto total: ${monto2:.2f}, Descuento: ${descuento2:.2f}, Total a pagar: ${total_a_pagar2:.2f}")



