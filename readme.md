
# Project Setup and Run Instructions

Follow these steps to set up and run the project.

---

## 1. Create Python Virtual Environment

Make sure you have Python 3.8+ installed.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

---

## 2. Install TensorFlow (Recommended for users in Iran)

Due to restrictions, you can either:

### Option A: Use pip mirror in Iran

Use a trusted mirror (such as from University of Science and Technology):

```bash
pip install -i https://mirrors.sustech.edu.cn/pypi/web/simple/ tensorflow
```

### Option B: Use DNS tools like Shecan

1. Go to [Shecan.ir](https://www.shecan.ir/)
2. Set your DNS to:
   - `178.22.122.100`
   - `185.51.200.2`
3. Then install via regular pip:

```bash
pip install tensorflow
```

---

## 3. Install Other Requirements

Make sure you're in your virtual environment, then:

```bash
pip install -r requirements.txt
```
or if you using mirror instead of DNS 
```bash
pip install -i https://mirrors.sustech.edu.cn/pypi/web/simple/ -r requirements.txt
```
---

## 4. Run the Notebook

Open and run all cells in the notebook file:

```bash
jupyter notebook diabeties.ipynb
```

Or use VS Code or any Jupyter-compatible interface to execute the notebook.

---

## 5. Start the Django Server

Navigate to the `core` directory and run:

```bash
cd core
python manage.py runserver
```

The server should now be running at: `http://127.0.0.1:8000/`

---
