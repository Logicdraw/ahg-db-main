from setuptools import setup


setup(
	name='ahg-db',
	version='1.1',
	py_modules=['cli', 'cli.commands'],
	install_requires=[
		'click',
	],
	entry_points='''
		[console_scripts]
		ahg-db-cli=cli.cli:cli
	''',
)


