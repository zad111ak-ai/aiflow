from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="aiflow",
    version="0.1.0",
    description="AI Workflow Runner — YAML configs, any model, one terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="zad111ak-ai",
    url="https://github.com/zad111ak-ai/aiflow",
    py_modules=["aiflow_cli"],
    scripts=["aiflow"],
    install_requires=[
        "requests>=2.28.0",
        "pyyaml>=6.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: System :: Shells",
    ],
)
