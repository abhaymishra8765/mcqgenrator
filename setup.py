from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='abhay mishra',
    author_email='abhaymishra94814@gmal.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2", "pandas"],
    packages=find_packages()
)