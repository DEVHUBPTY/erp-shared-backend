#!/usr/bin/env python3
"""
Setup script for erp-shared package
"""

from setuptools import setup, find_packages

# Leer el README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="erp-shared",
    version="0.1.0",
    author="captainsparrow10",
    author_email="javier1009rm@gmail.com",
    description="Paquete compartido entre microservicios del ERP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/captainsparrow10/erp-shared-backend",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.11",
    install_requires=[
        "pydantic>=2.11.0,<3.0.0",
        "email-validator>=2.2.0,<3.0.0",
        "python-jose[cryptography]>=3.4.0,<4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=8.3.5",
            "pytest-cov>=5.0.0",
            "black>=24.0.0",
            "isort>=5.13.0",
            "flake8>=7.0.0",
            "mypy>=1.8.0",
        ],
        "docs": [
            "mkdocs>=1.5.0",
            "mkdocs-material>=9.5.0",
        ],
    },
    keywords="erp, shared, microservices, schemas, utilities",
    project_urls={
        "Bug Reports": "https://github.com/captainsparrow10/erp-shared-backend/issues",
        "Source": "https://github.com/captainsparrow10/erp-shared-backend",
        "Documentation": "https://github.com/captainsparrow10/erp-shared-backend#readme",
    },
) 