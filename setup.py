import os
import setuptools

setuptools.setup(
    name='pycarver',
    version='0.0.1',
    packages=setuptools.find_packages(),
    package_data={"": ['*.jpg', '*.png', '*.json', '*.txt']},
    author='Hayden Welch',
    author_email='hcw360@gmail.com',
    description='Image processing to estimate work time on handcarved leather goods',
    long_description=open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'README.md')).read(),
    license='GPLv3+',
    url='https://github.com/hwelch-fle/pycarver',
    install_requires=['numpy',
                      'scipy',
                      'Pillow',
                      'opencv-python',],
    classifiers=['Development Status :: 0 - Alpha',
                 'Intended Audience :: Crafts/Artists',
                 'License :: GPLv3+ License',
                 'Operating System :: OS Independent',
                 'Topic :: Art :: Leatherworking'],
)