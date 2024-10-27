from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function fetches list of Python packages used to make the ML application a package
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='MLOPSproject',
version='0.0.1',
author='Shruti Sharada, Vaishali, Abishek, Chaitra, Aysha Fathima',
author_email='sssharada99@gmail.com, vaishali.sekar_ds24fall@praxistech.school, abishek.k_ds24fall@praxistech.school, chaitra.pamidi_ds24fall@praxistech.school, ayshafathima2308@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)