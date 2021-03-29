# Kullanıcıdan integer türünde bir değer isteyiniz. İstemiş olduğunuz bu değerin çarpım tablosu
# değerlerini gösteren kodu for döngüsü ile gerçekleştiriniz

def multiplicationTable(num):
    for i in range(10):
        print(f'{i} x {num} == {i*num}')



#  Girilen bir sayının kaç basamaklı olduğunu belirleyen programı while döngüsü ile gerçekleştiriniz

def howManyDigits(num):
    return f'{num} number has {len(list(string(num)))} digits'

#alternative with while
def howManyDigits2(num):
    count=0
    while(num > 0):
        count+= 1
        num//= 10
    return f'Number has {count} digits'



# Aşağıda bir listeye ait sayısal değerler verilmiştir. 
# sayısalDeğerler = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# Bu listedeki 5’e bölünen sayıları çıktı olarak veren programı hem for hem de while döngüsü ile 
# gerçekleştiriniz. 150’den büyük değerleri dikkate almayınız

def dividableToFive(list_of_numbers):
    for num in list_of_numbers:
        if(num <= 150 and num%5 == 0):
            print(num)



# Kullanıcıdan 3 adet (a, b ve c) değer alınız. a (dahil) ve b (dahil) arasında kaç sayının c’ye 
# bölünebildiğini belirleyen programı yazınız

def findingDividableNumbers(first, second, third):
    counter = 0
    for num in range(first,second+1):
        if(third % num == 0):
            print(f'number {num} can divide {third}')
            counter+=1
    return f'{counter} numbers can divide number {third}'



# Aşağıdaki çıktıyı veren programı yazınız.
# 1 – 99
# 2 – 98
# 3 – 97
# ..
# ..
# ..
# 98 – 2
# 99 – 1

def oneToNinetyNine():
    for i in range(1, 100):
        print(f' {i} - {100-i} ')



# Kullanıcıdan bir IP adresi isteyiniz. İstediğiniz bu IP adresinden sonraki 5 değeri çıktı olarak 
# veren programı yazınız
# Örnek: 192 168 255 252
# Çıktı: 192 168 255 253
#        192 168 255 254
#        192 168 255 255
#        192 169 0   0
#        192 169 0   1


def increaseIpAddress(ip_address):
    print(f' {ip_address} ')
    ip_address= ip_address.split('.')
    unit0 = int(ip_address[3])
    unit1 = int(ip_address[2])
    unit2 = int(ip_address[1])
    unit3 = int(ip_address[0])

    for i in range(1,6):
        unit0+=1
        if (unit0 == 256):
            unit0 = 0
            unit1+=1
            if(unit1 == 256):
                unit1 = 0
                unit2+=1
                if(unit2 == 256):
                    unit2 = 0
                    unit3+=1
                    if(unit3 == 256):
                        unit3= 0
        else:
            print(f' {unit3}.{unit2}.{unit1}.{unit0} ')
