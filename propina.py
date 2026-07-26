# --- CALCULADORA DE PROPINAS ---

def calcular_propina():
    print("=" * 30)
    print(" 🧾 CALCULADORA DE PROPINAS 🧾")
    print("=" * 30)
    
    total_cuenta = float(input("¿Cuánto fue el total de la cuenta? $"))
    porcentaje = float(input("¿Qué porcentaje de propina quieres dejar? (10, 15, 20): "))
    personas = int(input("¿Entre cuántas personas se va a dividir la cuenta? "))
    
    # Cálculos
    monto_propina = total_cuenta * (porcentaje / 100)
    total_general = total_cuenta + monto_propina
    cuota_por_persona = total_general / personas
    
    print("\n--- RESUMEN ---")
    print(f"Propina total: ${monto_propina:.2f}")
    print(f"Total a pagar: ${total_general:.2f}")
    print(f"Cada persona paga: ${cuota_por_persona:.2f}")
    print("=" * 30)

# Ejecutar la función
calcular_propina()
