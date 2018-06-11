a = "without,hello,bag,world"              

b = a.split(',')                 # Conversion of string to list

print (b)                        # printing out b for reference

b.sort()                         # Sorting out b in sequence (Note: sorting changes value forever)

print (b)                        # for reference

d = (','.join(b))                # Joining the list by comma to convert it into string

print (d)                        # print d

# CODED BY - GAURAV PADAWE