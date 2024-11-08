from setuptools import setup, find_packages

setup(
    name="iloveyou",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'iloveyou=iloveyou.main:main',  # Maps the command 'iloveyou' to your main function
        ],
    },
    install_requires=[
        
    ],
    description="A fun turtle script to display 'I love you'.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/hundifops/ILOVEYOU",
)
