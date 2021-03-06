#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="FlightPlanDB",
    version="0.0.1",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "docopt==0.6.2",
        "requests==2.24.0",
        "python-dateutil==2.8.1"
    ],
    extras_require={
        "dev": [
            "flake8==3.8.4",
            "mypy==0.790",
        ]
    },
    entry_points = {
        'console_scripts': ['flightdb-test=FlightPlanDB.flightplandb:test_run'],
    }
)
