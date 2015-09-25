from distutils.core import setup
setup(
  name = 'travel-intelligence',
  packages = ['travel-intelligence'], # this must be the same as the name above
  version = '0.1',
  install_requires=['json','urllib2','urllib'],
  description = 'A wrapper around the travel-intelligence Web Service API',
  author = 'Sebastien Perez',
  author_email = 'sebastien.perez@amadeus.com',
  url = 'https://github.com/travel-intelligence/TIpy', # use the URL to the github repo
  download_url = 'https://github.com/travel-intelligence/TIpy/tarball/0.1', # I'll explain this in a second
  keywords = ['travel', 'intelligence', 'business', 'api', 'web services'], # arbitrary keywords
  classifiers = [],
)
