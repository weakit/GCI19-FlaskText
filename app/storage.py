import shelve

data = None


def open_shelf():
    global data
    data = shelve.open('data.shelf')


def close_shelf():
    data.close()


def available(name):
    open_shelf()
    name = name.replace(' ', '_').lower()
    result = name not in data
    close_shelf()
    return result


def save(name, text):
    open_shelf()
    fname = name.replace(' ', '_').lower()
    data[fname] = text, name
    close_shelf()


def read(name):
    open_shelf()
    name = name.replace(' ', '_').lower()
    text, rname = data[name]
    close_shelf()
    return text, rname


def url_name(name):
    open_shelf()
    uname = data[name.replace(' ', '_').lower()][1]
    close_shelf()
    return uname.replace(' ', '_')


def list_texts():
    open_shelf()
    x = list(data.keys())
    close_shelf()
    return x


def delete(name):
    open_shelf()
    name = name.replace(' ', '_').lower()
    del data[name]
    close_shelf()
