

# pyqo
A set of useful command line scripts to navigate through your files, directories and favourite websites with ease.

## Compatibility
Fully compatible with :

- **Windows** 7 and higher.
- **Linux** distributions running under the X Window System.

Requires `Python 3.0` or higher.

## Usage
Install the [PyPI package](https://pypi.python.org/pypi/pyqo/):
```
$ pip install pyqo
```
and you're ready to go.
You can also clone the repository:
```
$ git clone https://github.com/Whenti/pyqo
```
or [download and extract the zip](https://github.com/Whenti/pyqo/archive/master.zip), and then run the setup:
```
$ python setup.py install
```

Check the [commands documentation below](https://github.com/Whenti/pyqo#Commands) to see what is available.

## Authors

* **Quentin LÉVÊQUE** - [Whenti](https://github.com/Whenti)

## License
This project is proudly licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

# Commands
Below we briefly describe the different commands of `pyqo`. Make sure to use the `--help` option for more details.


## Command ``pyqo``

Generic command to get help. Lists all the commands available.


## Command ``d``

Open the file manager to your favourite directories with ease.
The command ``c`` is also available to ``cd`` into the associated directory.
For a script to alter the current environment, it requires `source`'ing in linux.
We suggest you to create an alias to avoid doing it manually : `alias c="source c"`.

### Example

```
$ cd ~/Documents/games
$ # open the current working directory, here '~/Documents/games'
$ d
$ # associate permanently the key 'films' to '~/Documents/films'
$ d films -a /home/pyqo/Documents/films
$ # open '~/Documents/films'
$ d films
```

## Command ``f``

Open your favourite files with ease.

### Example

```
$ cd ~
$ # associate permanently the key 'bashrc' to the file '~/.bashrc'
$ f bashrc -a .bashrc
$ cd ~/Documents/games
$ # open the '~/.bashrc' file
$ f bashrc
```

## Command ``i``

Open your favourite websites with ease.

### Example

```
$ # associate permanently the key 'github' to 'http://www.github.com'
$ i github -a http://www.github.com
$ # associate permanently the key 'so' to 'https://stackoverflow.com/'
$ i so -a https://stackoverflow.com/
$ # open the two websites on the existing webbrowser window
$ i github so
```

## Command ``s``

Perform a web search with ease.

### Example

```
$ # associate permanently the key 'so' to a search on stackoverflow
$ s so -a https://stackoverflow.com/search?q={}
$ # perform a search on stackoverflow
$ s so "what is __init__.py for ?"
```

## Command ``v``
Associative table to save small variables.
### Example
```
$ # save the value '+44 1234 123456' under the key 'john_number'
$ v john_number -a '+44 1234 123456'
$ # print John's number
$ v john_number
$ # forget John's number
$ v john_number -d
```
