from setuptools import setup, find_packages


setup(
    name="camera_alglin",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["opencv-python", "numpy"],
    author="Luise Pessoa Bastos",
    author_email="luise@gustavobastos.com.br",
    description="Uma biblioteca de criptografia.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/luisebastos/APS_03",
    entry_points={
        'console_scripts': [
            'APS_03=APS_03.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)