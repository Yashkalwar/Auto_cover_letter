# Auto_cover_letter
AutoCoverLetter: AI-Powered Cover Letter Generator

📌 Overview

AutoCoverLetter is a Python-based automation tool that generates personalized and professional cover letters using AI. It extracts key details from your resume and a job description to craft a tailored cover letter, helping you stand out in your job applications.

✨ Features

📄 Extracts text from a PDF resume.

🔍 Fetches and parses job descriptions from provided URLs.

🤖 Uses Mistral 7B via LM Studio to generate high-quality cover letters.

🎯 Highlights relevant technical skills from the job description.

💾 Saves generated cover letters and technical terms for future use.

🛠️ Requirements

Python 3.8+

Required Python packages:

pip install requests PyPDF2 beautifulsoup4

LM Studio running locally with the Mistral 7B model.

🚀 Usage

1️⃣ Run the script:

python autocover_letter.py

2️⃣ Follow the prompts:

Enter the path to your PDF resume (or use the default path).

Enter the job posting URL.

3️⃣ Outputs:

Cover Letter: Saved as cover_letter.txt

Technical Skills Extracted: Saved as technical_terms.txt

🔧 Configuration

Modify the following constants if needed:

LM_STUDIO_API_URL = "http://localhost:1234/v1/chat/completions"  # LM Studio API URL
MODEL_NAME = "mistral"  # Model name loaded in LM Studio

📚 How It Works

Extract Resume Data: Reads text from the provided PDF.

Fetch Job Description: Scrapes the job listing webpage for relevant details.

Generate Cover Letter: Uses AI to tailor a professional and engaging letter.

Extract Technical Terms: Identifies and saves key skills from the job description.

❗ Notes

Ensure LM Studio is running locally with Mistral 7B loaded.

Job description extraction relies on HTML parsing, so some job pages may not be fully supported.

The generated cover letter should be reviewed and customized before submission.

💡 Future Enhancements

✅ Support for more AI models (GPT, LLaMA, etc.).

✅ Improved job description parsing for various websites.

✅ Enhanced AI prompts for even more personalized letters.

📝 License

This project is open-source and available under the MIT License.

🙌 Contributions

Feel free to contribute! Submit issues, suggest features, or fork and improve the project.

🎯 Created by Yash Kalwar | 📍 Master's in AI at King's College London
