from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
  name = 'nestedfetch',
  packages = ['nestedfetch'],
  version = '0.1',
  license='MIT',
  description = 'Syntactic sugar to deal with nested python dictionary and list. You can get, set, update and flatten values from deeply nested dictionaries and lists with a more concise, easier and a more KeyError, IndexError free way',
  long_description=readme,
  author = 'Shubham Dalvi',
  author_email = 'shubham.dalvi97@gmail.com', 
  url = 'https://github.com/saintlyzero/NestedFetch',
  download_url = ('https://github.com/saintlyzero/NestedFetch/archive/v_01.tar.gz'),
  keywords = [
      'dict',
      'nested dictionary',
      'nested list',
      'list',
      'flatten',
      'scalpl',
      'nestedfetch',
      'addict',
      'box',
      'Nested Fetch'
  ],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ]
)