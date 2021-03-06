try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='InPhOSite',
    version='1.0rc1',
    description='''The Indiana Philosophy Ontology Project web site and applications''',
    author='Jaimie Murdock',
    author_email='inpho@indiana.edu',
    url='http://inpho.cogs.indiana.edu',
    install_requires=[
        "mysql-python>=1.2",
        "Pylons>=1.0.0,<=1.0.99",
        "SQLAlchemy>=0.6.0,<=0.6.99",
        "Mako>=0.2.2,<=0.2.99",
        "FormBuild>=3.0,<3.99",
        "WebHelpers>=1.0,<1.99",
        "repoze.who>=1.0,<=1.0.99",
        "Sphinx>=0.6.4,<=0.6.99",
        "inflect>=0.2.0,<=0.2.99",
        "turbomail>=3.0.0,<=3.0.99",
        "BeautifulSoup>=3.2.0,<=3.2.99"
    ],
    dependency_links = [
        "http://pylonshq.com/download/"
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'inphosite': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'inphosite': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = inphosite.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
