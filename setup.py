from setuptools import setup

setup(
    name='SenialSOLID',
    version='6.0.0',
    description='SenialSOLID - LSP ',
    long_description='Resuelve la violación del principio de Liskov',
    long_description_content_type='text/markdown',
    author='VV',
    author_email='vvalotto@gmail.com',
    py_modules=['lanzador'],
    entry_points={'console_scripts': 'lanzador = lanzador:Lanzador.ejecutar'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)