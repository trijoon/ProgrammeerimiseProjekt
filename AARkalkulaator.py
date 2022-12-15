from easygui import *


valikud1 = ["Kahendsüsteemis arvu", "Kümnendsüsteemis arvu", "Kaheksandsüsteemis arvu", "Kuueteistkümnendsüsteemis arvu"]
valik1 = choicebox("Mida soovid teisendada?", "AAR kalkulaator", valikud1)



# Kahendsüsteemis arv
if valik1 == valikud1[0]:
    valikud2 = ["Kümnendsüsteemis arvuks", "Kaheksandsüsteemis arvuks", "Kuueteistkümnendsüsteemis arvuks"]
    valik2 = choicebox("Milleks soovid teisendada?", "Kahend -> ???", valikud2)


    # Kahendsüsteemis arv kümnendsüsteemis arvuks
    if valik2 == valikud2[0]:
        arv = int(enterbox("Sisesta arv: ", "Kahend -> kümnend"))
        kümnend = 0
        i = 0
        while arv:
            kümnend = kümnend + (arv % 10) * 2 ** i
            i += 1
            arv = arv // 10

        teisendus = msgbox("Vastus: " + str(kümnend), "Kahend -> kümnend")


    # Kahendsüsteemis arv kaheksandsüsteemis arvuks
    elif valik2 == valikud2[1]:
        arv = int(enterbox("Sisesta arv: ", "Kahend -> kaheksand"))
        kaheksand = 0
        kümnend = 0
        i = 0
        while arv:
            kümnend = kümnend + (arv % 10) * 2 ** i
            i += 1
            arv = arv // 10
        i = 1
        while kümnend:
            kaheksand = kaheksand + (kümnend % 8) * i
            kümnend = kümnend // 8
            i *= 10

        teisendus = msgbox("Vastus: " + str(kaheksand), "Kahend -> kaheksand")


    # Kahendsüsteemisarv kuueteistkümnendsüsteemis arvuks
    elif valik2 == valikud2[2]:
        arv = int(enterbox("Sisesta arv: ", "Kahend -> kuueteistkümnend"))
        kümnend = 0
        i = 0
        while arv:
            kümnend = kümnend + (arv % 10) * 2 ** i
            i += 1
            arv = arv // 10

        teisendus = msgbox("Vastus: " + hex(kümnend)[2:].upper(), "Kahend -> kuueteistkümnend")


# Kümnendsüsteemis arv
elif valik1 == valikud1[1]:
    valikud2 = ["Kahendsüsteemis arvuks", "Kaheksandsüsteemis arvuks", "Kuueteistkümnendsüsteemis arvuks"]
    valik2 = choicebox("Milleks soovid teisendada?", "Kümnend -> ???", valikud2)


    # Kümnendsüsteemis arv Kahendsüsteemis arvuks
    def kümnend_kahend(arv):
        return "{0:b}".format(int(arv))

    if valik2 == valikud2[0]:
        arv = int(enterbox("Sisesta arv: ", "Kümnend -> kahend"))
        if arv >= 1:
            arv = kümnend_kahend(arv)

        teisendus = msgbox("Vastus: " + str(arv), "Kümnend -> kahend")


    # Kümnendsüsteemis arv Kaheksandsüsteemis arvuks
    elif valik2 == valikud2[1]:
        arv = int(enterbox("Sisesta arv: ", "Kümnend -> kaheksand"))
        vastus = 0
        i = 0
        kümnend = arv
        while kümnend > 0:
            vastus += ((kümnend % 8) * (10 ** i))
            kümnend = int(kümnend / 8)
            i += 1

        teisendus = msgbox("Vastus: " + str(vastus), "Kümnend -> kaheksand")


    # Kümnendsüsteemis arv Kuueteistkümnendsüsteemis arvuks
    teisendus_tabel = {0: "0", 1: "2", 2: "", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8",
                       9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    def kümnend_kuueteistkümnend(arv):
        kuueteistkümnend = ""
        while arv > 0:
            jääk = arv % 16
            kuueteistkümnend += teisendus_tabel[jääk]
            arv = arv // 16

        return kuueteistkümnend


    if valik2 == valikud2[2]:
        arv = int(enterbox("Sisesta arv: ", "Kümnend -> kuueteistkümnend"))
        teisendus = msgbox("Vastus: " + hex(arv)[2:].upper(), "Kümnend -> kuueteistkümnend")
        # if arv >= 1:
        #     arv = kümnend_kuueteistkümnend(arv)
        #
        # teisendus = msgbox("Vastus: " + str(arv), "Kümnend -> kuueteistkümnend")



# Kaheksandsüsteemis arv
elif valik1 == valikud1[2]:
    valikud2 = ["Kahendsüsteemis arvuks", "Kümnendsüsteemis arvuks", "Kuueteistkümnendsüsteemis arvuks"]
    valik2 = choicebox("Milleks soovid teisendada?", "Kaheksand -> ???", valikud2)


    # Kaheksandsüsteemis arv kahendsüsteemis arvuks
    if valik2 == valikud2[0]:
        arv = int(enterbox("Sisesta arv: ", "Kaheksand -> kahend"))
        kahend = 0
        kümnend = 0
        i = 1
        j = 1
        while arv:
            kümnend += (arv % 10) * i
            i *= 8
            arv //= 10
        while kümnend:
            kahend += (kümnend % 2) * j
            j *= 10
            kümnend //= 2

        teisendus = msgbox("Vastus: " + str(kahend), "Kaheksand -> kahend")


    # Kaheksandsüsteemisarv kümnendsüsteemis arvuks
    elif valik2 == valikud2[1]:
        arv = int(enterbox("Sisesta arv: ", "Kaheksand -> kümnend"))
        kümnend = 0
        i = 1
        j = 1
        while arv:
            kümnend += (arv % 10) * i
            i *= 8
            arv //= 10

        teisendus = msgbox("Vastus: " + str(kümnend), "Kaheksand -> kümnend")


    # Kaheksandsüsteemis arv kuueteistkümnendsüsteemis arvuks
    elif valik2 == valikud2[2]:
        arv = int(enterbox("Sisesta arv: ", "Kaheksand -> kuueteistkümnend"))
        kümnend = 0
        i = 1
        j = 1
        while arv:
            kümnend += (arv % 10) * i
            i *= 8
            arv //= 10

        teisendus = msgbox("Vastus: " + hex(kümnend)[2:].upper(), "Kaheksand -> kuueteistkümnend")



# Kuueteistkümnendsüsteemis arv
elif valik1 == valikud1[3]:
    valikud2 = ["Kahendsüsteemis arvuks", "Kümnendsüsteemis arvuks", "Kaheksandsüsteemis arvuks"]
    valik2 = choicebox("Milleks soovid teisendada?", "Kuueteistkümnend -> ???", valikud2)


    # Kuueteistkümnendsüsteemis arv kahendsüsteemis arvuks
    if valik2 == valikud2[0]:
        arv = enterbox("Sisesta arv: ", "Kuueteistkümnend -> kahend")
        teisendus = msgbox("Vastus: " + bin(int(arv, 16))[2:], "Kuueteistkümnend -> kahend")


    # Kuueteistkümnendsüsteemis arv kümnendsüsteemis arvuks
    elif valik2 == valikud2[1]:
        arv = enterbox("Sisesta arv: ", "Kuueteistkümnend -> kümnend")
        teisendus = msgbox("Vastus: " + str(int(arv, 16)), "Kuueteistkümnend -> kümnend")


    # Kuueteistkümnendüsteemis arv kaheksandsüsteemis arvuks
    elif valik2 == valikud2[2]:
        arv = enterbox("Sisesta arv: ", "Kuueteistkümnend -> kaheksand")
        vastus = 0
        i = 0
        kümnend = int(arv, 16)
        while kümnend > 0:
            vastus += ((kümnend % 8) * (10 ** i))
            kümnend = int(kümnend / 8)
            i += 1

        teisendus = msgbox("Vastus: " + str(vastus), "Kuueteistkümnend -> kaheksand")