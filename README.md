## **🧠 Intelligent Arabic Question Answering System** 

This project implements both Generative and Extractive Arabic Question Answering (QA) systems on content scraped from the Arabic sports news website FilGoal
.
Users can ask natural-language questions in Arabic and receive accurate, context-aware answers directly derived from FilGoal articles.

# **📘 Project Overview**

The system processes Arabic news articles, cleans and indexes them, retrieves the most relevant passages, and then uses two different QA approaches:

- **🟩 Extractive QA** – using **Arabic BERT** (asafaya/bert-base-arabic) to locate the most relevant span of text from FilGoal content that answers the question.

- **🟦 Generative QA** – using **AraGPT2** (aubmindlab/aragpt2-base) to generate fluent, context-aware answers in natural Arabic.

Together, they form a **hybrid Arabic Question Answering framework** that combines retrieval-based accuracy with natural language fluency.

# **Implementation Steps**
**1. Data Collection** 

- **Web Scraping:** Articles were scraped from FilGoal using requests and BeautifulSoup.

- **HTML Parsing:** Extracted text from <p>, <h1–h6>, and <li> tags while removing scripts, ads, and irrelevant HTML.

**2. Preprocessing**

- **Text Cleaning:** Removed HTML tags, special characters, and extra spaces.

- **Chunking:** Split long articles into smaller, manageable text segments.

- **Metadata:** Stored article titles, URLs, and timestamps for better context retrieval.

**3. Retrieval**

**Techniques Used:**

- 🔹 BM25 (via rank_bm25) for keyword-based ranking.

- 🔹 FAISS for dense semantic similarity search.

Retrieves the **top-k** relevant text chunks for each user query.

**4. Answer Generation**
**🟩 Extractive Model**

- **Model:** asafaya/bert-base-arabic

- **Approach:** Identifies and extracts the most relevant text span answering the question.

**🟦 Generative Model**

- **Model:** aubmindlab/aragpt2-base

- **Approach:** Generates a natural Arabic answer based on the question and retrieved context.
# **Example Usage**
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("aubmindlab/aragpt2-base")
model = AutoModelForCausalLM.from_pretrained("aubmindlab/aragpt2-base")
qa_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

question = "من فاز في مباراة الأهلي والزمالك الأخيرة؟"
context = "الأهلي فاز على الزمالك بثلاثة أهداف مقابل هدف في الدوري المصري الممتاز..."
response = qa_pipeline(f"سؤال: {question}\nسياق: {context}\nإجابة:", max_length=100)
print(response[0]["generated_text"])  
# **🚀 Deployment**

Built as a REST API using Flask.
It accepts an Arabic question and returns either:

- **✅ Extracted answer** (from Arabic BERT)

- **💬 Generated answer** (from AraGPT2)

# **🧠 Future Improvements**

- Fine-tune AraGPT2 and Arabic BERT on Arabic QA datasets (e.g., Arabic-SQuAD).

- Integrate context summarization for long articles.

- Build a web interface for interactive Arabic QA.
 # **🧩 Tech Stack**
**Component**	                   **Library / Tool**
**🕸️ Scraping**                    BeautifulSoup, requests
**🤖 NLP**	                       Transformers (Hugging Face), PyTorch
**🔍 Retrieval**	                  rank_bm25, FAISS
**🧪 Evaluation**	                evaluate, datasets
**🌐 Deployment**                   Flask / FastAPI (optional)
# **✅ Summary**
This project demonstrates a dual-model Arabic QA system combining extractive reasoning (Arabic BERT) and generative fluency (AraGPT2) to deliver contextually rich answers from real-world Arabic sports news.

