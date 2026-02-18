import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification, TrainingArguments, Trainer
from datasets import load_dataset
import numpy as np
import evaluate

# Load dataset
dataset = load_dataset("imagefolder", data_dir="../data")

# Load processor
processor = AutoImageProcessor.from_pretrained("facebook/convnext-base-224")

def transform(example):
    inputs = processor(example["image"], return_tensors="pt")
    example["pixel_values"] = inputs["pixel_values"][0]
    return example

dataset = dataset.with_transform(transform)

# Load model
model = AutoModelForImageClassification.from_pretrained(
    "facebook/convnext-base-224",
    num_labels=2
)

# Freeze backbone for small dataset test
for param in model.base_model.parameters():
    param.requires_grad = False

training_args = TrainingArguments(
    output_dir="./convnext-ai-detector",
    per_device_train_batch_size=2,
    num_train_epochs=2,
    save_strategy="no"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"]
)

trainer.train()

trainer.save_model("./convnext-ai-detector")
processor.save_pretrained("./convnext-ai-detector")
