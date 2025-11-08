import os
from pathlib import Path

project_name = "us_visa"

list_of_files = [

    f"{project_name}/__int__.py",
    f"{project_name}/componets/__int__.py",
    f"{project_name}/componets/data_ingestion.py",
    f"{project_name}/componets/data_validation.py",
    f"{project_name}/componets/data_transformation.py",
    f"{project_name}/componets/model_trainer.py",
    f"{project_name}/componets/model_evaluation.py",
    f"{project_name}/componets/model_pusher.py",
    f"{project_name}/configuration/__int__.py",
    f"{project_name}/constans/__int__.py",
    f"{project_name}/enity/__int__.py",
    f"{project_name}/enity/config_enity.py",
    f"{project_name}/enity/artifact_enity.py",
    f"{project_name}/exception/__int__.py",
    f"{project_name}/logger/__int__.py",
    f"{project_name}/pipeline/__int__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__int__.py",
    f"{project_name}/utils/main_utils.py",
    ]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")