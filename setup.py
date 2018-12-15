from setuptools import setup, find_packages

setup(
    name="template",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'solution=model.__main__:main',
        ],
    },
)
