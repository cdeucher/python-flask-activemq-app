from setuptools import setup, find_packages

setup(
	name='activemq-app',
	version='1.0.0a1',
	author='Cristiano Deucher',
	author_email='cristiano.deucher@cabd.link,
	description='App with Flask and ActiveMQ',
	url='',
	keywords=['objective', 'activemq', 'flask'],
	license='All Rights Reserved',

	packages=find_packages('src'),
	package_dir={'': 'src'},
	python_requires='>=3.8',
	install_requires=['Flask==1.1.2', 'Flask-Cors==3.0.10','Flask-RESTful==0.3.8','requests==2.25.1','python-dotenv==0.17.0',
	'stomp.py==7.0.0','bson==0.5.10'],
	extras_require={
		'tests': ['pytest>=6', 'pytest-asyncio>=0.14']
	}
)
