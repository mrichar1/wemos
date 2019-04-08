from ujson import load

def Config(filename="config.json"):
    with open(filename) as conf_f:
        return load(conf_f)


