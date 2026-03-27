# 🌟 Lumina AI - Intelligent Image Generator

<div align="center">
  <p><strong>A powerful, full-stack AI image generation application powered by Stable Diffusion and FastAPI.</strong></p>
</div>

---

## 📖 Overview

**Lumina AI** is a state-of-the-art web application that bridges the gap between imagination and reality. By leveraging advanced Machine Learning models (Stable Diffusion), it allows users to generate high-quality images directly from text prompts. 

This project is built with a modern, decoupled full-stack architecture—ensuring high performance on the backend while providing a snappy, interactive user experience on the frontend. Every image generated is seamlessly saved to a local database, allowing users to revisit their past creations in a beautiful gallery format.

---

## 🚀 Tech Stack Actually Used

Lumina AI is engineered using a robust and modern technology stack:

### **Frontend (User Interface)**
- **React.js**: Powers the interactive, component-based user interface.
- **HTML5 & CSS3**: For styling and layout.
- **Node.js & npm**: Handles frontend dependencies and scripts.

### **Backend (API & Database)**
- **FastAPI**: A blazing-fast, modern Python web framework used for building the backend REST APIs.
- **Uvicorn**: The lightning-fast ASGI server that serves the FastAPI application.
- **SQLAlchemy**: The Object Relational Mapper (ORM) for managing SQLite database records cleanly and efficiently.
- **SQLite**: A lightweight, disk-based database used to store image generation history (prompts, file paths, metadata).

### **AI & Machine Learning Engine**
- **Hugging Face Diffusers**: The core library used to load and run the Stable Diffusion image generation pipeline.
- **PyTorch & Accelerate**: Deep learning frameworks utilized for executing tensor operations and optimizing AI model inference on CPU/GPU.
- **Transformers**: For text processing and tokenization required by the Stable Diffusion pipeline.

*(Note: There is also an alternative legacy Streamlit frontend located in `app.py`)*

---

## 📂 Project Structure

```text
IMAGE-GENERATOR/
│
├── backend/                  # The FastAPI Backend System
│   ├── database.py           # Database connection & engine setup
│   ├── generator.py          # AI logic (Stable Diffusion pipeline)
│   ├── main.py               # FastAPI application & REST endpoints
│   ├── models.py             # SQLAlchemy database models
│   ├── schemas.py            # Pydantic validation schemas
│   ├── requirements.txt      # Python dependencies
│   ├── images.db             # SQLite database (auto-generated)
│   └── generated_images/     # Folder where AI-generated images are saved
│
├── image-generator/          # The React Frontend Application
│   ├── public/               # Static assets
│   ├── src/                  # React components and styles
│   └── package.json          # Node.js dependencies
│
├── app.py                    # Alternative Streamlit UI (Legacy)
├── run_all.bat               # Master script to launch all services on Windows
└── README.md                 # Project documentation
```

---

## ⚙️ How It Works (Architecture)

1. **User Input:** The user types a creative text prompt into the React frontend.
2. **API Request:** The React app sends an asynchronous HTTP POST request to the FastAPI backend.
3. **AI Generation:** The backend receives the prompt, initializes the Stable Diffusion pipeline via Hugging Face `diffusers`, and generates the image.
4. **Storage:** The generated image is saved locally in the `generated_images/` directory. Simultaneously, a record containing the prompt, file path, and timestamps is saved to the SQLite database.
5. **Response & Render:** The backend sends the image URL/metadata back to the React app, which seamlessly renders the newly created masterpiece in the user's gallery.

---

## 🛠️ Installation & Setup

### Prerequisites
- **Python 3.8+**
- **Node.js & npm**
- *(Optional but recommended)* A CUDA-compatible GPU for faster AI image generation.

### 1. Clone the repository
```bash
git clone https://github.com/MisterSRINIVASAN/IMAGE-GENERATOR.git
cd IMAGE-GENERATOR
```

### 2. Environment Setup (Optional for cloud APIs)
If you are using cloud-based Hugging Face models, create a `.env` file in the root directory:
```env
HUGGINGFACE_API_KEY=your_api_key_here
```

### 3. Run the Application (The Easy Way)
For Windows users, simply double-click or run the included batch script. This will automatically install dependencies and launch both the backend and frontend servers!
```cmd
run_all.bat
```

### 4. Manual Startup

**Start the Backend (FastAPI)**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
# API runs on http://localhost:8000
```

**Start the Frontend (React)**
```bash
cd image-generator
npm install
npm start
# React App runs on http://localhost:3000
```

---

## 🔮 Future Enhancements
- 🧠 **Multiple AI Models:** Support for SDXL or external APIs (e.g., Midjourney/OpenAI).
- 🎨 **Image Style Customization:** Add dropdowns for specific styles (e.g., "Cyberpunk", "Anime", "Photorealistic").
- ☁️ **Cloud Deployment:** Migrate database to PostgreSQL and host on AWS/Vercel/Render.
- 💾 **Download & Share:** Allow users to directly download or share generated images to social networks.

---

## 👨‍💻 Author

**Srinivasan Balaji**  
*Full Stack Developer & AI Enthusiast* 🚀  
Building intelligent applications for the modern web.

---
## 📜 License
This project is licensed under the MIT License.
