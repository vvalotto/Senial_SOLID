from setuptools import setup

setup(
    name='SenialSOLID',
    version='1.1.0',
    description='SenialSOLID - Aplicación del Principio SRP - con Módulos compilados separados',
    long_description='Este proyecto aplica el Principio de Responsabilidad Única (SRP) dividiendo las responsabilidades en diferentes módulos.',
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