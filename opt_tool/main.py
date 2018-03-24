import argparse
import logging
import yaml

parser = argparse.ArgumentParser()
parser.add_argument('--config', dest='config', required=True, help='Path to config')
args = parser.parse_args()

log = logging.getLogger(__name__)


if __name__ == "__main__":
    with open(args.config, 'r') as config_file:
        cfg = yaml.load(config_file)
        print(cfg)