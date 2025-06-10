# Description
The aim of this project is to clear and improve performance of a dataset

## Virtual environment

Linux :
```bash
python3 -m venv .venv
```

MacOS-Windows
```bash
python -m venv .venv
```

## Activate Virtual environment :
Windows : 
```bash
.venv\Scripts\activate
```

macOS/Linux : 
```bash
source .venv/bin/activate
```

## Dependencies :

* Make sure you're in the project directory
* Install dependencies : `pip install -r requirements.txt`
* Alternatively, you can install the libraries yourself by reading requierements.txt file
  
### Project structure
```bash
.
├── data
│   ├── data.csv
│   └── out.csv
├── modules
│   └── filter_data.py # main script
├── notebook.ipynb
├── README.md
├── requirements.txt
└── utils
    └── outliers.py

```

### Launch script to filter the default data.csv
```bash
python3 modules/filter_data.py
```
