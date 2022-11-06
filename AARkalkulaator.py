from easygui import *


valikud1 = ["Kahendsüsteemis arvu", "Kümnendsüsteemis arvu", "Kaheksandsüsteemis arvu", "Kuueteistkümnendsüsteemis arvu"]
valik1 = choicebox("Mida soovid teisendada?", "AAR kalkulaator", valikud1)


# Kahendsüsteemis arv
if valik1 == valikud1[0]:
    valikud2 = ["Kümnendsüsteemis arvuks", "Kaheksandsüsteemis arvuks", "Kuueteistkümnendsüsteemis arvuks"]
    valik2 = choicebox("Milleks soovid teisendada?", "Kahend -> ???", valikud2)


    # Kahendsüsteemis arv kümnendsüsteemis arvuks
    if valik2 == valikud2[0]:
        arv = enterbox("Sisesta arv: ", "Kahend -> kümnend")
        vastus = 0
        ring = (len(arv) - 1)

        for number in arv:
            vastus += int(number) * 2**ring
            ring -= 1

        teisendus = msgbox("Vastus: " + str(vastus), "Kahend -> kümnend")


    # Kahendsüsteemis arv kaheksandsüsteemis arvuks
  # elif valik2 == valikud2[1]:



# Kümnendsüsteemis arv
elif valik1 == valikud1[1]:
    valikud2 = ["Kahendsüsteemis arvuks", "Kaheksandsüsteemis arvuks", "Kuueteistkümnendsüsteemis arvuks"]
    valik2 = choicebox("Milleks soovid teisendada?", "Kümnend -> ???", valikud2)


# Kaheksandsüsteemis arv
elif valik1 == valikud1[2]:
    valikud2 = ["Kahendsüsteemis arvuks", "Kümnendsüsteemis arvuks", "Kuueteistkümnendsüsteemis arvuks"]
    valik2 = choicebox("Milleks soovid teisendada?", "Kaheksand -> ???", valikud2)


# Kuueteistkümnendsüsteemis arv
elif valik1 == valikud1[3]:
    valikud2 = ["Kahendsüsteemis arvuks", "Kümnendsüsteemis arvuks", "Kaheksandsüsteemis arvuks"]
    valik2 = choicebox("Milleks soovid teisendada?", "Kuueteistkümnend -> ???", valikud2)