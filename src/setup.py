from setuptools import setup # type: ignore

setup(
    name="barky",
    version="0.1.1",
    packages=["djbarky"],
)
from setuptools import setup, find_packages # type: ignore

setup(
    name="pms",
    version="0.1.0",
    packages=find_packages(),
    
    include_package_data=True,
    # Additional metadata about your package
    description="Patient Monitoring System",
    author="Your Name",
    author_email="your.email@example.com",
    # More detailed description
    long_description=open('README.md').read(),
   
    url="https://github.com/yourusername/pms",
   
    install_requires=[
        # 'dependency==version',
    ],
    # To provide executable scripts, use entry points
    entry_points={
        'console_scripts': [
            # 'script_name = module:function',
        ],
    },
   
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Django",
        "Operating System :: OS Independent",
    ],
)
