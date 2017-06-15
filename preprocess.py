# coding=utf-8

def get_name_list(en=False):
    if en:
        f = open('data/name')
        content = f.readlines()
        name_list = []
        for line in content:
            name_list.append(line.decode('utf-8').strip())
        return name_list

    f = open('data/人物名')
    content = f.readlines()
    name_list = []
    for line in content:
        name_list.append(line.decode('utf-8').split(u'--')[2].strip())
    return name_list

if __name__ == '__main__':
    names = get_name_list()
    print '\n'.join(names)
    print names.__len__()