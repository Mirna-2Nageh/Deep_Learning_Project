# Deep_Learning_Project
# Pneumonia Classification Project

## Overview
Binary classification of pediatric chest X-rays (Pneumonia vs Normal) using:
- VGG-19 (from scratch)
- ResNet (transfer learning)
- Inception V1 (transfer learning)
- MobileNet / Vision Transformer (transfer learning)

## Setup
1. Create virtual env: `python3 -m venv deep && source deep/bin/activate`
2. Install: `pip install -r requirements.txt`

## Data
Dataset: Kaggle - paultimothymooney/chest-xray-pneumonia

## Run training
Example:
`python src/train.py --config configs/vgg_scratch.yaml`

## Evaluation & XAI
- Metrics: accuracy, precision, recall, F1, ROC, AUC
- Explanations: Grad-CAM, Integrated Gradients

## References
- Simonyan & Zisserman, VGG (2014). :contentReference[oaicite:5]{index=5}
- He et al., ResNet (2015). :contentReference[oaicite:6]{index=6}
- Szegedy et al., Inception V1 (2014). :contentReference[oaicite:7]{index=7}
- Howard et al., MobileNet (2017). :contentReference[oaicite:8]{index=8}
- Dosovitskiy et al., ViT (2020). :contentReference[oaicite:9]{index=9}
- Grad-CAM (Selvaraju et al., 2017). :contentReference[oaicite:10]{index=10}
