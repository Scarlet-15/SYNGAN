import streamlit as st
import tensorflow as tf
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch
from PIL import Image
import io
import base64

# Initialize session state variables at the very beginning
if 'generator_initialized' not in st.session_state:
    st.session_state.generator_initialized = False
if 'generator' not in st.session_state:
    st.session_state.generator = None

class TamilTextToImage:
    def __init__(self, generator_path="Model_glove_raw_500/generator_epoch_final.h5"):
        """Initialize the Tamil text to image generator"""
        try:
            self.generator = tf.keras.models.load_model(generator_path)
            self.tokenizer, self.muril_model = self.load_muril_model()
        except Exception as e:
            st.error(f"Error initializing models: {str(e)}")
            raise e

    @staticmethod
    def load_muril_model():
        """Load MuRIL tokenizer and model"""
        tokenizer = AutoTokenizer.from_pretrained("google/muril-base-cased")
        model = AutoModel.from_pretrained("google/muril-base-cased")
        return tokenizer, model

    def get_text_embeddings(self, text, target_dim=50):
        """Generate embeddings for Tamil text and resize by truncation or padding."""
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
        
        with torch.no_grad():
            outputs = self.muril_model(**inputs)
            embeddings = outputs.last_hidden_state[:, 0, :].numpy()

        # Adjust embedding size to match `target_dim`
        if embeddings.shape[1] > target_dim:
            reduced_embeddings = embeddings[:, :target_dim]
        else:
            padding = np.zeros((embeddings.shape[0], target_dim - embeddings.shape[1]))
            reduced_embeddings = np.concatenate([embeddings, padding], axis=1)

        return reduced_embeddings

    def generate_image(self, text_embedding, latent_dim=100):
        """Generate image from text embedding"""
        noise = np.random.normal(0, 1, (1, latent_dim))
        generator_input = np.concatenate([noise, text_embedding], axis=1)
        
        generated_image = self.generator.predict(generator_input)
        generated_image = ((generated_image + 1) * 127.5).astype(np.uint8)

        return generated_image[0]

    def text_to_image(self, tamil_text):
        """Convert Tamil text to image"""
        try:
            embeddings = self.get_text_embeddings(tamil_text)
            image_array = self.generate_image(embeddings)
            return Image.fromarray(image_array)
        except Exception as e:
            raise Exception(f"Error generating image: {str(e)}")

def get_image_download_link(img, filename="generated_image.png"):
    """Generate a download link for the image"""
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/png;base64,{img_str}" download="{filename}">Download Generated Image</a>'
    return href

def initialize_generator():
    """Initialize the generator and store in session state"""
    try:
        with st.spinner("Loading models... Please wait..."):
            generator = TamilTextToImage()
            st.success("Models loaded successfully!")
            return generator
    except Exception as e:
        st.error(f"Failed to initialize generator: {str(e)}")
        return None

def main():
    # Page config
    st.set_page_config(page_title="Tamil Text to Image Generator", layout="wide")

    # Title and description
    st.title("Tamil Text to Image Generator")
    st.markdown("""
    Generate images from Tamil text using MuRIL embeddings and a trained GAN model.
    Type your Tamil text in the chat box below!
    """)

    # Initialize generator if not already done
    if not st.session_state.generator_initialized:
        generator = initialize_generator()
        if generator is not None:
            st.session_state.generator = generator
            st.session_state.generator_initialized = True
        else:
            st.error("Failed to initialize models. Please refresh the page.")
            return

    # Input form
    with st.form(key='message_form'):
        user_input = st.text_area("Type your Tamil text here:", 
                                  height=100, 
                                  placeholder="உங்கள் தமிழ் உரையை இங்கே தட்டச்சு செய்யவும்...")
        submit_button = st.form_submit_button("Generate Image")
        
        if submit_button and user_input:
            if st.session_state.generator is not None:
                try:
                    # Generate image from user input
                    with st.spinner('Generating image...'):
                        generated_image = st.session_state.generator.text_to_image(user_input)

                    # Display the generated image
                    st.image(generated_image, caption="Generated Image", use_column_width=True)

                    # Display download link
                    st.markdown(get_image_download_link(generated_image), unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"Error generating image: {str(e)}")
            else:
                st.error("Generator not initialized. Please refresh the page.")

    # Sidebar with additional options
    with st.sidebar:
        st.header("About")

        # About section
        st.markdown("---")
        st.markdown("""
        This application uses:
        - MuRIL embeddings for Tamil text processing
        - GAN for image generation
        - Streamlit for the user interface

        ### Instructions
        1. Type Tamil text in the chat box
        2. Click 'Generate Image'
        3. Download the generated image using the link below it

        """)

if __name__ == "__main__":
    main()
