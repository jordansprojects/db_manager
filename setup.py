from setuptools import setup, find_packages

setup(
        name='my_module',
        version='0.1.0',
        author='Your Name',
        author_email='your.email@example.com',
        description='A short description of your module.',
        packages=find_packages(), # Automatically finds packages in the directory
        install_requires=[
            # List any external dependencies your module needs, e.g., 'requests>=2.20.0'
        ],
        python_requires='>=3.6', # Specify compatible Python versions
    )