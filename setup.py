from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='file_api',
    packages=['file_api'],
    version='0.1',
    description='Client for the Bmat TV/AV file api',
    author='BMAT developers',
    author_email='tv-av@bmat.com',
    url='https://github.com/bmat/file_api',
    download_url='https://github.com/bmat/file_api/archive/master.zip',
    keywords=['bmat', 'file', 'api'],
    classifiers=['Topic :: Adaptive Technologies', 'Topic :: Software Development', 'Topic :: System',
                 'Topic :: Utilities'],
    install_requires=install_requires
)
