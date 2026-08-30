import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from PIL import Image


# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("GOOGLE_API_KEY is missing. Please add it to your .env file.")
    st.stop()

# Configure Gemini client
client = genai.Client(api_key=api_key)


def get_gemini_response(input_prompt, image):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=[input_prompt, image]
    )

    return response.text


st.set_page_config(page_title="AI Nutritionist")

st.header("AI Nutritionist")

uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "png", "jpeg"]
)

image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image.",
        use_container_width=True
    )


submit = st.button("Tell me about the total calories")


input_prompt = """
You are an expert nutritionist.

Analyze the food items in the provided image.

Identify each food item and estimate its calorie content.

Provide the response in the following format:

1. Food Item - Approximate Calories
2. Food Item - Approximate Calories
3. Food Item - Approximate Calories

Then provide:

- Total estimated calories
- Macronutrient breakdown
- Approximate carbohydrates percentage
- Approximate protein percentage
- Approximate fat percentage
- Fiber information
- Sugar information
- Whether the meal is generally healthy or not
- A short explanation of why

Clearly state that calorie and nutrient values are approximate estimates
and can vary based on portion size and preparation method.
"""


if submit:

    if uploaded_file is None:
        st.warning("Please upload a food image first.")

    else:
        try:
            response = get_gemini_response(
                input_prompt,
                image
            )

            st.header("Nutrition Analysis")

            st.write(response)

        except Exception as e:
            st.error(f"An error occurred: {e}") 