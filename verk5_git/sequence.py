# Fyrst læt ég notandann slá inn tölu sem segir til um hversu margar tölur í rununnii hann vill sjá
# Ég nota for lykkju með range-i frá einum og upp í töluna sem notandinn slær inn
# Reglan á rununni er að tala er summa af þrem síðustu tölunum, þess vegna er 1,2 og 3 special case þar sem við höfum enga history fyrir þær
# Ef 1,2 eða 3 kemur upp prentum við tölurnar út
# Þar væri 1=first, 2=second og 3=third og búum til nýja breytu sem heitir summa og er (first+second+third)
# Þá breytum við hvað er breytunum þannig að first=second, second=third, third=summa
    
n = int(input("Enter the length of the sequence: ")) # Do not change this line

first = 1
second = 2
third = 3

for i in range(1,n+1):
    if i == 1:
        print(first)
    elif i == 2:
        print(second)
    elif i == 3:
        print(third)
    else:
        summa = first + second + third
        print(summa)    
        
        
        first = second
        second = third
        third = summa
        
        