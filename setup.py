try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='htmldiff',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    version='0.2',
    url='http://github.com/mitsuhiko/htmldiff',
    py_modules=['htmldiff'],
    description='Diffs arbitrary HTML inline.',
    zip_safe=False,
    install_requires=['genshi', "html5lib"],
    test_suite='test',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
    ]
)
