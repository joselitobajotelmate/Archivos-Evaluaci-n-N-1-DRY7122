# Defina ACL estandar, extendida o el numero no corresponde a una lista de acceso

acl_ranges = {
    "min": 1,
    "max": 99,
    "ex_min": 100,
    "ex_max": 199,
}

acl_number = input("Ingrese el número de la ACL IPv4: ")

if acl_number.isdigit():
    acl_number = int(acl_number)
    if acl_ranges["min"] <= acl_number <= acl_ranges["max"]:
        print(f"La ACL {acl_number} es una ACL Estándar.")
    elif acl_ranges["ex_min"] <= acl_number <= acl_ranges["ex_max"]:
        print(f"La ACL {acl_number} es una ACL Extendida.")
    else:
        print(f"El número {acl_number} no corresponde a una lista de acceso.")
else:
    print(f"El valor ingresado no es un nuumero valido.")


