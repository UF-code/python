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
        count += 1
        num//= 10
    return f'Number has {count} digits'