from setuptools import setup

setup(
    name='synthesizer',
    version='1.0.0',
    packages=['synthesizer'],
    install_requires=[
        'faker',
        'Pydbgen'
        'Mimesis'
        'Trumania'
        'pydantic'
        'uvicorn'
        'fastapi'
        'httpx'
        'DataSynthesizer'
            ],
    author='Boris Veis',
    author_email='boris.veis@gmail.com'
)