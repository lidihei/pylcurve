from setuptools import find_packages
#from distutils.core import setup, Extension
from setuptools import setup
import os
import numpy
import subprocess
from distutils.command.install import install

###Check the OS system
import platform
os_name = platform.system()
if os_name =="Darwin":
    lib_format = "dylib" # MacOS
else:
    lib_format = "so"  # Linux


dir_current = os.path.dirname(os.path.abspath(__file__))

#### write a Makefile from Makefile_pyclurve######
lines = [f"CPPFLAGS = -I./cpp-lcurve/include {os.environ['CPPFLAGS']}\n"]
lines += [f"LDFLAGS = {os.environ['LDFLAGS']}\n"]



#### install class
class _install(install):

    def set_environ(self):
        _continue = True
        try:
           os.environ['TRM_SOFTWARE']
           print('The TRM_SOFTWARE environment is existed')
        except:
            print('The TRM_SOFTWARE environment is not existed. \n Do you want set TRM_SOFTWARE environment same as the CONDA_PREFIX: [y/n]')
            sss = input()
            if sss.lower() == '' or sss.lower() == 'y':
                print('The TRM_SOFTWARE environment will be set the same as CONDA_PREFIX')
                print(f"CONDA_PREFIX={os.environ['CONDA_PREFIX']}\n")
                os.system(f"export TRM_SOFTWARE={os.environ['CONDA_PREFIX']}")
                print(f"TRM_SOFTWARE={os.environ['CONDA_PREFIX']}\n\n\n")
            else:
                print('you should set TRM_SOFTWARE environment by yourself, firstly.')
                _continue = False
        return _continue


    def install_cpp_code(self, dir_cppcode, dir_current=dir_current):
        ''' install the cpp code of lcurves e.g. cpp-lcurve'''
        print(f'change working directory to: {dir_cppcode} \n\n')
        dir_cppcode = os.path.join(dir_current, 'srcs',  dir_cppcode)
        os.chdir(dir_cppcode)
        print(f'------------------------start install {dir_cppcode} ------------------------')
        os.system('./pyinstall')
        subprocess.call(['make', 'clean', '-C', '.'])
        print(f'change working directory to: {dir_current} \n\n')
        os.chdir(dir_current)
        print(f'------------------------end install {dir_cppcode}---------------------------\n\n')

    def download_code(self, dir_current=dir_current, url = 'https://github.com/lidihei/cpp-lcurve.git'):
        dir_cppcode = os.path.join(dir_current, 'srcs')
        print(f'-------------------download: {dir_cppcode}---------------------------------\n\n')
        os.chdir(dir_cppcode)
        os.system(f'git clone {url}')
        if 'cpp-lcurve' in url:
            _makefile_os = os.path.join('cpp-lcurve', 'src', f'Makefile_{os_name}.am')
            _makefile = os.path.join('cpp-lcurve', 'src', f'Makefile.am') 
            os.system(f'cp {_makefile_os} {_makefile}')
        os.chdir(dir_current)

    def lib_cpp_code(self, dir_cppcode, dir_current=dir_current):
        ''' produce the dynamice libarary of lcurves
        '''
        print(f'#-------------------------start make {dir_cppcode} lib------------------------\n\n')
        #dircode = os.path.join(dir_current, 'srcs', dir_cppcode, 'src')
        #libs = os.path.join(dir_current, 'srcs', dir_cppcode, 'src', '.libs', '*.so')
        libs = os.path.join('$TRM_SOFTWARE', 'lib', f'libpylcurve.{lib_format}')
        libpy = os.path.join(dir_current, 'pylcurve', 'lib')
        #subprocess.call(['make',  '-C', dircode])
        #os.system(f'cp {libs} {libpy}')
        os.system(f'cp {libs} {libpy}')
        #subprocess.call(['make', 'clean', '-C', dircode])
        print(f'#-------------------------end make {dir_cppcode} lib--------------------------\n\n\n')

    def run(self):
        _continue = self.set_environ()
        if _continue: self.download_code()
        if _continue: self.install_cpp_code('cpp-lcurve')
        if _continue: self.lib_cpp_code('cpp-lcurve')
        if _continue: install.run(self)


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
            "Programming Language :: Python :: 3.11",
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
        package_data={'pylcurve': [f'./lib/*.{lib_format}'],
                      },
        ##headers=['csstpsf/Centroid/libCentroid/nrutil.h'],
        ##ext_modules=[ext],
)
