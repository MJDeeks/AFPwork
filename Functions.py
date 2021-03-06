def main():
    print('hello')
    print('this program has 3 converters')
    print('--------------------------------')
    menu()

def menu():
    choice = '0'
    while choice == '0':
        print('1:fahrenheit to celcius')
        print('2:cm to mm')
        print('3:kilometres to metres')
        print('4:to quit')
        choice = input('please make a choice')
        if choice == '4':
            print('quitting...')
            print('-----------------------------')
            break
        #kilometres to metres
        elif choice == '3':
            kilo = int(input('enter a number of kilometres'))
            metr = (kilo*1000)
            print('{0} kilometres = {1:.1f} metres'.format(kilo, metr))
            print('-----------------------------')
            menu()
        #centimetres to milimetres
        elif choice == '2':
            cent = int(input('enter a measurement in centimetres'))
            mili = (cent*10)
            print('{0} centimetres = {1:.1f} milimetres'.format(cent, mili))
            print('-----------------------------')
            menu()
        #fahrenheit to celcius
        elif choice == '1':
            val = int(input('enter a temperature'))
            cel = ftoc(val)
            print('{0} fahrenheit = {1:.1f} celcius'.format(val, cel))
            print('-----------------------------')
            menu()
        else:
            print('I do not understand')
            print('-----------------------------')
            menu()

#create function to convert farenheit to celcius
def ftoc(fah):
    cel = (fah-32) *5/9
    return cel

main()
