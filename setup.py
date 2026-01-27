#!/usr/bin/env python3
"""
Setup configuration for Tier-2 Semantic Layer
"""
from setuptools import setup, find_packages

setup(
    name="seekreap-tier2-structural",
    version="0.1.0",
    description="SeekReap Tier-2: Semantic Layer - Envelope creation and transformation",
    author="SeekReap Team",
    author_email="tier2@seekreap.example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Pure Python, no external dependencies
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
