from setuptools import setup


setup(
	name='ahg-serv-database',
	version='1.1',
	py_modules=['cli', 'cli.commands'],
	install_requires=[
		'click',
	],
	entry_points='''
		[console_scripts]
		ahg-serv-database-cli=cli.cli:cli
	''',
)


