import requests
import PyPDF2  
from bs4 import BeautifulSoup  
# === CONFIGURATION ===
LM_STUDIO_API_URL = "http://localhost:1234/v1/chat/completions"  # LM Studio API URL
MODEL_NAME = "mistral"  # Ensure this matches the model loaded in LM Studio

# === 1️⃣ FUNCTION: LOAD RESUME FROM PDF FILE ===
def load_pdf_resume(file_path):
    """Reads the PDF resume file as text."""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()  # Extract text from each pagea
    return text

# === 2️⃣ FUNCTION: CONNECT TO MISTRAL 7B VIA LM STUDIO ===
def query_mistral(prompt):
    """Sends a request to the locally running Mistral 7B model."""
    headers = {"Content-Type": "application/json"}
    payload = {
    "model": MODEL_NAME,
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.5,
    "max_tokens": 500  # Reduce response size for faster generation
}

    response = requests.post(LM_STUDIO_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

def generate_cover_letter(resume_text, job_description):
    """Generates a customized, professional, and human-like cover letter based on the resume and job description."""
    
    prompt = f"""
    I am applying for a job, and I want to craft a compelling cover letter tailored to the role. Below is my resume in PDF foramt:

    ---- RESUME START ----
    {resume_text}
    ---- RESUME END ----

    The job description for the position is:
    {job_description}

    Please generate a **professional, engaging, and personalized** cover letter that:
    - Captures my enthusiasm for the role and the company.
    - Highlights my most **relevant skills, achievements, and experiences** based on the job description.
    - Uses **a natural, confident, and engaging tone**, avoiding generic phrases.
    - Is **concise and well-structured**, fitting within one page.
    - Incorporates relevant **keywords** from the job description in a seamless, meaningful way.
    - Starts with a **strong, attention-grabbing opening**.
    - Ends with a **persuasive closing paragraph**, expressing eagerness for an interview and appreciation for their time.
    - Uses my name, **Yash Kalwar**, in the closing.
    - I am currently doing my msater in AI from king's college london , first job in amdocs , second in Brainywood currently not working anywhere
    Return **only** the complete cover letter text, without any explanations or formatting tags.
    """

    return query_mistral(prompt)


def save_cover_letter(cover_letter_text):
    """Saves the generated cover letter into a text file."""
    with open("cover_letter.txt", "w", encoding="utf-8") as file:
        file.write(cover_letter_text)

    print("✅ Cover letter saved as: cover_letter.txt")


def parse_job_description(job_link):
    """Fetches and parses the job description from the provided job portal link."""
    response = requests.get(job_link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for common keywords in headings and paragraphs
        keywords = ["job description", "responsibilities", "requirements", "qualifications", "Roles and Responsibilities",
                     "Who We're Looking For", "Experience & Skills", "About the role"]
        job_description = ""

        # Search for relevant sections
        for keyword in keywords:
            section = soup.find(text=lambda text: text and keyword in text.lower())
            if section:
                # Get the parent element and extract text
                job_description = section.find_parent().get_text(strip=True)
                break  # Stop after finding the first relevant section

        if not job_description:
            raise Exception("Job description not found on the page.")
        
        return job_description
    else:
        raise Exception(f"Error fetching job description: {response.status_code}")

# === 8️⃣ FUNCTION: EXTRACT TECHNICAL TERMS ===
def extract_technical_terms(job_description):
    """Extracts important technical terms from the job description."""
    # Define a list of technical terms to look for
    technical_terms = [
    # Programming Languages
            "Python", "R", "Java", "Scala", "C++", "SQL", "NoSQL", "Julia", 

            # Data Processing & ETL
            "Apache Spark", "Hadoop", "Kafka", "Flink", "Airflow", "ETL", "Data Pipelines", 

            # Databases & Data Storage
            "PostgreSQL", "MySQL", "MongoDB", "Cassandra", "Redshift", "BigQuery", "Snowflake", "Elasticsearch",

            # Machine Learning & AI
            "Machine Learning", "Deep Learning", "Reinforcement Learning", "Supervised Learning", 
            "Unsupervised Learning", "Transfer Learning", "Neural Networks", "Computer Vision", 
            "Natural Language Processing", "Generative AI", "Large Language Models", "LLMs", "GPT", 
            "Transformers", "AutoML", "Hyperparameter Tuning",

            # ML & AI Frameworks
            "TensorFlow", "PyTorch", "Keras", "Scikit-Learn", "XGBoost", "LightGBM", "Hugging Face", 

            # Data Science & Analytics
            "Data Science", "Statistics", "Exploratory Data Analysis", "Feature Engineering", 
            "Data Visualization", "Pandas", "NumPy", "Matplotlib", "Seaborn", "Scipy", "Dask", "Plotly",

            # Cloud Computing & DevOps
            "AWS", "Azure", "GCP", "Docker", "Kubernetes", "Terraform", "CI/CD", "MLflow", "Kubeflow",

            # Software Development & APIs
            "REST API", "GraphQL", "FastAPI", "Flask", "Django", "Streamlit", "LangChain",

            # Big Data & Distributed Computing
            "MapReduce", "Hive", "HBase", "Delta Lake", "Parquet", "ORC", 

            # Experimentation & A/B Testing
            "A/B Testing", "Bayesian Methods", "Multivariate Testing",

            # Data Governance & Engineering
            "Data Modeling", "Data Warehousing", "Data Governance", "Data Lineage", "Data Quality",

            # Optimization & Mathematics
            "Optimization", "Linear Algebra", "Calculus", "Probability", "Bayesian Statistics",

            # Others
            "MLOps", "DataOps", "Reproducibility", "Explainable AI (XAI)", "Fairness in AI"] 
            
    found_terms = [term for term in technical_terms if term.lower() in job_description.lower()]
    
    return found_terms

# === 7️⃣ MAIN EXECUTION ===
if __name__ == "__main__":
    # Ask for the path to your resume, with a default value
    resume_path = input("Enter the path to your PDF resume file (default: D:\\PYTHON\\AutoCover_letter\\Resume.pdf): ") or "D:\\PYTHON\\AutoCover_letter\\Resume.pdf"
    
    # Load resume (PDF format)
    resume_text = load_pdf_resume(resume_path)

    # Ask for job portal link
    job_link = input("Enter the job portal link for the job description: ")

    # Parse job description from the link
    job_description = parse_job_description(job_link)

    # Generate the cover letter
    print("⏳ Generating cover letter...")
    generated_cover_letter = generate_cover_letter(resume_text, job_description)

    # Extract and save technical terms
    technical_terms = extract_technical_terms(job_description)
    with open("technical_terms.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(technical_terms))

    # Save outputs
    save_cover_letter(generated_cover_letter)
    # save_updated_resume(resume_text)  # Removed this line

    print("\n🎉 Done! Your cover letter is ready.")
