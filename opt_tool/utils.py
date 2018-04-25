import errno
import os


def make_directory(dir_name):
    try:
        os.makedirs(dir_name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def generate_entity():
    pass


def generate_packages(pkg_name, dir_name=''):
    if isinstance(pkg_name, list):
        for el in pkg_name:
            generate_packages(pkg_name[pkg_name.index(el)], dir_name)
    else:
        try:
            for pkg in pkg_name:
                _pkg = None
                if isinstance(pkg, dict):
                    _pkg, pkg = pkg, list(pkg.keys())[0]
                if pkg != 'entity':
                    dir_n = dir_name + '/' + str(pkg)
                    print(dir_n)
                    make_directory(dir_n)
                    generate_packages(pkg_name[pkg], dir_n)
                else:
                    generate_entity()
        except TypeError:
            pass


def generate_directories(config):
    for package in config.packages:
        _dir = str(config.output_dir) + str(package['name'])
        make_directory(_dir)
        for component in package['components']:
            generate_packages(component, _dir)
