import setuptools


long_desc = ''
with open('README.md', 'r') as f:
    long_desc = f.read()

setuptools.setup(
    name='data-reader',
    version='0.0.5',
    author='Ibragim Abubakarov',
    author_email='ibragim.ai95@gmail.com',
    maintainer='Ibragim Abubakarov',
    maintainer_email='ibragim.ai95@gmail.com',
    description='Lightweight Python package that can lazily read large data files.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/polkovnik-z/python-data-reader',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=['ijson'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
