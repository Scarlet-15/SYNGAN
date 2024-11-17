
# **SYNGAN: Tamil Text-to-Image Synthesis using GANs** 🎨  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) [![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/) [![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)](https://tensorflow.org/)

**SYNGAN** bridges the gap between Tamil text descriptions and image generation using advanced Generative Adversarial Networks (GANs). Leveraging state-of-the-art embeddings like MURIL, FastText, and GloVe, SYNGAN is tailored to synthesize high-quality images from Tamil text inputs.
![Banner](https://github.com/Scarlet-15/SYNGAN/blob/main/Assets/Banner.svg)

[🌐 **Live Demo**](your-streamlit-app-link)

---

## **✨ Features**
- Multi-embedding support: **MURIL**, **FastText**, **GloVe**  
- Size of Image Generated (64x64x3)  
- Intuitive web interface with **Streamlit**  
- Supports both proofread and unproofread datasets  

---

## **🏗️ Architecture Overview**
**Core Components**:
1. **Text Encoder**: Processes Tamil text into embeddings using MURIL, FastText, and GloVe.  
2. **Generator**: Creates images from text embeddings and noise vectors.  
3. **Discriminator**: Validates generated images against real samples.  

![Architecture Diagram](https://github.com/Scarlet-15/SYNGAN/blob/main/Assets/Project%20Flow.png)


---

## **🧬 Generator and Discriminator Architecture**
<p align="center">
  <img src="https://img.icons8.com/color/48/000000/artificial-intelligence.png" alt="AI Icon" width="40">
</p>

### **Generator Architecture**
![Generator Architecture](https://github.com/Scarlet-15/SYNGAN/blob/main/Assets/Generator.png)

### **Discriminator Architecture**
![Discriminator Architecture](https://github.com/Scarlet-15/SYNGAN/blob/main/Assets/Discriminator.png)


## **📊 Key Metrics**

| Model                | FID Score | Inception Score (Mean ± Std)           
|----------------------|-----------|-------------------------------|  
| MURIL Proofread      | 11.5919   | 31282540.0000 ± 29133.0       |  
| FastText Proofread   | 12.4062   | 7186333.5000 ± 12192.0        |  
| GloVe Proofread      | 29.2469   | 299437890.0000 ± 544659.00    |  
| MURIL UnProofread    | 49.1608   | 3757548964009724.0000 ± inf   |  
| FastText UnProofread | 7.3187    | 1542239.7500 ± 444679.5625    |  
| GloVe UnProofread    | 7.5565    | 29722342.0000 ± 21500020.000  | 

---

## **🚀 Quick Start**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Scarlet-15/SYNGAN.git
   cd SYNGAN
   ```
---

## **📁 Repository Structure**
```
SYNGAN/
├── GAN_Trained_Modes/           # Zip files of all embeddings generated
├── Results/                     # Loss Graphs and Results
├── Assets/                      # Architecture Diagrams
├── app.py                       # Streamlit application
├── Final_Results.ipynb          # Model code for steamlit application
└── README.md                    # Project overview
```

---

## **🌟 Demo**
Explore the live demo: [**Streamlit App**](your-streamlit-app-link)  
Features include real-time Tamil text-to-image synthesis and model comparison.

---


## **📜 License**
Licensed under the [MIT License](LICENSE).

---

## **📫 Contact**


- <img src="https://img.icons8.com/ios-filled/50/000000/gmail.png" alt="Email Icon" width="20"> [Harinee J](mailto:harinee.j2021@vitstudent.ac.in)  
- <img src="https://img.icons8.com/ios-filled/50/000000/gmail.png" alt="Email Icon" width="20"> [Mhanjhusriee B](mailto:mhanjhusriee.b2021@vitstudent.ac.in)  
- <img src="https://img.icons8.com/ios-filled/50/000000/gmail.png" alt="Email Icon" width="20"> [Srinidhi K](mailto:srinidhi.k2021@vitstudent.ac.in)


