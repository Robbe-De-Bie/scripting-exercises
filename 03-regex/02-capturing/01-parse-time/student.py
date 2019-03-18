import re


def parse_time(string):
    eis = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(?:\.(\d{3}))?', string)

    if eis:
        return tuple( [ int(x) for x in eis.groups('000') ] )
    else:
        return None
