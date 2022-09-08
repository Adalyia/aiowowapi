from setuptools import setup

    
readme = ''
with open('README.rst') as f:
    readme = f.read()
    
requirements = [
    'aiohttp>=3.7.0,<3.9.0'
]

extras_require = {
    'docs': [
        'sphinx>=4.1.2',
        'sphinx_rtd_theme>=0.5.2',
    ]
}

packages = [
    'aiowowapi',
    'aiowowapi.retail',
    'aiowowapi.classic',
]

setup(
    name='aiowowapi',
    author='Adalyia',
    url='https://github.com/Adalyia/aiowowapi',
    project_urls={
    "Documentation": "https://docs.adalyia.com/wowapi",
    "Issue tracker": "https://github.com/Adalyia/aiowowapi/issues",
    },
    version='2.0.2',
    packages=packages,
    license='MIT',
    description='An async ready client library for the World of Warcraft APIs',
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires='>=3.8.0',
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Internet',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
    ]
)