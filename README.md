# AI Nutritionist

# 🥗 AI Nutritionist

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange)

AI Nutritionist is a simple web application that uses **Google Gemini** to analyze food images and provide an estimated nutritional breakdown.

## Features
- Upload an image of food items.
- Uses Google Gemini AI to analyze the image and extract nutritional data.
- Provides calorie estimates for each food item.
- Offers a macronutrient breakdown (carbohydrates, fats, fibers, sugar, etc.).
- Determines whether the meal is healthy or not.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-nutritionist.git
   cd ai-nutritionist
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your API key:
   - Create a `.env` file in the project directory.
   - Add the following line, replacing `your_api_key` with your Google Gemini API key:
     ```
     GOOGLE_API_KEY=your_api_key
     ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Upload an image of a food item.
3. Click the **Tell me about the total calories** button.
4. View the nutritional breakdown and health analysis.

## Example Output
**Input: <img width="764" height="476" alt="image" src="https://github.com/user-attachments/assets/bbbbe7d2-306e-41ae-9d48-9edfdac76e97" />


**Generated Response:**
```
1. Rice - 200 calories
2. Chicken - 250 calories
3. Vegetables - 100 calories
---
Total Calories: 550 kcal
The meal is balanced with 50% carbohydrates, 30% protein, and 20% fats.
This is a healthy meal.
```

## Dependencies
- Python 3.7+
- Streamlit
- Google Generative AI SDK
- Python-dotenv
- Pillow

## Contributing
Feel free to submit pull requests or raise issues to improve the project.

## License
This project is licensed under the MIT License.

## Author
[Nandan](https://github.com/your-username)
