
# **SYNGAN: Tamil Text-to-Image Synthesis using GANs** 🎨  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)  
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)  
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)](https://tensorflow.org/)  

**SYNGAN** bridges the gap between Tamil text descriptions and image generation using advanced Generative Adversarial Networks (GANs). Leveraging state-of-the-art embeddings like MURIL, FastText, and GloVe, SYNGAN is tailored to synthesize high-quality images from Tamil text inputs.

[🌐 **Live Demo**](your-streamlit-app-link) | [📝 **Paper**](paper-link-if-available)  

---

## **✨ Features**
- Multi-embedding support: **MURIL**, **FastText**, **GloVe**  
- High-resolution image generation (512x512)  
- Intuitive web interface with **Streamlit**  
- Supports both proofread and unproofread datasets  

---

## **🏗️ Architecture Overview**
**Core Components**:
1. **Text Encoder**: Processes Tamil text into embeddings using MURIL, FastText, and GloVe.  
2. **Generator**: Creates images from text embeddings and noise vectors.  
3. **Discriminator**: Validates generated images against real samples.  

![Architecture Diagram](path-to-architecture-diagram)

---

## **📊 Key Metrics**
| Model            | FID Score | Inception Score |  
|-------------------|-----------|-----------------|  
| MURIL Proofread   | X.XX      | X.XX            |  
| FastText Proofread| X.XX      | X.XX            |  
| GloVe Proofread   | X.XX      | X.XX            |  

For detailed analysis and loss curves, refer to our [report](path-to-metrics-file).  

---

## **🚀 Quick Start**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourUsername/SYNGAN.git
   cd SYNGAN
   ```
2. **Set up environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Run the demo**:
   ```bash
   streamlit run app/streamlit_app.py
   ```

---

## **📁 Repository Structure**
```
SYNGAN/
├── configs/           # Configuration files
├── data/              # Dataset & embeddings
├── models/            # Generator & Discriminator
├── app/               # Streamlit application
├── requirements.txt   # Dependencies
└── README.md          # Project overview
```

---

## **🌟 Demo**
Explore the live demo: [**Streamlit App**](your-streamlit-app-link)  
Features include real-time Tamil text-to-image synthesis and model comparison.

---

## **🤝 Contributing**
We welcome contributions!  
- Fork this repository  
- Make your changes  
- Open a pull request  

See our [Contributing Guidelines](CONTRIBUTING.md) for details.

---

## **📜 License**
Licensed under the [MIT License](LICENSE).

---

## **📫 Contact**
- **Your Name**: [Your Email]  
- **GitHub**: [SYNGAN Repository](https://github.com/YourUsername/SYNGAN)
