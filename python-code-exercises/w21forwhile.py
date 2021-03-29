# Kullanıcıdan integer türünde bir değer isteyiniz. İstemiş olduğunuz bu değerin çarpım tablosu
# değerlerini gösteren kodu for döngüsü ile gerçekleştiriniz

def multiplicationTable(num):
    for i in range(10):
        print(f'{i} x {num} == {i*num}')

