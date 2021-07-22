def dump_csv(dict, file):
        for i in dict:
            file.write(f'{i},{dict[i]}\n')


def read_csv(file):
    d_read = file.read().splitlines()
    data={}
    for i in d_read:
        key, value = i.split(',')
        data[key] =value
    return data


access = 't'
dump = dump_csv
loadfile = read_csv
