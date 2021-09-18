

# pyqo
A set of useful command line scripts to navigate through your files, directories and favourite websites with ease.

## Compatibility
Fully compatible with :

- **Windows** 7 and higher.
- **Linux** distributions running under the X Window System.

Requires `Python 3.0` or higher.

## Usage
Clone the repository:
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

Generic command: see ``pyqo --help``.


## Command ``d``

Open the file manager to your favourite directories with ease.

### Example

```
$ cd ~/Documents/games
$ # open the current working directory, here '~/Documents/games'
$ d
$ # associate permanently the key 'films' to '~/Documents/films'
$ pyqo d add films /home/pyqo/Documents/films
$ # open '~/Documents/films'
$ d films
```

## Command ``f``

Open your favourite files with ease.

### Example

```
$ cd ~
$ # associate permanently the key 'bashrc' to the file '~/.bashrc'
$ pyqo f add bashrc .bashrc
$ cd ~/Documents/games
$ # open the '~/.bashrc' file
$ f bashrc
```

## Command ``i``

Open your favourite websites with ease.

### Example

```
$ # associate permanently the key 'github' to 'http://www.github.com'
$ pyqo i add github http://www.github.com
$ # associate permanently the key 'so' to 'https://stackoverflow.com/'
$ pyqo i add so https://stackoverflow.com/
$ # open the two websites with your web browser
$ i github so
```

## Command ``v``
Associative table to save small variables.
### Example
```
$ # save the value '+44 1234 123456' under the key 'john_number'
$ pyqo v add john_number '+44 1234 123456'
$ # print John's number
$ v john_number
$ # forget John's number
$ pyqo v remove john_number
```
