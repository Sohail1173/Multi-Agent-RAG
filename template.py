import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="src"
list_of_files=[

    f"{project_name}/__init__.py",
    f"{project_name}/agents/__init__.py",
    f"{project_name}/agents/graph.py",
    f"{project_name}/agents/nodes.py",
    # f"{project_name}/retriever",
    f"{project_name}/retriever/__init__.py",
    f"{project_name}/retriever/embed_generation.py",
    f"{project_name}/retriever/docs_retriever.py",
   f"{project_name}/logging/__init__.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "main.py",
    "setup.py",

]

for filepath in list_of_files:
    filepath=Path(filepath)
    print(f"filepath::{filepath}")
    dirpath,filename=os.path.split(filepath)
    if dirpath!="":
        os.makedirs(dirpath,exist_ok=True)
        logging.info(f"dir created {dir} for {filepath}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"creating file:{filepath}")
    else:
        logging.info(f"{filepath} is already exists")