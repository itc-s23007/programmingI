name_age = {'tanaka': 35, 'satou': 25, 'suzuki':27}

def dict_info(dict_tbl, key):
    try:
        return dicttbl[key]
    except:
        return 'key is bot found'

print(dict_info(name_age, 'satou'))
print(dict_info(name_age, 'yamada'))
