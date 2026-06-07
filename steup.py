from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT = '-e .' 
def get_requirements(file_path:str)->list:
    with open(file_path) as f:
        requirements = f.readlines()
    requirements = [req.strip() for req in requirements if req.strip()]
   

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)      

    return requirements  
    
setup(
    name="mlproject",
    version="0.0.1",
    author="Vishal",
    author_email="vishalagrahari2024@gmail.com",
    description="A sample Python package",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
