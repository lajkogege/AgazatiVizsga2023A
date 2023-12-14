import ertekel


import pogasz1

print("III/A, B: ")
csomag_lista=pogasz1.fajlbeolvasas()#vissza térési értéket hivom meg
#Az első csomag széllesége
print(f"\tA pogászok száma: {len(csomag_lista)}")

print(f"Az első csomag bszélessége: {csomag_lista[0].a}")
print("III/C: ")
atlag=pogasz1.pogyasz_atlag_suly(csomag_lista)
print(f"\tAz 51 cm-es pogyászok átlag sulya: {atlag} g")
print("III/D: ")
max_index=pogasz1.legmagasabb_pogyasz(csomag_lista)
print(f"\tA legmagasabb pogyász méretei: {csomag_lista[max_index].a}x{csomag_lista[max_index].a}")
