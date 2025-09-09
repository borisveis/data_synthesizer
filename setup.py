from setuptools import setup

setup(
    name='data_synthesizer',           # ← This should be data_synthesizer
    version='1.0.0',
    packages=['data_synthesizer'],     # ← This should be data_synthesizer
    install_requires=[
        'faker',
        'fastapi',
        'uvicorn',
        'pydantic',
        'httpx',
        'Pydbgen',
        'Mimesis',
        # 'DataSynthesizer==0.1.13',  # Commented out
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