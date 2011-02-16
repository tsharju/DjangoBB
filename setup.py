from setuptools import setup, find_packages

setup(
    name = 'DjangoBB',
    version = '0.1',
    url = 'http://djangobb.org',
    packages = ['djangobb'],
    install_requires=['django-registration==0.7',
                      'django-haystack>=1.1.0',
                      'django-authopenid==1.0.1',
                      'PIL==1.1.7',
                      'Markdown==2.0',
                      'django-messages==0.4.4',
                      'django-mailer==0.1.0',
                      'whoosh==1.5.9'],
    zip_safe=False,
)
