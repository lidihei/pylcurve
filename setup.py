from setuptools import find_packages
#from distutils.core import setup, Extension
from setuptools import setup
import os
import numpy
import subprocess
from distutils.command.install import install

dir_current = os.path.dirname(os.path.abspath(__file__))

#### write a Makefile from Makefile_pyclurve######
lines = [f"CPPFLAGS = -I./cpp-lcurve/include {os.environ['CPPFLAGS']}\n"]
lines += [f"LDFLAGS = {os.environ['LDFLAGS']}\n"]



#### install class
class _install(install):
    
    def install_cpp_code(self, dir_cppcode, dir_current=dir_current):
        ''' install the cpp code of lcurves e.g. cpp-lcurve'''
        print(f'change working directory to: {dir_cppcode} \n\n')
        dir_cppcode = os.path.join(dir_current, 'srcs',  dir_cppcode)
        os.chdir(dir_cppcode)
        print(f'------------------------start install {dir_cppcode} ------------------------')
        os.system('./bootstrap')
        subprocess.call(['make', 'clean', '-C', '.'])
        print(f'change working directory to: {dir_current} \n\n')
        os.chdir(dir_current)
        print(f'------------------------end install {dir_cppcode}---------------------------\n\n')

    def lib_cpp_code(self, dir_cppcode, dir_current=dir_current):
        ''' produce the dynamice libarary of lcurves
        '''
        print(f'#-------------------------start make {dir_cppcode} lib------------------------\n\n')
        #dircode = os.path.join(dir_current, 'srcs', dir_cppcode, 'src')
        #libs = os.path.join(dir_current, 'srcs', dir_cppcode, 'src', '.libs', '*.so')
        libs = os.path.join('$TRM_SOFTWARE', 'lib', 'libpylcurve.so')
        libpy = os.path.join(dir_current, 'pylcurve', 'lib')
        #subprocess.call(['make',  '-C', dircode])
        #os.system(f'cp {libs} {libpy}')
        os.system(f'cp {libs} {libpy}')
        #subprocess.call(['make', 'clean', '-C', dircode])
        print(f'#-------------------------end make {dir_cppcode} lib--------------------------\n\n\n')
 
    def run(self):
        self.install_cpp_code('cpp-lcurve')
        self.lib_cpp_code('cpp-lcurve')
        install.run(self)

def install_cpp_code(install, dir_cppcode):
    ''' install the cpp code of lcurves e.g. cpp-lcurve
    '''
    print(install)
    if install == 'install':
       os.chdir(dir_cppcode)
       os.system('./bootstrap')
       os.chdir(dir_current)

######--------------------install cpp-lcurve-------------------------------
#dir_cpplcurve = os.path.join(dir_current, 'srcs', 'cpp-lcurve')
#install_cpp_code(install, dir_cpplcurve)


'''
subprocess.call(['make',  '-C', './srcs/cpp-lcurve/src'])
os.system('cp ./srcs/cpp-lcurve/src/.libs/*.so pylcurve/lib/')
subprocess.call(['make', 'clean', '-C', './srcs/cpp-lcurve'])
'''


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
        cmdclass={'install': _install},
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
