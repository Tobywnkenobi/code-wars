def abbrev_name(name):
    first_name, last_name = name.split()
    return f'{first_name[0.upper()]}.{last_name[0].upper()}'