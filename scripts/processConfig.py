#! /usr/bin/env python

# This is an example of using a pre-build script to process the merged config
# file, to generate a header (prebuild-demo/defs.h), which can be #included by
# other modules


import json
import os

def generateDefinitions(config):
    definitions = ''
    expose_definitions = '$exposeDef' in config.keys()
    for k, v in config.items():
        if isinstance(v, dict):
            definitions += generateDefinitions(v)
        elif expose_definitions and not k.startswith('$'):
            definitions += '\n#define %s %s' % (k.upper(), v)
    return definitions


with open(os.environ['YOTTA_MERGED_CONFIG_FILE'], 'r') as f:
    merged_config = json.load(f, encoding='utf-8')
    definitions = generateDefinitions(merged_config)
    if not os.path.exists('./expose-defs'):
        os.makedirs('./expose-defs')
    with open('./expose-defs/defs.h', 'w') as outf:
        outf.write(definitions)
