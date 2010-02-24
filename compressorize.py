#!/usr/bin/env python

'''
# compressorize.py

Provides the main guts of the compressorize package.

If using config files, PyYAML is required.

## Methods

* [setconfig](#setconfig)
* [compress](#compress)
'''

import os
import commands
import sys
import glob

def setconfig(path_or_object=None):
    '''
    ### setconfig    {#setconfig}
    
    Handles setting up the config object, usually from a YAML file.
    
    _path_or_object_ (str or dict)
    :    Optional; if a string is passed in, it will be used as a path
         to a YAML file. If a dict is passed it, it will be used as
         the config object. If None will default to `"current working
         directory"/compressorize.yaml`
    
    **Returns void**
    '''
    config = None
    # Make sure to handle empty strings passed in as the path
    if path_or_object == '':
        path_or_object = None
    if path_or_object is None or isinstance(path_or_object, basestring):
        # Importing here means it won't break a second Python project
        # that isn't using YAML config files
        import yaml
        
        working_dir = os.getcwd()
        path = path_or_object if path_or_object is not None else \
               os.path.join(working_dir, "compressorize.yaml")
        if not os.path.exists(path):
            raise ValueError("Cannot find YAML config file at `%s`" % path)
            return
        f = open(path)
        config = yaml.load(f)
        f.close()
        # Setup the path to the file to reference later
        path = os.path.dirname(path)
    elif isinstance(path_or_object, dict):
        config = path_or_object
        path = os.getcwd()
    
    # Set up the base directory if not already configured
    if 'base_dir' not in config:
        config['base_dir'] = path
    
    return config

def compress(path_or_object=None):
    '''
    ### compress    {#compress}
    
    Executes the actual compression and combination of the files.
    
    _path_or_object_ (str or dict)
    :    Optional; only necessary if not explicitly using
         [setconfig](#setconfig). Identical to its argument.
    
    **Returns array of strings or None if no messages**
    '''
    config = setconfig(path_or_object)
    
    # Look for the compressor binary
    if "compressorPath" in config:
        compressor = config['compressorPath']
    else:
        self_dir = os.path.dirname(__file__)
        possible_paths = glob.glob(
            os.path.join(self_dir, 'yuicompressor*.jar')
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
    if 'recipes' in config:
        recipes = config['recipes']
    else:
        # No recipe, so items must be in root
        # Since we'll test for keys later, just toss the whole config in
        recipes = [config]
    
    # Process the recipes
    messages = []
    for index, recipe in enumerate(recipes):
        # Check for the required fields
        if 'files' not in recipe:
            raise ValueError("Error: required files array not found")
            return
        root = recipe['root'] if 'root' in recipe else ''
        if root != '' and not os.path.isabs(root):
            # Relative path, so construct relative to script directory
            root = os.path.join(config['base_dir'], root)
            root = os.path.normpath(root)
        # Grab the type based on the first file's extension
        ext_start = recipe['files'][0].rfind('.')
        if ext_start == -1:
            # Couldn't find an extension, so default to JS
            type = 'js'
        else:
            type = recipe['files'][0][ext_start+1:].lower()
        # Setup the output name, or default to "compressed"
        output = recipe['output'] if 'output' in recipe else \
                 'compressed.' + type
        output = os.path.join(root, output)
        # Construct the string of file names
        files = ''
        for file in recipe['files']:
            files += os.path.join(root, file) + ' '
        
        command = 'cat ' + files + '| java -jar ' + compressor + \
                  ' --type ' + type + ' -o ' + output
        status, message = commands.getstatusoutput(command)
        if status > 0:
            messages.append(message)
        # Touch the file to update the date?
    
    # Everything's complete, let's exit!
    if len(messages) > 0:
        return messages
    else:
        return None


if __name__ == "__main__":
    if len(sys.argv) > 1:
        args = sys.argv[1]
    else:
        args = ''
    output = compress(args)
    if output is not None:
        for msg in output:
            print(msg)
