import re
def is_valid_password(string):
    validshit = [
        r'.{8,}',
        r'[0-9]',
        r'[a-z]',
        r'[A-Z]',
        r'[-+/.*@]'
    ]
    invalidshit = [
        r'(.)\1{2}',
        r'(.)(.*\1){3}'
    ]

    return all(re.search(eis,string)for eis in validshit) and not any(re.search(verboden,string) for verboden in invalidshit)