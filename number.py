print("mukodik")

kedvenc_szamom = 26

megtalaltam = False

while not megtalaltam:
    print("mi a kedvenc szamom?")

    tippelt_szam = input()

    print("a kedvenc szamom " + str(kedvenc_szamom))

    print("amit te tippeltel az " + str(tippelt_szam))

    szam_tipusu_tippelt_szam = int(tippelt_szam)

    megtalaltam = szam_tipusu_tippelt_szam == kedvenc_szamom

    print("a megtalaltam erteke most " + str(megtalaltam))

    if megtalaltam:
        print("es tokre eltalaltad")
    else:
        print("es tokre nem talaltad el")
