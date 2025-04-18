from textSummarizer.pipeline.stage_01_data_ingestion import  DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import  DataValdiationPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_04_data_training import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evalution import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info((f">>>>stage{STAGE_NAME} started <<<<"))
    data_ingestion =DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info((f">>>>stage{STAGE_NAME} completed <<<<"))
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"
try:
    logger.info((f">>>>stage{STAGE_NAME} started <<<<"))
    data_validation = DataValdiationPipeline()
    data_validation.main()
    logger.info((f">>>>stage{STAGE_NAME} completed <<<<"))
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info((f">>>>stage{STAGE_NAME} started <<<<"))
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info((f">>>>stage{STAGE_NAME} completed <<<<"))
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

