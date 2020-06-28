import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discordbook", 
    version="0.1.0",
    author="Charlie Luo",
    author_email="charliexluo@gmail.com",
    description="A Discord.py module to facilitate easier viewing for large amounts of content.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cvxluo/discordbook",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)