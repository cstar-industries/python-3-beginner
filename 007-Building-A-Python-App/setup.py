import setuptools

setuptools.setup(
    name="pc",  # Replace with your own username
    version="0.0.1",
    author="Charles Francoise",
    author_email="chrales@chrales.dev",
    description="A python pocket calculator.",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'pc = pc.__main__:main_loop',
        ],
    },
    python_requires='>=3.7',
)
