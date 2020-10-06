from setuptools import setup, find_packages

THEME_NAME = 'cursive'
PACKAGE_NAME = f'mkdocs-{THEME_NAME}'

# Version
version_file = './{}/version.py'.format(PACKAGE_NAME)
version = {}
exec(open(version_file).read(), version)

# Readme
with open('README.md', 'r') as f:
    readme = f.readlines()
readme = ''.join(readme)

setup(name=PACKAGE_NAME,
      version=version['__version__'],
      url='https://github.com/ankur-gupta/mkdocs-cursive',
      license='MIT',
      author='Ankur Gupta',
      author_email='ankur@perfectlyrandom.org',
      description='MkDocs Cursive theme',
      long_description=readme,
      long_description_content_type="text/markdown",
      keywords='mkdocs, theme',
      packages=find_packages(),
      include_package_data=True,  # => if True, you must provide MANIFEST.in
      entry_points={
          'mkdocs.themes': [
              f'{THEME_NAME} = {THEME_NAME}'
          ]
      },
      zip_safe=False)
