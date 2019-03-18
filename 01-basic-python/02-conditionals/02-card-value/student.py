# Write your code here
def card_value(string):
    if string == 'Jack':
        return 11
    if string == 'Queen':
        return 12
    if string == 'King':
        return 13
    if string == 'Ace':
        return 1
    if int(string) >= 2 and int(string) <= 10:
        return int(string)
            