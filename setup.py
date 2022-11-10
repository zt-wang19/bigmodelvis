
import setuptools
import os

requires = """torch>=1.8.0
transformers>=4.10.0
rich
"""

def get_requirements():
    ret = [x for x in requires.split("\n") if len(x)>0]
    print("requirements:", ret)
    return ret

with open('README.md', 'r') as f:
    setuptools.setup(
        name = 'bigmodelvis',
        version = "0.0.1",
        description = "A tool to visualize big models",
        long_description=open("README.md", "r", encoding="utf-8").read(),
        long_description_content_type="text/markdown",
        author = '',
        author_email = 'shengdinghu@gmail.com',
        license="Apache",
        url="https://github.com/zt-wang19/bigmodelvis",
        keywords = ['transformers', 'Visualizaiton', 'AI', 'DeepLearning'],
        python_requires=">=3.6.0",
        install_requires=get_requirements(),
        package_dir={'bigmodelvis':'bigmodelvis'},
        package_data= {
            'bigmodelvis':['requirements.txt'],
        },
        include_package_data=True,
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ]
    )
