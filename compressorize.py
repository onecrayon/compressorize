#!/usr/bin/env python

'''
# compressorize.py

Provides the main guts of the compressorize package.

If using config files, PyYAML is required.

## Methods

* [set_config](#set_config)
* [compress](#compress)
'''

import os
import commands
import sys
import glob

# Save the current working directory and the script's directory
working_dir = os.getcwd()
script_dir = os.path.dirname(__file__)

# Global private config variable
_config = None

def set_config(path_or_object=None):
    '''
    ### set_config    {#set_config}
    
    Handles setting up the config object, usually from a YAML file.
    
    _path_or_object_ (str or dict)
    :    Optional; if a string is passed in, it will be used as a path
         to a YAML file. If a dict is passed it, it will be used as
         the config object. If None will default to `"current working
         directory"/compressorize.yaml`
    
    **Returns void**
    '''
    if path_or_object is None or isinstance(path_or_object, basestring):
        # Importing here means it won't break a second Python project
        # that isn't using YAML config files
        import yaml
        
        path = path_or_object if path_or_object is not None else \
               os.path.join(working_dir, "compressorize.yaml")
        if not os.path.exists(path):
            raise ValueError("Cannot find YAML config file at `%s`" % path)
            return
        f = open(path)
        _config = yaml.load(f)
        f.close()
    elif isinstance(path_or_object, dict):
        _config = path_or_object

def compress(path_or_object=None):
    '''
    ### compress    {#compress}
    
    Executes the actual compression and combination of the files.
    
    _path_or_object_ (str or dict)
    :    Optional; only necessary if not explicitly using
         [set_config](#set_config). Identical to its argument.
    
    **Returns array of strings or None if no messages**
    '''
    if _config is None:
        set_config(path_or_object)
    
    # Look for the compressor binary
    if "compressorPath" in _config:
        compressor = _config['compressorPath']
    else:
        possible_paths = glob.glob(
            os.path.join(working_dir, 'yuicompressor*.jar')
        )
        if len(possible_paths) == 0:
            compressor = ''
        else:
            # Names are typically yuicompressor-2.4.2.jar or similar
            # So if we sort alphabetically, the last element is most recent
            possible_paths.sort(reverse=True)
            compressor = possible_paths[0]
        if not os.path.exists(compressor):
            raise ValueError("Cannot find YUICompressor at `%s`" % compressor)
            return
    
    # Set up the recipes for later parsing
    if 'recipes' in _config:
        recipes = _config['recipes']
    else:
        # No recipe, so items must be in root
        # Since we'll test for keys later, just toss the whole config in
        recipes = [_config]
    
    # Process the recipes
    for index, recipe in enumerate(recipes):
        # Loop over the files and construct the string of them
        # Figure out the final file name
        # Put together the command with type variable, etc.
        # Run the command and echo any errors or status messages
        # Touch the file to update the date?
        pass
    # Everything's complete, let's exit!

# WHAT I HAD ORIGINALLY
'''
if not 'files' in config:
    raise ValueError("Required `files` array not present in config")

root = config.jsRoot if 'jsRoot' in config else ''
files = ''
for file in config.files:
    files += (root + file + ' ')

finalName = config.output if 'output' in config else 'compressed.js'
if 'jsRoot' in config:
    finalName = config.jsRoot + finalName

status, output = commands.getstatusoutput(
    'cat ' + files + '| java -jar ' + config.compressorPath + \
    ' --type js -o ' + finalName
)

if status > 0: 
    print output
'''

if __name__ == "__main__":
    ouput = compress(sys.argv[1])
    if output is not None:
        for msg in output:
            print(msg)
