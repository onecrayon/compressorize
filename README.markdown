Compressorize compresses your Javascript and CSS using YUI Compressor.

## Requirements

Compressorize requires PyYAML and YUICompressor.

## Installation

1. Run the following commands to install compressorize (customizing your
   install path appropriately):
   
        easy_install pyyaml
        cd /WHERE/TO/INSTALL
        git clone git://github.com/onecrayon/compressorize.git
        cd compressorize
        chmod +x compressorize.py

2. Download [YUICompressor](http://developer.yahoo.com/yui/compressor/) and
   install it in your "compressorize" directory.

## Usage

Compressorize is intended to be installed somewhere external to your web
projects.  You can then create YAML configuration files within your
individual projects that are tweaked to your particular project's
requirements.  Use the included `example.yaml` file as a guide.

To run compressorize, simply `cd` to the directory where your
`compressorize.yaml` file for the project lives and execute the
following command:

    /PATH/TO/compressorize/compressorize.py

You can optionally pass in the location of your YAML config file as an
argument (note that the name of the file doesn't need to be
`compressorize.yaml` in this case):

    /PATH/TO/compressorize/compressorize.py /OTHER/PATH/TO/config.yaml

### Bash or other shell alias

To make your life easier, you may want to consider adding the following
to your `.bash_profile` file in your home folder:

    alias compressorize="PATH/TO/compressorize/compressorize.py"

If you do so, you will be able to execute the command `compressorize`
rather than needing to specify the path to the Python file.

## Advanced usage

If you need, you can import compressorize as a Python module if the
compressorize folder is in your Python path.  Usage:

    import compressorize
    
    # You can bypass YAML by passing a Python object to set_config
    config = {
        files: ['mootools-core.js', 'mootools-more.js'],
        root: '../js/',
        compressorPath: '/PATH/TO/yuicompressor.jar'
        # base_dir is a required element that tells the script where to
        # base the relative root element
        # Normally base_dir is automatically set to the YAML file's directory
        base_dir: '/PATH/TO/PROJECT'
    }
    output = compressorize.compress(config)
    
    # Or you can pass in a string to the YAML file
    output = compressorize.compress('/PATH/TO/compressorize.yaml');
    
    # Outputs None or an array of error messages
    if output is not None:
        for msg in output:
            print(msg)

## License

Copyright (c) 2010 Ian Beck

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.