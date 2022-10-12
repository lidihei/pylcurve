from setuptools import find_packages
#from distutils.core import setup, Extension
from setuptools import setup
import os
import numpy
import subprocess

from distutils.command.install import install

#### write a Makefile from Makefile_pyclurve######
lines = [f"CPPFLAGS = -I./cpp-lcurve/include {os.environ['CPPFLAGS']}\n"]
lines += [f"LDFLAGS = {os.environ['LDFLAGS']}\n"]

f = open('Makefile_pylcurve', 'r')
lines += f.readlines()
f.close()

f = open('Makefile', 'w')
f.writelines(lines)
f.close()

#### install class
class _install(install):
    def run(self):
        print('#-------------------------start make libpylcurve lib--------------')
        subprocess.call(['autoreconf', '-f', '-i', '-s'])
        subprocess.call(['make', 'clean', '-C', './'])
        subprocess.call(['make', '-C', './'])
        install.run(self)
        print('#-------------------------end make libpylcurve---------------\n\n\n')



#subprocess.call(['cp', './cpp-lcurve/src/.libs/*.so' './'])
#subprocess.call(['make', 'clean', '-C', './srcs/cpp-lcurve'])
#os.system('./srcs/cpp-lcurve/bootstrap')
#subprocess.call(['make', 'clean', '-C', './srcs/cpp-lcurve/src'])
subprocess.call(['make',  '-C', './srcs/cpp-lcurve/src'])
os.system('cp ./srcs/cpp-lcurve/src/.libs/*.so pylcurve/lib/')
subprocess.call(['make', 'clean', '-C', './srcs/cpp-lcurve'])

VERSION = '0.0.0' 
DESCRIPTION = 'python wrapper of lcurve'

fh = open('README.md', 'r')
LONG_DESCRIPTION = fh.read()
fh.close()


# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="pylcurve", 
        version=VERSION,
        author="Jiao Li",
        author_email="lijiao@bao.ac.cn",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        url ='https://github.com/lidihei/pylcurve',
        install_requires=['numpy', 'matplotlib', 'scipy',
                         ], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
 
        classifiers= [
            "Development Status :: beta",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3.8",
            "Topic :: Scientific/Engineering :: Physics",
            "Topic :: Scientific/Engineering :: Astronomy"
        ],
        #cmdclass={'install': _install},
        include_package_data=True,
        package_dir={
        #             'config': './config',
        #             'fits': './fits',
        #             'results': './results'
                    },
        package_data={'pylcurve': ['./lib/*.so'],
                      },
        ##headers=['csstpsf/Centroid/libCentroid/nrutil.h'],
        ##ext_modules=[ext],
)
