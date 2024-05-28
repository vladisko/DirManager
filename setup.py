from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='directorymanager',
    version='0.0.1',
    author='dumenko_vladyslav',
    author_email='',
    description='directory management library',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/vladisko',
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='directory management',
    project_urls={
        'GitHub': 'https://github.com/vladisko'
    },
    python_requires='>=3.6'
)
