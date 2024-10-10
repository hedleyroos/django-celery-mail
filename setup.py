from setuptools import setup, find_packages

setup(
    name="celery_mail",
    version="0.1",
    description="",
    url="https://github.com/hedleyroos/django_celery_mail",
    license="Proprietary",
    packages=find_packages(),
    install_requires=[
    ],
    include_package_data=True,
    tests_require=[
        "tox",
    ],
    zip_safe=False,
)
