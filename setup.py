# setup.py — Project structure generator
import os

# Saari folders aur files ki list
structure = {
    "data/raw": [],           # Kaggle se downloaded CSV
    "data/processed": [],     # Clean kiya hua data
    "notebooks": [
        "01_EDA.ipynb",
        "02_model_training.ipynb"
    ],
    "src": [
        "__init__.py",
        "preprocess.py",      # Data cleaning functions
        "train.py",           # Model training
        "predict.py",         # Prediction function
        "evaluate.py"         # Model evaluation
    ],
    "models": [],             # Saved .pkl model files
    "webapp": [
        "app.py",             # Flask/Streamlit app
        "templates/index.html"
    ],
    "reports": [
        "figures/"            # EDA plots save honge yahan
    ]
}

# Folders aur files banao
for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)
    print(f"✅ Folder created: {folder}/")
    for file in files:
        filepath = os.path.join(folder, file)
        # Nested folder handle karo (jaise templates/)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                pass  # Empty file
            print(f"   📄 File created: {filepath}")

# Root level files
root_files = [
    "requirements.txt",
    "README.md",
    ".gitignore"
]

for file in root_files:
    if not os.path.exists(file):
        with open(file, "w") as f:
            pass
        print(f"📄 Root file created: {file}")

print("\n🎉 Project structure ready hai!")
print("Ab 'data/raw/' folder mein Kaggle dataset rakho.")