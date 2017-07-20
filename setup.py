from setuptools import setup

setup(
    name="replacex",
    version="1.1.0",
    license='MIT',
    description="Replace string (regular expression) for files in current folder",
    author='1e0n',
    author_email='i@leons.im',
    keywords='replace all string regular expression folder',
    url='https://github.com/leonsim/replacex',
    packages=['replacex'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'replacex=replacex:main',
        ],
    },
)
