# `pc` – Pocket Calculator emulator

## Usage

// TODO

## Developer guide

### Fetch source from repository

Download the source repository with `git` (or download a ZIP), then set the `cd` to the project directory.

```shell
git clone https://github.com/cstar-industries/python-3-beginner.git
cd 007-Building-A-Python-App
```

### Activating the virtual environment

A [virtual environment (venv)](https://docs.python.org/3/library/venv.html) makes sure you use a fixed local version of the Python interpreter and installed packages.

```shell
python3 -m venv venv
. venv/bin/activate         ## For Linux/macOS
venv\Scripts\activate.bat   ## For Windows
```

### Installing dependencies

Once you've activated the venv, install required dependencies with [`pip`](https://pip.pypa.io/en/stable/).

```shell
pip install -r requirements.txt
```

### Testing

Run the project tests with [`pytest`](https://docs.pytest.org/en/latest/)

```shell
pytest
```

### Running

Run the project executable with:

```shell
python -m pc
```

### Building

Build a distributable project wheel with [`setuptools`](https://setuptools.readthedocs.io/en/latest/) and [`wheel`](https://wheel.readthedocs.io/en/stable/).

```shell
python setup.py bdist_wheel
```

The built wheel can be found in the `dist` directory.

> Read more about packaging a python app in the [Python Packaging User Guide](https://packaging.python.org/)
