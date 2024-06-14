# pylcurve
This is a python wrapper of lcurve and is written by Jiao Li (lijiao@bao.ac.cn). 
The [lcurve](https://github.com/trmrsh/cpp-lcurve) is for modelling of light curves which is written by Thomas Marsh.
In order to use the share libary for pyclurve, a [modified lcurve version](https://github.com/lidihei/cpp-lcurve) is written. 

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

- If you are using macOS, autoconf, automake, libtool, pcre, and llvm can be installed by brew
- - brew install autoconf automake libtool pcre llvm
- - - note: glibtoolize is in libtool; [install brew](https://brew.sh)

- - PGPLOT can be installed by using [mesasdk](http://user.astro.wisc.edu/~townsend/static.php?ref=mesasdk#Prerequisites). This is the easiest way for me to install PGPLOT

- install the pacakages by conda, e.g.
- - $conda install -c anaconda pcre

if you install the packages by using conda, then you should modify environment file of the include and lib:

- set environment variables (e.g. write them into \~/.bashrc, or \~/.zshrc)
- - export TRM_SOFTWARE= the_prefix_directory (e.g. "/Users/pcname/TRM_SOFTWARE/local") 
- - export CPPFLAGS="-I$CONDA_PREFIX/include -I$TRM_SOFTWARE/include"
- - export LDFLAGS="-L$CONDA_PREFIX/lib -L$TRM_SOFTWARE/lib"
- - export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$LD_LIBRARY_PATH

if the dependence packages are installed by brew or the other methods (for MacOS-Silicon):
- - export PGPLOT_DIR="/Applications/mesasdk/lib/pgplot"
- - export PGPLOT_FONT="$PGPLOT_DIR/grfont.dat
- - export TRM_SOFTWARE= the_prefix_directory
- - export CPPFLAGS="-I/usr/local/include -I$TRM_SOFTWARE/include -I/opt/homebrew/include -I$PGPLOT_DIR -I$PGPLOT_DIR"
- - export LDFLAGS="-L/opt/homebrew/lib -L$TRM_SOFTWARE/lib -L$PGPLOT_DIR"
- - export LD_LIBRARY_PATH=$PGPLOT_DIR:$CONDA_PREFIX/lib:/opt/homebrew/lib:$LD_LIBRARY_PATH


- install slalib (C version)
- - should ask Tom Marsh Warwick (T.R.Marsh@warwick.ac.uk) to get this package
- - $ tar -xcf sla.tar.gz
- - $ cd sla-1.0.5
- - $ autoreconf -f -i -s
- - $ ./configure --prefix=$TRM_SOFTWARE
- - $ make install
- - $ make clean

The file called 'Lcurve' that is generated in this directory defines
aliases (csh-style) and prints a help message when sourced.

https://cygnus.astro.warwick.ac.uk/phsaap/software


- 1st, install subs (can be download from [cpp-subs](https://github.com/trmrsh/cpp-subs))
- - $ cd cpp-subs
- - $ autoreconf -f -i -s
- - $ ./configure --prefix=$TRM_SOFTWARE
- - $ make install
- - $ make clean

- 2nd, install colly (can be download from [cpp-colly](https://github.com/trmrsh/cpp-colly))
- - $ cd cpp-colly
- - $ autoreconf -f -i -s
- - $ ./configure --prefix=$TRM_SOFTWARE
- - $ make install

- 3rd, install binary (can be download from [cpp-binary](https://github.com/trmrsh/cpp-binary))
- - $ cd cpp-binary
- - $ autoreconf -f -i -s
- - $ ./configure --prefix=$TRM_SOFTWARE
- - $ make install
- - $ make clean

- 4th, install roche (can be download from [cpp-roche](https://github.com/trmrsh/cpp-roche))
- - $ cd cpp-roche
- - $ autoreconf -f -i -s
- - $ ./configure --prefix=$TRM_SOFTWARE
- - $ make install
- - $ make clean


- 5th install [pylcurve](https://github.com/lidihei/pylcurve) (Note: pylcurve needs a modified cpp-lcurve version. 
If you want to install cpp-lcurve without "python setup.py install", you should dowload it from https://github.com/lidihei/cpp-lcurve and install it by using "./pyinstall" )
- - $ cd pyclurve
- - $ python setup.py install

if you want to use the commands such as lroch, levmarq, lroches, you can write alias into the default configuration file (\~/.bashrc or \~/.zshrc)
- For example:
- - alias lroche="$TRM_SOFTWARE/bin/lcurve/lroche"

# uninstall:
- $ cd cpp-subs & make uninstall
- $ cd cpp-colly & make uninstall
- $ cd cpp-binary & make uninstall
- $ cd cpp-roche & make uninstall
- $ cd pylcurve/srcs/cpp-lcurve & make uninstall
- $ pip unistall pylcurve

