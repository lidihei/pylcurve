# pylcurve
This a python wrapper for lcurve written by Thomas Marsh


'lcurve' is for modelling of light curves.

Installation order: subs --> colly, binary --> roche --> lcurve  (https://github.com/trmrsh/cpp-lcurve)

The file called 'Lcurve' that is generated in this directory defines
aliases (csh-style) and prints a help message when sourced.

https://cygnus.astro.warwick.ac.uk/phsaap/software

installation:
- set environment variables (e.g. write them into ~/.bashrc)
export TRM_SOFTWARE="~/anaconda3/include"
export CPPFLAGS="-I~/anaconda3/include"
export CFLAGS="-I~/anaconda3/include"
export LDFLAGS="-L/home/lijiao/anaconda3/lib"

- install subs

- install colly
$ cd srcs/cpp-colly & ./bootstrap

- install binary
$ cd srcs/cpp-binary & ./bootstrap

- install roche
$ cd srcs/cpp-roche & ./bootstrap


- install pylcurve
$ python setup.py install


uninstall:
- cd srcs/cpp-colly & make uninstall
- cd srcs/cpp-binary & make uninstall
- cd srcs/cpp-roche & make uninstall
- cd srcs/cpp-lcurve & make uninstall
- pip unistall pylcurve

