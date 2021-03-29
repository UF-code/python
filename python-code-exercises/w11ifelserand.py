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



