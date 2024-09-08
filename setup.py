from setuptools import setup

setup(
    name='SenialSOLID',
    version='4.0.0',
    description='SenialSOLID - Principio OCP ',
    long_description='Este proyecto implementa el patrón Strategy para la adquisición y el procesamieto de señales.',
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