from setuptools import setup, find_packages

setup(name='iotleds',
      version='0.1',
      packages=find_packages(),
      install_requires=['flask', 'flask-socketio'])
