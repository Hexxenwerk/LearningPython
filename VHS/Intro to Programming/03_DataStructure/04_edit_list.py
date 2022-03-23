teilnehmer_liste = sorted(["Thomas", "Ingo", "Sara", "Lena", "Julia", "Sven", "Frank"])
print(teilnehmer_liste)

# Add items to end of list
teilnehmer_liste.append("Florian")
print(teilnehmer_liste)

teilnehmer_liste.insert(1, "Maria")
print(teilnehmer_liste)

# Edit items
teilnehmer_liste[2] = "Ines"
print(teilnehmer_liste)

# Delete items
teilnehmer_liste.pop()  # deletes last item
print(teilnehmer_liste)

teilnehmer_liste.pop(3)  # delete a specific index
print(teilnehmer_liste)

teilnehmer_liste.remove("Thomas")
print(teilnehmer_liste)  # delete value (first match only)

del teilnehmer_liste[4]  # delete s specific index
print(teilnehmer_liste)

del teilnehmer_liste[1:4]  # delete range of items
print(teilnehmer_liste)
