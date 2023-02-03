from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tinypy",
    version="0.2.2",
    description="Tinypy is a collection of small Python functions and classes which make common patterns shorter and faster.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Arash Yeganeh",
    packages=find_packages(),
    url="https://github.com/arashyeganeh/tinypy",
    download_url="https://github.com/arashyeganeh/tinypy/releases/tag/0.2.2",
    keywords=[
        "utils",
        "tiny",
        "lightweight",
        "json",
        "convert json",
        "csv",
        "convert csv",
    ],
    install_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Utilities",
    ],
    project_urls={
        "Bug Reports": "https://github.com/arashyeganeh/tinypy/issues",
        "Source": "https://github.com/arashyeganeh/tinypy",
        "LinkedIn": "https://www.linkedin.com/in/arash-yeganeh",
    },
    python_requires=">=3",
    license="MIT",
    entry_points={
        "console_scripts": [
            "tinypy = tinypy.main:main",
        ]
    },
)
