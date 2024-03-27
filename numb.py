# "PERSEGI FC" football club jersey number
while True:
    jersey_number = int(input('Enter player\'s jersey number: '))

    # Check nomor punggung genap 
    if jersey_number % 3 == 0 or jersey_number % 5 == 0:
            print("player ini kiper")
    if jersey_number % 2 == 0:
        if jersey_number >= 50 and jersey_number <= 100:
            print("player memenuhi syarat menjadi kapten")
        else:
            print("player ini penyerang")
    
    else:
        if jersey_number % 2 != 0 and jersey_number > 90:
            print("player ini pemain tengah")
        else:
            print("player ini pemain bertahan")