# SYNGAN: Tamil Text-to-Image Synthesis using Generative Adversarial Networks 🎨

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)](https://tensorflow.org/)

SYNGAN is a pioneering framework that bridges the gap between Tamil text descriptions and image generation using state-of-the-art GANs. By leveraging multiple embedding techniques (MURIL, FastText, and GloVe), our model achieves robust text-to-image synthesis for the Tamil language.

[🌐 Live Demo](your-streamlit-app-link) | [📝 Paper](paper-link-if-available) | [🤗 Hugging Face Space](if-available)

![Project Banner or Sample Generated Images](<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300">
  <!-- Background -->
  <rect width="1200" height="300" fill="#f8f9fa"/>
  
  <!-- Decorative network pattern -->
  <g fill="none" stroke="#e9ecef" stroke-width="1">
    <path d="M50,150 C200,50 400,250 600,150 S900,50 1150,150"/>
    <path d="M50,100 C200,0 400,200 600,100 S900,0 1150,100"/>
    <path d="M50,200 C200,100 400,300 600,200 S900,100 1150,200"/>
  </g>

  <!-- Main title text -->
  <text x="100" y="150" font-family="Arial" font-size="72" font-weight="bold" fill="#212529">
    SYNGAN
  </text>
  
  <!-- Subtitle -->
  <text x="100" y="190" font-family="Arial" font-size="24" fill="#495057">
    Tamil Text-to-Image Synthesis
  </text>

  <!-- Tamil script symbol -->
  <text x="500" y="160" font-family="Arial" font-size="48" fill="#7048e8">
    த
  </text>

  <!-- Right side elements -->
  <!-- Flower representation -->
  <g transform="translate(800, 150)">
    <path d="M0,0 C20,-20 40,-20 60,0 C80,-20 100,-20 120,0 C120,20 100,40 80,40 C60,40 40,40 20,40 C0,40 -20,20 0,0" 
          fill="#ff922b" fill-opacity="0.6"/>
    <path d="M60,0 C80,-20 100,-20 120,0 C140,-20 160,-20 180,0 C180,20 160,40 140,40 C120,40 100,40 80,40 C60,40 40,20 60,0" 
          fill="#f06595" fill-opacity="0.6"/>
  </g>

  <!-- GAN representation -->
  <g transform="translate(950, 100)">
    <!-- Generator -->
    <rect x="0" y="0" width="80" height="40" rx="5" fill="#339af0" fill-opacity="0.8"/>
    <text x="40" y="25" font-family="Arial" font-size="12" fill="white" text-anchor="middle">Generator</text>
    
    <!-- Discriminator -->
    <rect x="100" y="0" width="80" height="40" rx="5" fill="#ff6b6b" fill-opacity="0.8"/>
    <text x="140" y="25" font-family="Arial" font-size="12" fill="white" text-anchor="middle">Discriminator</text>
    
    <!-- Connecting arrows -->
    <path d="M85,20 L95,20" stroke="#495057" stroke-width="2" marker-end="url(#arrowhead)"/>
  </g>

  <!-- Arrow marker definition -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#495057"/>
    </marker>
  </defs>

  <!-- Embedding model names -->
  <g font-family="Arial" font-size="14" fill="#868e96">
    <text x="700" y="250">MURIL • FastText • GloVe</text>
  </g>
</svg>)

## ✨ Key Features

- 🌟 Multi-embedding approach using MURIL, FastText, and GloVe
- 🖼️ High-resolution image generation (512x512)
- 📊 Comprehensive evaluation metrics and analysis
- 🚀 Easy-to-use Streamlit web interface
- 🔄 Support for both proofread and unproofread datasets

## 🏗️ Architecture

![Model Architecture](path-to-architecture-diagram)

### Components:
- **Text Encoder**: Utilizes three embedding models:
  - MURIL (Multilingual Representations for Indian Languages)
  - FastText
  - GloVe
- **Generator**: Transforms noise vectors and text embeddings into images
- **Discriminator**: Validates image authenticity

## 📊 Performance Metrics

### Comparative Analysis

| Model Configuration | FID Score | Inception Score |
|--------------------|-----------|-----------------|
| MURIL (Proofread)  | X.XX      | X.XX           |
| FastText (Proofread)| X.XX     | X.XX           |
| GloVe (Proofread)  | X.XX      | X.XX           |
| MURIL (Unproofread)| X.XX      | X.XX           |
| FastText (Unproofread)| X.XX   | X.XX           |
| GloVe (Unproofread)| X.XX      | X.XX           |

### Loss Curves
<details>
<summary>Click to view loss curves</summary>

#### MURIL Configuration
![MURIL Loss Curves](path-to-muril-loss-curves)

#### FastText Configuration
![FastText Loss Curves](path-to-fasttext-loss-curves)

#### GloVe Configuration
![GloVe Loss Curves](path-to-glove-loss-curves)
</details>

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/YourUsername/SYNGAN.git
cd SYNGAN

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Download Pre-trained Models
```python
# Example code for downloading and setting up models
from transformers import AutoModel
muril = AutoModel.from_pretrained("google/muril-base-cased")
```

### Training
```python
# Example training command
python train.py --config configs/default.yaml
```

## 📁 Repository Structure
```
SYNGAN/
├── configs/
│   └── default.yaml
├── data/
│   ├── embeddings/
│   │   ├── proofread/
│   │   └── unproofread/
│   └── metrics/
├── models/
│   ├── generator.py
│   └── discriminator.py
├── notebooks/
│   └── analysis.ipynb
├── app/
│   └── streamlit_app.py
├── requirements.txt
└── README.md
```

## 📊 Experimental Results

### Sample Generations
![Sample Generated Images](path-to-sample-images)

### Detailed Metrics
Our comprehensive evaluation includes:
- FID Scores
- Inception Scores
- Loss Analysis
- Quality Assessments

Full metrics and analysis can be found in our [detailed results](path-to-metrics-file).

## 🌟 Demo Application

Try our Streamlit-based demo application:
- 🔗 [Live Demo](your-streamlit-app-link)
- Features:
  - Real-time image generation from Tamil text
  - Multiple embedding model options
  - Result comparison

## 🤝 Contributing

We welcome contributions! Please check our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Oxford 102 Flowers Dataset team
- Google's MURIL team
- FastText and GloVe developers
- [Add any other acknowledgments]

## 📫 Contact

- Your Name - [Your Email]
- Project Link: [https://github.com/YourUsername/SYNGAN](https://github.com/YourUsername/SYNGAN)
