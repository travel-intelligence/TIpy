from distutils.core import setup

requirements = [
    'simplejson'
]

setup(
  name = 'travel_intelligence',
  packages = ['travel_intelligence'], # this must be the same as the name above
  version = '0.10',
  install_requires=requirements,
  description = 'A wrapper around the travel-intelligence Web Service API',
  author = 'Sebastien Perez',
  author_email = 'sebastien.perez@amadeus.com',
  url = 'https://github.com/travel-intelligence/TIpy', # use the URL to the github repo
  download_url = 'https://github.com/travel-intelligence/TIpy/tarball/0.10', # I'll explain this in a second
  keywords = ['travel', 'intelligence', 'business', 'api', 'web services'], # arbitrary keywords
  classifiers = [],
)
