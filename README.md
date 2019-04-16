#pyq

A set of useful command line scripts to navigate through your files and directories with ease and to get informed quickly.

##Compatibility
Fully compatible with :

- **Windows** 7 and higher.
- **Linux** distributions running under the X Window System.

##Usage
Install the [PyPI package](https://pypi.python.org/pypi/pyq/):

    pip install pyq

or clone the repository:

    git clone https://github.com/Whenti/pyq

or [download and extract the zip](https://github.com/Whenti/pyq/archive/master.zip) into your project folder.

Then check the [commands doc below](https://github.com/Whenti/pyq#Commands) to see what commands are available.

##Dependencies
See the

##Authors
* **Quentin LÉVÊQUE** - [Whenti](https://github.com/Whenti)

## License
This project is proudly licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

#Commands
Below we briefly describe the different commands of `pyq`. Make sure to use the `--help` option for more details.


``v`` command.

##``f`` command

Open your favourite files with ease. See `f --help` for more details.

###Example

```
$ cd ~
$ # associate permanently the key 'bashrc' to the file '~/.bashrc'
$ f bashrc -a .bashrc
$ # call 'f' with the associated key as parameter to open the affiliated file
$ f bashrc
$ # if '~/.bashrc' is not one of your favourite files anymore
$ f bashrc -r
```

``d`` command.

##``i`` command

Open your favourite websites with ease. See `i --help` for more details.

###Example

```
$ # associate permanently the key 'github' to 'http://www.github.com'
$ i github -a http://www.github.com
$ # associate permanently the key 'so' to 'https://stackoverflow.com/'
$ i so -a https://stackoverflow.com/
$ # open the two websites on the existing webbrowser window
$ i github so
$ # open github and performs a google search for 'python' on a new webbrowser window
$ i -n github -g python
```

``c`` command.

``ant`` command.

``syn`` command.

``say`` command.

``def`` command.

``rand`` command.

``yget`` command.