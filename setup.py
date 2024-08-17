import setuptools


setuptools.setup(
    name="DemoFE", 
    version="0.1",
    author="Katharine Long",
    author_email="katharine.long@ttu.edu",
    description="Minimalist finite elements",
    long_description="Minimalist finite elements",
    long_description_content_type="text/markdown",
    url="https://github.com/krlong014/DemoFE",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=['numpy', 'scipy']
)