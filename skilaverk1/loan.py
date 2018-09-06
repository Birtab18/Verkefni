hofudstoll = int(input("Input the cost of the item in $: "))
manudir = 0
heildarvextir = 0

# vaxtarprosenta:
if hofudstoll <= 1000:
    vaxtarprosenta = float(0.015)
else:
    vaxtarprosenta = float(0.02)


while hofudstoll > 0:
    vextir_borgadir = hofudstoll * vaxtarprosenta

    #greidsla_a_man (skiptist i afborganir og vexti)
    if hofudstoll >= 50:
        greidsla_a_man = 50.0
    else:
        greidsla_a_man = hofudstoll + vextir_borgadir
    

    afborgun_a_man = greidsla_a_man - vextir_borgadir

    manudir = manudir + 1

    hofudstoll = hofudstoll - afborgun_a_man

    heildarvextir = heildarvextir + vextir_borgadir



    print("Month:", manudir, "Payment:", round(greidsla_a_man,2), "Interest paid:", round(vextir_borgadir,2),"Remaining debt:", round(hofudstoll,2))

print("\nNumber of months:", manudir)
print("Total interest paid:", round(heildarvextir,2))