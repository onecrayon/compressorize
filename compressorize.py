#!/usr/bin/env python

import os, commands
import yaml

# Save the current working directory and the script's directory

# Look for the compressorize.yaml file in the scripts directory, or use whatever was passed as a commandline argument

# If compressorPath is specified and exists, use it; otherwise look for the compressor next to the script.
# Exit with error if we can't find the compressor

# Check to see if we have recipes, or if things are living at the root level; if at root, load it into a single array recipe

# Loop over recipes
# Loop over the files and construct the string of them
# Figure out the final file name
# Put together the command with type variable, etc.
# Run the command and echo any errors or status messages
# Touch the file to update the date?

# Everything's complete, let's exit!


# THIS STUFF WAS MY INITIAL ATTEMPT

f = open('config.yaml')
config = yaml.load(f)
f.close()

if not 'compressorPath' in config or not os.path.exists(config.compressorPath):
    raise ValueError(
        "YUI Compressor cannot be found at [%s]" % config.compressorPath
    )

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
