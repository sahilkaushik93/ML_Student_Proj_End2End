from setuptools import  find_packages, setup
from typing import List

HYPHE_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this funciton will return the list of requirements
    :param file_path:
    :return:
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHE_E_DOT in requirements:
            requirements.remove(HYPHE_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Sahil',
    author_email='kaushiksahil1412@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)