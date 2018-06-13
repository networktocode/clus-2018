#!/usr/bin/env python

import yaml
from jinja2 import Environment, FileSystemLoader

if __name__ == "__main__":

    config_data = yaml.load(open('./configs.yml'))

    env = Environment(loader = FileSystemLoader('./templates'), trim_blocks=True,
                     lstrip_blocks=True)

    template = env.get_template('configs.j2')

    print(template.render(config_data))



