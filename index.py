import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyD9pXIDsH3O7BWIn1567I0L5mfCLMglIxc")

# Set default parameters
defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}

st.title('Health Information')
st.write('Please ask anything you want to know about health')
final_response = None

# Creating a side panel for inputs
with st.sidebar:
    st.write("## Health Information Settings")
    # Create a text input for the health-related prompt
    health_prompt = st.text_input("Please let me know what specific health topics or information you are interested in")
    # When the 'Generate' button is pressed, generate the text
    if st.button('Generate'):
        formatted_prompt = f"{health_prompt}"

        # Filter only health-related prompts
        health_keywords = ['health', 'medical', 'disease','wellness', 'nutrition', 'lifestyle', 'fitness', 'human']
        if any(keyword in formatted_prompt.lower() for keyword in health_keywords):
            response = genai.chat(
                messages=formatted_prompt
            )
            final_response = response
        else:
            st.warning("Please enter about health (e.g., health, medical, disease, wellness, nutrition, lifestyle, fitness, human).")

if final_response is not None:
    st.write(final_response.last)
