
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements
    from requirements.txt file.
    """
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [
            req.strip() for req in requirements
            if req.strip() and not req.strip().startswith("#")
        ]

    # Remove -e . if present in requirements
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='student_ml_project',
    version='0.0.1',
    author='tejaswini2964',
    author_email='tejaguluguluri2004@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
