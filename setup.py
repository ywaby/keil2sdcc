from setuptools import setup

install_requires = []

long_description = """
Convert keil program to sdcc
support c51 to sdcc

`website/docs <http://github.org>`_
"""

setup(name='keil2sdcc',
      description='Convert c51 to sdcc',
      version='0.0.1',
      license='MIT',
      author='ywaby',
      author_email='ywaby@163.com',
      url='http://github.com',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Topic :: Software Development :: File Convert',
      ],
      keywords="Convert c51 to sdcc",

      packages=['keil2sdcc'],
      install_requires=install_requires,
      long_description=long_description,
      entry_points={
          'console_scripts': [
              'keil2sdcc = keil2sdcc.__main__:main'
          ]
      },
      )
