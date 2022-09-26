from datetime import datetime, timedelta




fakturaDatum = datetime.now()
forfallodag = fakturaDatum + timedelta(days=30)
if forfallodag.weekday() == 5: #Lördag 29 
    forfallodag = forfallodag - timedelta(days=1) 
if forfallodag.weekday() == 6: #Söndag 31
    forfallodag = forfallodag + timedelta(days=1)

formattedForFalloDag = forfallodag.strftime("%Y-%m-%d")
print(f"Förfallodag: {formattedForFalloDag}")





def getWeekDayName(weekday:int) -> str: 
    if weekday == 0:
        return "Måndag"
    if weekday == 1:
        return "Tisdag"
    if weekday == 2:
        return "Onsdag"
    if weekday == 3:
        return "Torsdag"
    if weekday == 4:
        return "Fredag"
    if weekday == 5:
        return "Lördag"
    if weekday == 6:
        return "Söndag"
    return "Ogiltig dag"

nu = datetime.now()
jullovet = datetime(2022,12,14)
print(f"Antal dagar till jullovet:{(jullovet-nu).days}")    

diff = jullovet - nu
dagar = diff.days
print(f"Antal dagar till jullovet:{dagar}")    


while True:
    year = int(input("Ange år du är född:"))
    mon = int(input("Ange månad du är född:"))
    dag = int(input("Ange dag du är född:"))
    birthDate = datetime(year,mon, dag)
    # Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
    weekday = getWeekDayName(birthDate.weekday())

    nu = datetime.now()

    diff = nu - birthDate

    print(f"Du är född på en {weekday}")
    print(f"Har du utnyttjat alla {diff} dagar väl?")

nu = datetime.now()
while nu.hour < 16:
    print("Vara kvar på skolan")
    nu = datetime.now()

    

if nu.month == 9 or nu.month == 10 or nu.month == 11:
    print("Beklagar...tråkig höst är det nu")
elif nu.month == 12:     
    print("Julmånad")
print(nu)




























julAfton = datetime(2021,12,24)
idag =  datetime.now()
timespan = julAfton - idag
print(f"Det är {timespan.days} dagar")

invoiceDate = datetime.now()
forFalloDag =  invoiceDate +  timedelta(days=32)
print(forFalloDag.weekday())
if forFalloDag.weekday() == 5:
    forFalloDag = forFalloDag - timedelta(days=1)
if forFalloDag.weekday() == 6:
    forFalloDag = forFalloDag + timedelta(days=1)

formattedInvoiceDate = invoiceDate.strftime('%Y-%m-%d')
print(f"Fakturadatum: {formattedInvoiceDate}")
formattedForFalloDag = forFalloDag.strftime('%Y-%m-%d')
print(f"Förfallodag: {formattedForFalloDag}")

while True:
    print("Skriv in din födelsedag - ex 1972-08-03:")
    datum = input()
    dat = datetime.strptime(datum, "%Y-%m-%d" )
    print(f"Du är född på en {dat.weekday()}")

precisNu = datetime.now()
#print(precisNu)

#snyggTid = f"{precisNu.year}-{precisNu.month}-{precisNu.day}"
snyggTid = precisNu.strftime("%Y-%m-%d")
print(snyggTid)



ettAnnat = datetime(1972,8,3)


jagArFoddDettaDatum = datetime(1972,8,3)
print(jagArFoddDettaDatum.weekday() )

weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

print(weekDays[3])
print(weekDays[jagArFoddDettaDatum.weekday()])


lista = [12,22,33]
dc = { "Namn":"Kalle", "Adress":"Hejgatan12"}
print(dc['Namn'])

idag = datetime.now()

if idag.day != 1:
    print("Kör batch")

print(idag.year)
print(idag.month)
print(idag.day)
#DEBUG OCH SE. Hmmm
# i denna "låda" idag ligger
# det massa delar inte som lista/dictionary
#utan på ett tredje sätt. What???
#Hello OOP ;)
print(idag)