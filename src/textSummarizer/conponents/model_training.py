import os
import torch
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk
from textSummarizer.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)

        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

        # Load preprocessed dataset
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,  # Updated output directory
            num_train_epochs=1,
            warmup_steps=500,
            per_device_train_batch_size=4,  # You can increase batch size with t5-small
            per_device_eval_batch_size=4,
            weight_decay=0.01,
            logging_steps=10,
            evaluation_strategy='steps',
            eval_steps=500,
            save_steps=int(1e6),  # Convert to int to avoid float issues
            gradient_accumulation_steps=4,  # Adjust based on your GPU memory
            report_to="none"
        )


        # trainer_args = TrainingArguments(
        #     output_dir=self.config.root_dir, num_train_epochs=1, warmup_steps=500,
        #     per_device_train_batch_size=1, per_device_eval_batch_size=1,
        #     weight_decay=0.01, logging_steps=10,
        #     evaluation_strategy='steps', eval_steps=500, save_steps=1000000,
        #     gradient_accumulation_steps=16
        # )

        trainer = Trainer(
            model=model,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["test"],
            eval_dataset=dataset_samsum_pt["validation"]
        )

        trainer.train()

        # Save model and tokenizer
        model.save_pretrained(os.path.join(self.config.root_dir, "t5-samsum-model"))  # ✅ Updated name
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
