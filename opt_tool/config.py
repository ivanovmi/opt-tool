import yaml


class Config(object):
    def __init__(self, cfg):
        with open(cfg, 'r') as config_file:
            conf = yaml.load(config_file)
            self.output_dir = conf['output_dir'] + '/'
            self.packages = conf['packages']
