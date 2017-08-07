from setuptools import setup

setup(
    name='barron_gen',
    version='0.1',
    description='Vocabulary test generator',
    long_description=open('README.rst').read(),
    url='https://github.com/maomihz/Barron-Paper-Gen',
    author='Dexter MaomiHz',
    author_email='maomihz@gmail.com',
    license='MIT',
    packages=['barron'],
    include_package_data=True,

    entry_points = {
        'console_scripts': ['barron=barron:main']
    }
)
