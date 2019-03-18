# Write your code here
import re
def hide_email_addresses(string):
    def replace(email):
        return '*' * len(email.group(0))
    return re.sub(r'[a-zA-Z0-9.]+@[a-zA-Z0-9.]+', replace, string)