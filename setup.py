from typing import Optional

from setuptools import setup, find_packages


package_name = 'flake8_annotations_coverage'


def get_version() -> Optional[str]:
    with open('flake8_annotations_coverage/__init__.py', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('__version__'):
            return line.split('=')[-1].strip().strip("'")


def get_long_description() -> str:
    with open('README.md') as f:
        return f.read()


setup(
    name=package_name,
    description='A flake8 extension that checks for type annotations coverage',
    long_description=get_long_description(),
    packages=find_packages(),
    include_package_data=True,
    keywords='flake8 annotations',
    version=get_version(),
    author='Ilya Lebedev',
    author_email='melevir@gmail.com',
    install_requires=['setuptools'],
    entry_points={
        'flake8.extension': [
            'TAE001 = flake8_annotations_coverage.annotations_coverage:AnnotationsCoverageChecker',
        ],
    },
    url='https://github.com/best-doctor/flake8-annotations-coverage',
    license='MIT',
    py_modules=[package_name],
    zip_safe=False,
)
