# pylcurve
This is a python wrapper of lcurve written by Thomas Marsh


'lcurve' is for modelling of light curves.

Installation order: subs --> colly, binary --> roche --> lcurve  (details see https://github.com/trmrsh/cpp-lcurve)


The package of cpp-subs is based on pcre, pgplot, and slalib(C version)


# installation:

- install pre
- - $conda install -c anaconda pcre

if you install the pcre by using conda, then you should modified environment file of the include and lib


- set environment variables (e.g. write them into \~/.bashrc)
- - export TRM_SOFTWARE= the_prefix_directory 
- - export CPPFLAGS="-I$CONDA_PREFIX/include/ -I$TRM_SOFTWARE/local/include"
- - export LDFLAGS="-L$CONDA_PREFIX/lib -L$TRM_SOFTWARE/local/lib"
- - export CFLAGS="-I$CONDA_PREFIX/include/"

- install slalib (C version)
- - should ask Tom Marsh Warwick (T.R.Marsh@warwick.ac.uk) to get this package
- - $ tar -xcf sla.tar.gz
- - $ cd sla-1.0.5
- - $ autoreconf -f -i -s
- - $ ./configure --prefix=$CONDA_PREFIX
- - $ make install
- - $ make

The file called 'Lcurve' that is generated in this directory defines
aliases (csh-style) and prints a help message when sourced.

https://cygnus.astro.warwick.ac.uk/phsaap/software


- 1st, install subs (can be download from [cpp-subs](https://github.com/trmrsh/cpp-subs))
- - $ cd cpp-subs
- - $ autoreconf -f -i -s
- - $ ./configure --prefix=$TRM_SOFTWARE
- - $ make install
- - $ make

- 2nd, install colly (can be download from [cpp-colly](https://github.com/trmrsh/cpp-colly))
- - $ cd cpp-colly
- - $ autoreconf -f -i -s
- - $ ./configure --prefix=$TRM_SOFTWARE
- - $ make install
- - $ make

- 3rd, install binary (can be download from [cpp-binary](https://github.com/trmrsh/cpp-binary))
- - $ cd cpp-binary
- - $ autoreconf -f -i -s
- - $ ./configure --prefix=$TRM_SOFTWARE
- - $ make install
- - $ make

- 4th, install roche (can be download from [cpp-roche](https://github.com/trmrsh/cpp-roche))
- - $ cd cpp-roche
- - $ autoreconf -f -i -s
- - $ ./configure --prefix=$TRM_SOFTWARE
- - $ make install
- - $ make


- 5th install [pylcurve](https://github.com/lidihei/pylcurve)
- - $ python setup.py install


# uninstall:
- $ cd cpp-colly & make uninstall
- $ cd cpp-binary & make uninstall
- $ cd cpp-roche & make uninstall
- $ cd pylcurve/srcs/cpp-lcurve & make uninstall
- $ pip unistall pylcurve

