from setuptools import setup, find_packages

setup(
    name='todo_site',
    version='0.1',
    python_requires='>=3.8',
    include_package_data=True,
    install_requires=[
        "asgiref",
        "Django",
        "django-cors-headers",
        "djangorestframework",
        "pytz",
        "sqlparse",
        "tzdata"
    ],

    packages=find_packages(),
)
