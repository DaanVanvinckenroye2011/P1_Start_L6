def ontcijfer(bericht, key):
    ontcijferd_bericht = ""
    for letter in bericht:
        if letter in key:
            ontcijferd_bericht += letter
    return ontcijferd_bericht
