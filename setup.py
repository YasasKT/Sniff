from setuptools import setup, find_packages

setup(
    name='packetSniffer',
    version='1.0',
    author='Yasas',
    author_email='yasskt@gmail.com',
    description='A simple packet sniffer tool',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'packetSniffer=packetSniffer.__main__:main',
        ],
    },
    install_requires=[
        'scapy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
)