# Kullanıcıdan integer türünde bir değer isteyiniz. İstemiş olduğunuz bu değerin çarpım tablosu
# değerlerini gösteren kodu for döngüsü ile gerçekleştiriniz

def multiplicationTable(num):
    for i in range(10):
        print(f'{i} x {num} == {i*num}')



#  Girilen bir sayının kaç basamaklı olduğunu belirleyen programı while döngüsü ile gerçekleştiriniz

def howManyDigits(num):
    return f'{num} number has {len(list(num))} digits'

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
        if(num <= 150 and n%5 == 0):
            print(n)

