# pylcurve
This is a python wrapper of lcurve and is written by Jiao Li (lijiao@bao.ac.cn). 
The [lcurve](https://github.com/trmrsh/cpp-lcurve) is for modelling of light curves which is written by Thomas Marsh.

- major modification: 
- - trm/lcurve.h add Pparam(double value, double range, double dstep, bool vary, bool defined) and 
    Constructor from arguments added by lijiao
    Model(//Binary and stars
           double q_value, double q_range, double q_dstep, bool q_vary, bool q_defined,... 
- - src/Makefile.am add lib_LTLIBRARIES = libpylcurve.la ...
- - src/trm_lcurve.cc  add Lcurve::Model::Model(//Binary and stars...
- - add libpylcurve.cc and pylight_curve_comp.cc

'lcurve' is for modelling of light curves.

Installation order: subs --> colly, binary --> roche --> lcurve  (details see https://github.com/trmrsh/cpp-lcurve)


The package of cpp-subs is based on pcre, pgplot, and slalib(C version)


# installation:

- install pre
- - $conda install -c anaconda pcre

- install pgplot
- - $conda install -c conda-forge pgplot
- - $conda install -c "conda-forge/label/gcc7" pgplot

if you install the pcre by using conda, then you should modified environment file of the include and lib


- set environment variables (e.g. write them into \~/.bashrc)
- - export TRM_SOFTWARE= the_prefix_directory 
- - export CPPFLAGS="-I$CONDA_PREFIX/include/ -I$CONDA_PREFIX/include/pgplot/ -I$TRM_SOFTWARE/include"
- - export LDFLAGS="-L/usr/lib/ -L$CONDA_PREFIX/lib -L$TRM_SOFTWARE/lib"
- - export CFLAGS="-I$CONDA_PREFIX/include/"

- install slalib (C version)
- - should ask Tom Marsh Warwick (T.R.Marsh@warwick.ac.uk) to get this package
- - $ tar -xcf sla.tar.gz
- - $ cd sla-1.0.5
- - $ autoreconf -f -i -s
- - $ ./configure --prefix=$CONDA_PREFIX
- - $ make
- - $ make install

The file called 'Lcurve' that is generated in this directory defines
aliases (csh-style) and prints a help message when sourced.

https://cygnus.astro.warwick.ac.uk/phsaap/software


- 1st, install subs (can be download from [cpp-subs](https://github.com/trmrsh/cpp-subs))
- - $ cd cpp-subs
- - $ autoreconf -f -i -s
- - $ ./configure --prefix=$TRM_SOFTWARE
- - $ make
- - $ make install

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
- - $ make
- - $ make install

- 4th, install roche (can be download from [cpp-roche](https://github.com/trmrsh/cpp-roche))
- - $ cd cpp-roche
- - $ autoreconf -f -i -s
- - $ ./configure --prefix=$TRM_SOFTWARE
- - $ make
- - $ make install


- 5th install [pylcurve](https://github.com/lidihei/pylcurve)
- - $ python setup.py install


# uninstall:
- $ cd cpp-subs & make uninstall
- $ cd cpp-colly & make uninstall
- $ cd cpp-binary & make uninstall
- $ cd cpp-roche & make uninstall
- $ cd pylcurve/srcs/cpp-lcurve & make uninstall
- $ pip unistall pylcurve

