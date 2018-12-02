# Kvadrifibrilne Grudvice - Projektni zadatak.

Odgovor na teorijska pitanja nalazi se u Teorija.txt.
Bonus zadatak nalazi se u direktorijumu bonus, a opis bonus zadatka i odgovor na 4. teorijsko pitanje nalazi se u Bonus.txt


# Opis zadatka

Dodali smo trazene endpointe za dovlacenje izmenu i brisanje clana. 

* GET /members/<member_id>

* PUT /members/<member_id>

* DELETE /members/<member_id>

Takodje smo dodali frontend funkcionalnost za ove metode. U listi timova moze se otvoriti forma za izmenu tima i izmenu pojedinacnog clana svakog tima.

U backendu i frontendu smo onemogucili dodavanje tima sa manje od tri a vise od pet clanova.
Takodje smo onemogucili brisanje clanova u timovima koji imaju samo tri clana.
Na frontend dodali smo navigacioni bar na sve stranice aplikacije i napravili druge kozmeticke promene.