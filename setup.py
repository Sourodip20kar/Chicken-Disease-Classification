import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.1.0"

REPONAME = "Chicken-Disease-Classification"
AUTHOR_USER_NAME= "Sourodip20kar"
SRC_REPO= "cnnClassifier"
AUTHOR_EMAIL="sourodipkar2002@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package for chicken disease classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Sourodip20kar/Chicken-Disease-Classification",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)