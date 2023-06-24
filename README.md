# Ausrine Example

## 1. Install

Download source.

```bat
git clone https://github.com/naoyoshinori/ausrine_example.git
```

Create a Python virtual environment.

```bat
cd ausrine_example
py -m venv venv
```

Run the `activate.bat` file. This will activate the Python virtual environment. Or execute the following command.

```bat
start .\venv\Scripts\activate
```

Install dependent libraries with the pip command.

```bat
(venv) ausrine_example> pip install https://github.com/naoyoshinori/ausrine/archive/main.zip
(venv) ausrine_example> pip install https://github.com/naoyoshinori/logging_support/archive/main.zip
```

## 2. Run the Ausrine Example

Run the `main.bat` file. Or execute the following command.

```bat
call .\venv\Scripts\activate
py main.py
```
