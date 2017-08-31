response = 'Y'

answer = "Left"
if answer == "Left":
    print "This is the Verbal Abuse Room, you heap of parrot droppings!"

# Will the above print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.

def using_control_once():
    if 2 < 3:
        return "Success #1"

def using_control_again():
    if 2 +2 != 4:
        return "Success #2"
    else:
        return "No Success #2"

print using_control_once()
print using_control_again()

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0

print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)
