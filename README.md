# AI Image Generator

## 📂 Project Structure

```text
IMAGE GENERATOR/
│── backend/
│   ├── database.py
│   ├── generator.py
│   ├── images.db
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── requirements.txt
│   └── generated_images/
│
│── image-generator/
│
│── app.py
│── apikey.py
│── .env
│── .gitignore
│── run_all.bat
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/MisterSRINIVASAN/IMAGE-GENERATOR.git
cd IMAGE-GENERATOR
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

#### Backend

```bash
cd backend
pip install -r requirements.txt
```

#### Frontend

```bash
cd ..
pip install streamlit requests
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
HUGGINGFACE_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

### Start Backend

```bash
cd backend
uvicorn main:app --reload
```

### Start Frontend

```bash
cd ..
streamlit run app.py
```

### OR (run everything)

```bash
run_all.bat
```

---

## 📸 How It Works

1. User enters a text prompt  
2. Frontend sends request to backend  
3. Backend calls AI model API  
4. Image is generated and stored  
5. Result is displayed to user  

---

## ⚠️ Important Notes

- Do NOT upload `.env` file  
- Add `venv/`, `__pycache__/`, `*.db` to `.gitignore`  
- Ensure backend runs before frontend  

---

## 🔮 Future Enhancements

- Multiple AI models  
- Image style customization  
- Download option  
- Cloud deployment  

---

## 🤝 Contributing

Feel free to fork and improve this project.

---

## 📜 License

MIT License  

---

## 👨‍💻 Author

**Srinivasan Balaji**  
Full Stack & AI Developer 🚀
