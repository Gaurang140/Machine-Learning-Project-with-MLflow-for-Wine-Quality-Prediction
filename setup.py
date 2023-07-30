import setuptools  as st

with open("description.txt" , "r" , encoding="utf-8") as f:
    l_discription = f.read()



__version__ = "0.0.0"

REPO_NAME = "Machine-Learning-Project-with-MLflow-for-Wine-Quality-Prediction"
AUTHOR_USER_NAME = "gaurang1404"
SRC_REPO = "wineQuality"
AUTHOR_EMAIL = "gaurangmeghanathi@gmail.com"


st.setup(name=SRC_REPO , 
         version=__version__ , 
         author=AUTHOR_USER_NAME , 
         author_email=AUTHOR_EMAIL , 
         description="python package for ml web app", 
         long_description=l_discription,
         url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=st.find_packages(where="src")
)
