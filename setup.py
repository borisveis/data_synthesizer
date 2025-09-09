from setuptools import setup

setup(
    name='synthesizer',
    version='1.0.0',
    packages=['data_synthesizer'],
    install_requires=[
        'faker',
        'fastapi',
        'uvicorn',
        'pydantic',
        'httpx',
        'Pydbgen',
        'Mimesis',
        # 'DataSynthesizer==0.1.13',  # Problematic package - see alternatives below
        # 'Trumania'  # Commented out as it was in your requirements.txt
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-playwright',
        ]
    },
    author='Boris Veis',
    author_email='boris.veis@gmail.com',
    python_requires='>=3.7'
)