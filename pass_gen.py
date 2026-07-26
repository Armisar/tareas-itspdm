import random
import string

def generar_password():
    print("=" * 40)
    print(" 🔐 GENERADOR DE CONTRASEÑAS SEGURAS 🔐")
    print("=" * 40)
    
    longitud = int(input("¿Cuántos caracteres quieres que tenga la contraseña? (Mínimo 8): "))
    if longitud < 8:
        longitud = 8
        print("-> Por seguridad, la ajustaremos a 8 caracteres mínimo.")
    
    incluir_simbolos = input("¿Incluir símbolos especiales? (!@#$%...) (s/n): ").lower() == 's'
    
    # Conjunto de caracteres base
    caracteres = string.ascii_letters + string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
        
    # Generar la contraseña aleatoria
    password = "".join(random.choice(caracteres) for _ in range(longitud))
    
    print("\n" + "-" * 40)
    print(f"🔑 Tu contraseña generada es: {password}")
    print("-" * 40)

# Ejecutar programa
generar_password()
