from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements 
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return

setup(
    name='Crop Yield Prediction India',
    version='0.1',
    author='Prasad Sonar',
    author_email="prasadsonar09@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)