import errno
import os


def make_directory(dir_name):
    try:
        os.makedirs(dir_name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def create_empty_class(class_name):
    tab_sign = ' ' * 4
    new_class = "class {}(object):\n{}pass".format(class_name.title(), tab_sign)
    print('Empty class {}'.format(class_name))
    return new_class


def create_class_with_method(class_name):
    new_class = list()
    tab_sign = ' ' * 4
    new_class.append("class {}(object):".format(list(class_name.keys())[0].title()))
    for value in class_name.values():
        for func_name in value:
            new_class.append("{}def {}(self):\n{}{}pass".format(tab_sign,
                                                                func_name,
                                                                tab_sign,
                                                                tab_sign))
    print(new_class)

    return '\n\n'.join(new_class)


def generate_entity(pkg_name, dir_name):
    for entity in pkg_name:
        if isinstance(entity, dict):
            new_class = create_class_with_method(entity)
            entity_name = list(entity.keys())[0]
        else:
            new_class = create_empty_class(entity)
            entity_name = entity
        filename = dir_name + '/' + entity_name + '.py'
        with open(filename, 'w+') as f:
            f.write(new_class + '\n')


def generate_init(dir_name):
    filename = str(dir_name) + '/' + '__init__.py'
    with open(filename, 'w+'):
        print('Creating init file in package {}...'.format(dir_name))


def generate_packages(pkg_name, dir_name=''):
    if isinstance(pkg_name, list):
        for el in pkg_name:
            generate_packages(pkg_name[pkg_name.index(el)], dir_name)
    else:
        if pkg_name is not None:
            for pkg in pkg_name:
                _pkg = None
                if isinstance(pkg, dict):
                    _pkg, pkg = pkg, list(pkg.keys())[0]
                if pkg != 'entity':
                    dir_n = dir_name + '/' + str(pkg)
                    print(dir_n)
                    make_directory(dir_n)
                    generate_packages(pkg_name[pkg], dir_n)
                    generate_init(dir_n)
                else:
                    dir_n = dir_name
                    generate_entity(pkg_name[pkg], dir_n)


def generate_directories(config):
    for package in config.packages:
        _dir = str(config.output_dir) + str(package['name'])
        make_directory(_dir)
        for component in package['components']:
            generate_packages(component, _dir)
