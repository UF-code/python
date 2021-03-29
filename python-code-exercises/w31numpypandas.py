import pandas as pd 

# csv formatında bu tabloyu oluşturup lokalde bu tabloyu Pandas kütüphanesini kullanarak açınız
tennis_csv= pd.read_csv('w31tenis.csv')



# Pandas kütüphanesi aracılığıyla tablodan “Sıcaklık” ve “Nem” değerlerini siliniz
dropSicaklikNem = tennis_csv.drop(['Sicaklik', 'Nem'], axis=1)



#  Pandas kütüphanesinin metodu olan DataFrame() ile yukarıda verilen tabloyu oluşturunuz ve 
# tablo hakkında betimleyici istatiksel bilgiler veriniz
weatherForTennis= {
    'Hava Durumu': ['Gunesli', 'Gunesli', 'Kapali', 'Yagmurlu', 'Yagmurlu', 'Yagmurlu', 'Kapali', 'Gunesli', 'Gunesli', 'Yagmurlu', 'Gunesli', 'Kapali', 'Kapali', 'Yagmurlu'],
    'Sicaklik': ['Sicak', 'Sicak', 'Sicak', 'Iliman', 'Soguk', 'Soguk', 'Soguk', 'Iliman', 'Soguk','Iliman', 'Iliman', 'Iliman', 'Sicak', 'Iliman'],
    'Nem': ['Yüksek', 'Yüksek', 'Yüksek', 'Yüksek', 'Normal', 'Normal', 'Normal', 'Yüksek', 'Normal', 'Normal', 'Normal', 'Yüksek', 'Normal', 'Yüksek'],
    'Yagis': ['Seyrek', 'Asiri', 'Seyrek', 'Seyrek', 'Seyrek', 'Asiri', 'Asiri', 'Seyrek', 'Seyrek', 'Seyrek', 'Asiri', 'Asiri', 'Seyrek', 'Asiri'],
    'Oyun': ['Yok', 'Yok', 'Var', 'Var', 'Var', 'Yok', 'Var', 'Var', 'Yok', 'Var', 'Var', 'Yok', 'Var', 'Yok']
}

weatherForTennisDataFramed = pd.DataFrame(weatherForTennis, columns= ['Hava Durumu', 'Sicaklik', 'Nem', 'Yagis', 'Oyun'], index=['Gun1', 'Gun2', 'Gun3', 'Gun4', 'Gun5', 'Gun6', 'Gun7', 'Gun8', 'Gun9', 'Gun10', 'Gun11', 'Gun12', 'Gun13', 'Gun14'])

described = weatherForTennisDataFramed.describe()
weatherForTennisDataFramed.info()



import numpy as np 

# (3,4) boyutunda bir dizi oluşturunuz. Oluşturduğunuz bu dizinin boyutunu (6,2) olacak şekilde değiştiriniz 
threeToFour = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])

sixToTwo= np.resize(threeToFour, (6,2))


#  İki tane (3,3) boyutunda rastgele sayılardan meydana bir dizi oluşturunuz. Oluşturulan bu diziyi 
# hem yatay hem de dikey olacak şekilde istif (stack) ediniz
first_random_array = np.random.rand(3,3)
second_random_array = np.random.rand(3,3)

# vertical stack
vertical_stack = np.vstack((first_random_array, second_random_array))

# horizantal stack
horizantal_stack = np.hstack((first_random_array, second_random_array))