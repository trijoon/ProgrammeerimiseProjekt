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
        kaheksand = 0
        kümnend = 0
        i = 0
        while arv != 0:
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
        while arv != 0:
            kümnend = kümnend + (arv % 10) * 2 ** i
            i += 1
            arv = arv // 10

        i = 1
        while kümnend != 0:
            kaheksand = kaheksand + (kümnend % 8) * i
            kümnend = kümnend // 8
            i *= 10

        teisendus = msgbox("Vastus: " + str(kaheksand), "Kahend -> kaheksand")


    # Kahendsüsteemisärv kuueteistkümnendsüsteemis arvuks
    elif valik2 == valikud2[2]:
        arv = int(enterbox("Sisesta arv: ", "Kahend -> kuueteistkümnend"))



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
    if valik2 == valikud2[1]:
        arv2 = int(enterbox("Sisesta arv: ", "Kümnend -> kaheksand"))
        vastus = 0
        ctr = 0
        kümnend = arv2

        while (kümnend > 0):
            vastus += ((kümnend % 8) * (10 ** ctr))
            kümnend = int(kümnend / 8)
            ctr += 1

        teisendus = msgbox("Vastus: " + str(vastus), "Kümnend -> kaheksand")

    # Kümnendsüsteemis arv Kuueteistkümnend süsteemis arvuks
    teisendus_tabel = {0: "0", 1: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8",
                       9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}


    def kümnend_kuueteistkümnend(arv3):
        kuueteistkümnend = " "
        while (arv3 > 0):
            jääk = arv3 % 16
            kuueteistkümnend = teisendus_tabel[jääk] + kuueteistkümnend
            arv3 = arv3 // 16

        return kuueteistkümnend


    if valik2 == valikud2[2]:
        arv3 = int(enterbox("Sisesta arv: ", "Kümnend -> kuueteistkümnend"))
        if arv3 >= 1:
            arv3 = kümnend_kuueteistkümnend(arv3)

        teisendus = msgbox("Vastus: " + str(arv3), "Kümnend -> kuueteistkümnend")



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
        while (arv):
            kümnend += (arv % 10) * i
            i *= 8
            arv //= 10

        while (kümnend):
            kahend += (kümnend % 2) * j
            j *= 10
            kümnend //= 2

        teisendus = msgbox("Vastus: " + str(kahend), "Kaheksand -> kahend")


    # Kaheksandsüsteemisarv kümnendsüsteemis arvuks
    elif valik2 == valikud2[1]:
        arv = int(enterbox("Sisesta arv: ", "Kaheksand -> kümnend"))
        kahend = 0
        kümnend = 0
        i = 1
        j = 1
        while (arv):
            kümnend += (arv % 10) * i
            i *= 8
            arv //= 10

        teisendus = msgbox("Vastus: " + str(kümnend), "Kaheksand -> kümnend")


    # Kaheksandsüsteemis arv kuueteistkümnendsüsteemis arvuks
    elif valik2 == valikud2[2]:
        arv = int(enterbox("Sisesta arv: ", "Kaheksand -> kuueteistkümnend"))




# Kuueteistkümnendsüsteemis arv
elif valik1 == valikud1[3]:
    valikud2 = ["Kahendsüsteemis arvuks", "Kümnendsüsteemis arvuks", "Kaheksandsüsteemis arvuks"]
    valik2 = choicebox("Milleks soovid teisendada?", "Kuueteistkümnend -> ???", valikud2)