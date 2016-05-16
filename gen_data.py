def fuzzer_options():
    print "1 )Bit flipper"
    print "2 )Radamsa"
    print "3 )Peach"
    print "4 )add more support here"

    choice = raw_input("Enter your choice : ")
    if int(choice) == 1:
        biflipper.flipp()
