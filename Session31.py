def calculate_gen(year_parameter)  :

    gen = 'unknown'

    #add logic here to identify generation
    if year_parameter >= 1964 and year_parameter <=1978:
        gen = 'very OLD'
    if year_parameter >= 1979 and year_parameter <= 1995:
        gen = 'Y- Millenials'
    if year_parameter >= 1996 and year_parameter <= 2012:
        gen = 'Z'

    return gen
    # function return
    #print 'You belong to {} generation:'.format(gen)

name = raw_input("Please Enter Name:")
year = input ("What year were you born? Please enter YYYY : ")
print 'Your name : ' + name
print 'Your DOB : ' +str(year)

result = calculate_gen(year)
print 'You belong to {} generation:'.format(result)
