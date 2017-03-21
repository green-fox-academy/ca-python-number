import random

print("mukodik")

kedvenc_szamom = random.randrange(1, 10)
megtalaltam = False
lehetosegek = 3

while (not megtalaltam) and lehetosegek > 0:
    print("meg " + str(lehetosegek) + " lehetoseged van")
    print("mi a kedvenc szamom?")

    tippelt_szam = input()

    print("amit te tippeltel az " + str(tippelt_szam))

    szam_tipusu_tippelt_szam = int(tippelt_szam)

    megtalaltam = szam_tipusu_tippelt_szam == kedvenc_szamom

    # print("a megtalaltam erteke most " + str(megtalaltam))

    if megtalaltam:
        print("es tokre eltalaltad")
    else:
        print("es tokre nem talaltad el")

    lehetosegek -= 1

if (not megtalaltam) and lehetosegek == 0:
    print("elfogytak a lehetosegeid :(((")
