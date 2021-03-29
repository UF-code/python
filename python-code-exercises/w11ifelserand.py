#  Kullanıcıdan 3 adet integer türünde değer alınız. Almış olduğunuz bu değerler bir üçgenin 
# açılarını ifade edecektir. Bu açı değerlerine göre bu üçgenin dik, geniş ya da dar üçgen olup 
# olmadığını belirleyen programı yazınız

def isTriangle(first_angle, second_angle, third_angle):
    if( 0< first_angle <180 
    and 0< second_angle <180 
    and 0< third_angle <180 
    and (first_angle + second_angle + third_angle) == 180):
        
        if(first_angle == 90 or second_angle == 90 or third_angle == 90):
            return 'right triangle'
        elif(first_angle > 90 or second_angle > 90 or third_angle > 90):
            return 'obtuse triangle'
        elif(first_angle == 60 and second_angle == 60):
            return 'equilateral triangle'
        else:
            return 'acute triangle'
    else:
        return 'not a triangle'



# içinde uzaylı olan bir oyun geliştirdiğinizi düşünün. uzaylı_rengi isminde bir değişken oluşturun 
# ve bu değişken string türünde değerler alsın. Bu değişkene kırmızı, yeşil ya da sarı 
# değerlerinden birini klavyeden veriniz. Eğer uzaylının rengi yeşilse “Tebrikler, yeşil uzaylıya ateş 
# ettiğiniz için 5 puan kazandınız” şeklinde bir çıktı veriniz. Eğer rengi yeşil değilse "Tebrikler, yeşil 
# olmayan uzaylıya ateş ettiğiniz için 10 puan kazandınız" şeklinde çıktı veriniz. Senaryoya ait 
# programı yazınız

from random import choice

def alienColor(alien_color):
    color= ['red', 'green', 'yellow']

    if(alien_color == choice(color)):
        return f'Congrats, You hit the right one! - {alien_color} '
    elif(alien_color in color):
        return f'You shoot the other alien - {alien_color}'
    else:
        return 'Invalid Credentials'

