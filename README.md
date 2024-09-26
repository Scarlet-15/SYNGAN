# SYN GAN: Tamil Text-to-Image Synthesis using Generative Adversarial Networks

This repository implements **SYN GAN**, a novel framework designed for generating high-quality images from Tamil text descriptions using Generative Adversarial Networks (GANs). The architecture integrates language models like **TAM-BERT** and **MuRIL BERT** to process Tamil text, and GAN-based models for image generation.

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Model Architecture](#model-architecture)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Training](#training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Text-to-image synthesis has become an important area of research in computer vision. This task focuses on generating realistic images from text descriptions using deep learning techniques. While models like GANs have shown promising results for languages such as English, vernacular languages like **Tamil** remain largely unexplored.

Tamil, being a morphologically rich and agglutinative language, presents unique challenges for text-to-image generation models. Existing models, primarily designed for languages with simpler syntactic structures, struggle with Tamil's complexity. **SYN GAN** aims to bridge this gap by providing a GAN architecture specifically tailored for **Tamil text-to-image generation**.

## Methodology

### Dataset
The **Oxford-102 flower dataset** was used for this project. It consists of images of 102 flower species with corresponding English descriptions. To adapt the dataset for Tamil, the English descriptions were translated into **Tamil** using Google Translate.

### Text Embeddings
Tamil word embeddings were generated using:
- **MuRIL BERT**: A multilingual model by Google that enhances embedding quality for Tamil.

### Model Architecture
The architecture consists of:
1. **Generator**: Converts latent vectors and text embeddings into image tensors using convolutional layers with ReLU and Tanh activations.
2. **Discriminator**: Distinguishes between real and generated images using Leaky ReLU and sigmoid activations.

The GAN is trained using an adjusted MINIMAX loss function and **Final Adversarial Loss**. To address issues like **mode collapse**, feature matching using the L1 norm was implemented to ensure diverse image outputs.

### GAN Training
The training process optimizes both the generator and discriminator using the following techniques:
- **GAN Loss**: Used to balance the generator and discriminator.
- **Feature Matching (L1 norm)**: Ensures that the generator produces diverse and realistic outputs.
- **Fréchet Inception Distance (FID)**: Quantitative measure used to evaluate the quality and realism of the generated images.

### Text-to-Image Generation
The trained model converts **Tamil text** into image embeddings via **MuRIL BERT**, and then uses the GAN to generate images that align with the text descriptions.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Scarlet-15/SYNGAN.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the dataset by downloading the **Oxford-102 flower dataset** and placing it in the designated folder.

4. Make sure the pre-trained **MuRIL BERT** model is available for embedding generation.

## Usage

1. **Prepare the Dataset**: 
    - Ensure the Tamil translations of the flower descriptions are available.
    - Convert the descriptions to embeddings using **MuRIL BERT**.

2. **Train the Model**: 
    - Use the following command to train the GAN model:
    ```bash
    python train.py --dataset_path /path/to/dataset --epochs 50 --batch_size 64
    ```

3. **Generate Images**:
    - After training, you can generate images from Tamil text inputs by running:
    ```bash
    python generate.py --text_input "தமிழ் விளக்கம்" --output_dir ./generated_images
    ```

## Training

The training script allows for specifying parameters such as the number of epochs, batch size, and learning rates for both the generator and discriminator. The training loop optimizes both models using **Adam Optimizer** with learning rates of `1e-4`.

### Key Hyperparameters:
- `noise_dim`: Dimension of the noise vector fed to the generator (default: 100).
- `embedding_dim`: Dimension of the Tamil text embeddings (default: 768).
- `image_resolution`: The model is designed for generating **512x512** resolution images.

## Results

### Qualitative Results
Generated images from Tamil text inputs show the ability of **SYN GAN** to create high-quality, realistic representations of flower species described in Tamil.

### Quantitative Results
The **Fréchet Inception Distance (FID)** was used to assess the realism and diversity of the generated images. The model demonstrated competitive performance with a low FID score, indicating high-quality outputs.

## Contributing

We welcome contributions to improve **SYN GAN**. Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

