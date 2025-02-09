from setuptools import find_packages, setup

setup(
    name="streamlit-navbar",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["streamlit"],
    author="Honey Kumar",
    author_email="sdithoney@gmail.com",
    description="A responsive navbar component for Streamlit apps.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aimlhoney/streamlit-navbar",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)