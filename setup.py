from setuptools import find_packages, setup

# find_packages - finds all packages available in entire ML application

from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    this function will return the list of requirements
    """

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="ML-Project",
    version="0.0.1",
    author="Soumya",
    author_email="kushsoumya30@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
