from setuptools import setup, find_packages

requires = [
    'flask'
]

setup(
    name='ML Server API',
    version='0.0',
    description='A ML API built with Flask',
    author='mekafuyu',
    author_email='macyonbrunob@hotmail.com',
    keywords='web flask ml',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)