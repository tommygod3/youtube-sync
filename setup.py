from setuptools import setup, find_packages

with open("README.md") as readme_file:
    _long_description = readme_file.read()

setup(
    name='youtube-sync',
    version='0.1.0',
    description='Youtube playlist sync tool',
    author='Tommy Godfrey',
    url='https://github.com/tommygod3/youtube-sync',
    long_description=_long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['docopt'],
    python_requires='>=3.5.0',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    zip_safe=False,
    entry_points={}
)
