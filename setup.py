from setuptools import setup


setup(name='trypengine',
      version='0.0.1',
      description='trypengine',
      install_requires=["pandas==0.12.0",
                        "XlsxWriter==0.5.2",
                        "xlrd==0.9.2",
                        "psycopg2==2.5.2"],
      author='Paulo Patricio Aquino',
      author_email='ogiaquino@gmail.com',
      maintainer='Paulo Patricio Aquino',
      maintainer_email='ogiaquino@gmail.com',
      platforms='Linux',
      url='https://github.com/ogiaquino/trypengine',
      zip_safe=False,
      tests_require=['nose'],
      test_suite='nose.collector',
      )
