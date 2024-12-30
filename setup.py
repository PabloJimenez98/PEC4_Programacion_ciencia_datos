from setuptools import setup, find_packages

setup(
    name="monegros",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas>=1.5.0',
        'numpy>=1.23.0',
        'matplotlib>=3.5.0',
        'pytest>=7.0.0',
        'Faker>=19.0.0',
    ],
    author="Pablo Jiménez Cruz",
    author_email="tu@email.com",
    description="Análisis de datos de la Orbea Monegros 2024",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/monegros",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)