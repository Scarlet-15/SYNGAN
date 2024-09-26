# SYNGAN: Tamil Text-to-Image Synthesis using Generative Adversarial Networks

This repository implements **SYNGAN**, a novel framework designed for generating high-quality images from Tamil text descriptions using Generative Adversarial Networks (GANs). The model utilizes **MURIL**, **FastText**, and **GloVe** to generate Tamil text embeddings and passes these embeddings to a **DCGAN** model to generate realistic images from Tamil text descriptions.

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Model Architecture](#model-architecture)
- [Dataset](#dataset)
- [Installation](#installation)
- [Training](#training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Text-to-image synthesis is a cutting-edge research area in computer vision, where models are developed to generate realistic images from text descriptions. While existing models have shown significant progress with English text, vernacular languages like **Tamil** present unique challenges due to their morphological richness and complexity.

**SYNGAN** aims to bridge this gap by using Tamil text descriptions to generate images. We used the **Oxford 102 Flowers Dataset** and generated English descriptions for each flower species. The English descriptions were then translated into **Tamil** using Google Translate. Tamil embeddings were generated using **MURIL**, **FastText**, and **GloVe**, which were subsequently used in a **DCGAN** architecture to generate images corresponding to the Tamil descriptions.

## Methodology

### Dataset
We used the **Oxford 102 Flowers Dataset**, which consists of images of 102 flower species. English descriptions were obtained for each flower, and these descriptions were translated into Tamil using Google Translate. The embeddings for the Tamil text were generated using the following models:
- **MURIL** (Multilingual Representations for Indian Languages)
- **FastText** (Word embeddings for fast text processing)
- **GloVe** (Global Vectors for Word Representation)

These embeddings were then passed to the **DCGAN** model to synthesize images.

## Model Architecture

The architecture consists of:
1. **Generator**: Converts noise vectors and Tamil text embeddings into image tensors using convolutional layers with ReLU and Tanh activations.
2. **Discriminator**: Distinguishes between real and generated images using Leaky ReLU and Sigmoid activations.

The GAN is trained using a modified **MINIMAX loss function**. Feature matching using the **L1 norm** was implemented to ensure the diversity of generated images.

## Dataset

- **Oxford-102 Flower Dataset**

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Scarlet-15/SYNGAN.git
    ```

### Pre-trained Models

- **MURIL**: [Download MURIL](https://tfhub.dev/google/MuRIL/1)
- **FastText**: [Download FastText Tamil model](https://fasttext.cc/docs/en/crawl-vectors.html)
- **GloVe**: [Download GloVe](https://nlp.stanford.edu/projects/glove/)

## Training

The training script allows for specifying parameters such as the number of epochs, batch size, and learning rates for both the generator and discriminator. The training loop optimizes both models using **Adam Optimizer** with learning rates of `1e-4`.

### Key Hyperparameters:
- `noise_dim`: Dimension of the noise vector fed to the generator (default: 100).
- `embedding_dim`: Dimension of the Tamil text embeddings (default: 768).
- `image_resolution`: The model is designed for generating **512x512** resolution images.

## Results

### Metrics Used:
1. **Fréchet Inception Distance (FID)**: This metric is used to evaluate the quality of the generated images by comparing the statistics of generated images to real images. A lower FID score indicates better image quality and diversity.
   
2. **Inception Score**: The Inception Score evaluates the quality and diversity of the generated images by passing them through a pre-trained Inception model. It assesses how well the generated images belong to clear object categories and their diversity within those categories. A higher Inception Score indicates better performance.

3. **Loss Curves**: During training, the loss curves for both the **generator** and **discriminator** are monitored to ensure stable training. A gradual reduction in generator loss and stability in discriminator loss indicate that the model is learning effectively.

The model performed competitively on the Oxford-102 flower dataset with a good balance of image quality and diversity, as indicated by the FID and Inception scores. Additionally, the loss curves demonstrated stable GAN training with minimal issues such as mode collapse.


