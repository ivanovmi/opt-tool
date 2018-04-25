import argparse
import logging

import config
import utils

parser = argparse.ArgumentParser()
parser.add_argument('--config', dest='config', required=True,
                    help='Path to config')
args = parser.parse_args()

log = logging.getLogger(__name__)


if __name__ == "__main__":
    cfg = config.Config(args.config)
    utils.generate_directories(cfg)
