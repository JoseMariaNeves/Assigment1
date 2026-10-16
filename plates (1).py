def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Verifica o tamanho (mínimo 2, máximo 6 carateres)
    if len(s) < 2 or len(s) > 6:
        return False

    # Verifica se contém apenas letras e números (sem pontuação/espaços)
    if not s.isalnum():
        return False

    # As duas primeiras carateres têm de ser letras
    if not s[:2].isalpha():
        return False

    # Validação dos números
    for i in range(len(s)):
        if s[i].isdigit():
            # O primeiro número não pode ser '0'
            if s[i] == '0':
                return False

            # A partir do primeiro número, todos os carateres restantes têm de ser números
            if not s[i:].isdigit():
                return False

            # Interrompe o loop pois já validou o resto da string
            break

    return True


if __name__ == "__main__":
    main()

