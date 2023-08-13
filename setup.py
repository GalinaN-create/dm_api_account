from setuptools import setup

REQUIRES = [
    'requests',
    'structlog',
    'curlify',
    'allure-pytest'
]

setup(
    name='dm_api_account',
    version='0.0.2',
    packages=['dm_api_account'],
    url='https://github.com/GalinaN-create/dm_api_account.git',
    license='MIT',
    author='Galina Nosova',
    author_email='-',
    install_requires=REQUIRES,
    description='dm_api_account with allure and logger'
)
