from setuptools import setup, find_packages

setup(
    name='function_notifier', 
    version='1.0.0',           
    author='Lewis Dean',
    description='This package contains the notify decorator, used to '
                'notify users when the wrapped function has finished '
                'execution.',
    long_description='This package contains the notify decorator, used to '
                     'notify users when the wrapped function has finished '
                     'execution.',
    long_description_content_type='text/markdown',
    packages=find_packages(),  # Automatically find all packages and subpackages
    python_requires='>=3.11',
    install_requires=[  
        'plyer>=2.1.0',  
    ],
)
