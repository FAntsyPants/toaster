#We want to be able to program a toaster and its behaviors.
#The toaster needs to have its lever pushed all the way down until the buttons can be turned on
from time import sleep
leverDown = False

#these define the grill racks that cook the toast or bagel
left_rack = {
    "inner_grill" : False,
    "outer_grill" : False
}
right_rack = {
    "inner_grill" : False,
    "outer_grill" : False
}


#initial greeting function. this runs when the program starts
def greeting():
    a = input("Would you like to make some toast? Y/N")
    match a:
        case "y":
            #assigning the results of set_timer()
            timer = set_timer()
            #pass results of set_timer, as timer, to cook().
            cook(timer)
        case "n":
            pass
        case other:
            pass

def set_timer():
    #get from the user dial amount. Default is 0 for all the way down
    dial = 0
    toastyQ = input("How toasty would you like your toast? type '1' for 1 minute and up to '6' for 6 minutes!")
    dial = int(toastyQ)
    return dial

def lower_lever():
    leverDown = True

def cook(time, option):
    lower_lever()
    if option == "bagel":
        left_rack["inner grill"] = True
        right_rack["inner grill"] = True
    elif option == "frozen toast":
        time * 2
        for x in left_rack:
            left_rack[x] = True
        for x in right_rack:
            right_rack[x] = True
        for i in range(time):
            print("toasting...")
            sleep(2)
    elif option == "frozen bagel":
        time * 2
        for i in range(time):
            print("toasting...")
            sleep(2)
    else:
        pass
    for i in range(time):
        print("toasting...")
        sleep(2)
    print("*DING!*")