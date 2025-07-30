#!/usr/bin/env python
"""Setup script for Drift-Aware RAG project."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="drift-aware-rag",
    version="0.1.0",
    author="Elena Paunova",
    author_email="elena.paunova@university.edu",
    description="Drift-Aware Retrieval-Augmented Language Models for Production Environments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/drift-aware-rag",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/drift-aware-rag/issues",
        "Documentation": "https://yourusername.github.io/drift-aware-rag/",
        "Source Code": "https://github.com/yourusername/drift-aware-rag",
    },
    packages=find_packages(exclude=["tests", "tests.*", "experiments", "experiments.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
            "pre-commit>=3.5.0",
        ],
        "docs": [
            "mkdocs>=1.5.0",
            "mkdocs-material>=9.4.0",
            "mkdocstrings>=0.23.0",
            "mkdocstrings-python>=1.7.0",
        ],
        "gpu": [
            "triton>=2.1.0",
            "nvidia-ml-py>=12.535.0",
            "gpustat>=1.1.1",
        ],
    },
    entry_points={
        "console_scripts": [
            "drift-detect=src.drift_detection.cli:main",
            "rag-align=src.rag_alignment.cli:main",
            "rag-benchmark=src.efficiency.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "drift_aware_rag": [
            "configs/*.yaml",
            "data/*.json",
        ],
    },
)
