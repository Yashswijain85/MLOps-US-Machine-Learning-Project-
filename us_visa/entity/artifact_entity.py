from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str 



@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    drift_report_file_path: str



@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str


@dataclass
class ClassificationMetricArtifact:
    f1_score:float
    precision_score:float
    recall_score:float



@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str 
    metric_artifact:ClassificationMetricArtifact


@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool # if current model is accepted rather than production model, it is true, else, it is false
    changed_accuracy:float # difference between the current or training accracy and production accuracy 
    s3_model_path:str 
    trained_model_path:str

@dataclass
class ModelPusherArtifact:
    bucket_name:str
    s3_model_path:str