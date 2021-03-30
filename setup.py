import setuptoolsSo i had no choice, this package is



long_desc = ''
with open('README.md', 'r') as f:
    long_desc = f.read()

setuptools.setup(
    name='data-reader',
    version='0.0.1',
    author='Ibragim Abubakarov',
    author_email='ibragim.ai95@gmail.com',
    maintainer='Ibragim Abubakarov',
    maintainer_email='ibragim.ai95@gmail.com',
    description='Python package that allows easy importation of data from large files like CSV, JSON and XML.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/polkovnik-z/data-reader',
    packages=[
        'data_reader'
    ],
    install_requires=['pandas', 'imperium', 'ijson'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers'
    ]
)
