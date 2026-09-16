class Solution: 
    def __init__(self,num_pass,from_,to):
        self.num_pass = num_pass 
        self.from_ = from_ 
        self.to = to 



def input_aufnahme():
    wahr = True  
    trips = []
    while wahr:

        num_pass = int(input("Wie viel Leute sind sie: "))
        from_ = int(input("Von wo: "))
        to = int(input("Bis wohin: "))
        abfrage = input("möchte sie eine weitere Fahrt hinzufügen (falls Ja bitte 'n' eingeben ansonnsten 'Enter drücken'): ")

        if abfrage.strip().lower() == "n":
            weiter = False 

        trips.append(Solution(num_pass,from_,to))

    trips.sort(key=lambda p: p.from_)

    return trips 

def belegung(anfrage):

    Abfahrt_werte = sorted(set(trip.from_ for trip in anfrage) | set(trip.to for trip in anfrage))
    belegt = 0
    max_beleg = 0 
    max_beleg_km = 0          
    max_range = max(trip.to for trip in anfrage)

    for i in Abfahrt_werte:
        for trip in anfrage:
            if i == trip.from_: 
                belegt += trip.num_pass
            elif i == trip.to: 
                belegt -= trip.num_pass

        if belegt > max_beleg:
            max_beleg = belegt
            max_beleg_km = i 

    return max_beleg, max_beleg_km


def main():
    
    kundenanfragen = input_aufnahme()
    max_belegt, max_beleg_km = belegung(kundenanfragen)    
    print(f"Die Maximale Belegung ({max_belegt}) findet am {max_beleg_km} Kilommeter statt")

main()
    