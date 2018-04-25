import errno
import os


def make_directory(dir_name):
    try:
        os.makedirs(dir_name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def generate_directories(config):
    for package in config.packages:
        print(package['name'])
        _dir = str(config.output_dir) + str(package['name'])
        make_directory(_dir)
        for component in package['components']:
            print(' ' * 2 + list(component.keys())[0])
            [make_directory(_dir+'/'+str(i)) for i in component.keys()]
