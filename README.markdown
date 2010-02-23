Compressorize compresses your Javascript and CSS using YUI Compressor.

## Requirements

Compressorize requires PyYAML and YUICompressor.

## Installation

Run the following commands to install compressorize:

    easy_install pyyaml
    cd /WHERE/TO/INSTALL
    git clone PATH
    cd compressorize
    chmod +x compressorize.py

Download [YUICompressor](http://developer.yahoo.com/yui/compressor/) and install it in your `compressorize` directory.

## Usage

Compressorize is intended to be installed somewhere external to your web projects.  You can then create YAML configuration files within your individual projects that are tweaked to your particular project's requirements.  Use the included `example.yaml` file as a guide.

To run `compressorize`, simply `cd` to the directory where your `compressorize.yaml` file for the project lives and execute the following command:

    /PATH/TO/compressorize/compressorize.py

You can optionally pass in the location of your YAML config file as an argument (note that the name of the file doesn't need to be `compressorize.yaml` in this case):

    /PATH/TO/compressorize/compressorize.py /OTHER/PATH/TO/config.yaml

To make your life easier, you may want to consider adding the following to your `.bash_profile` file in your home folder:

    alias compressorize="PATH/TO/compressorize/compressorize.py"

If you do so, you will be able to execute the command `compressorize` rather than needing to specify the path to the Python file.

## Advanced topics

If you need, you can import compressorize as a Python module if the compressorize folder is in your Python path.  Usage:

    import compressorize
    
    # Optional; only call if no compressorize.yaml file
    # in current working directory
    compressorize.setConfig('/PATH/TO/compressorize.yaml')
    # You can alternatively bypass YAML and just pass in a Python object
    config = {
        files: ['mootools-core.js', 'mootools-more.js'],
        root: '../js/',
        compressorPath: '/PATH/TO/yuicompressor.jar'
    }
    compressorize.setConfig(config)
    
    # Runs the actual compressing routine
    output = compressorize.compress();
    if output != '':
        print("Compressorize error: " + output)
