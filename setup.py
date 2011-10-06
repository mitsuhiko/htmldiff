try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='htmldiff',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    version='0.1',
    url='http://github.com/mitsuhiko/htmldiff',
    py_modules=['htmldiff'],
    description='Diffs arbitrary HTML inline.',
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
    ]
)
