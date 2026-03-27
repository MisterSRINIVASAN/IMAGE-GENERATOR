<div align="center">
  <h1>🌟 Lumina AI 🌟<br/>React Frontend Interface</h1>
  <p><strong>The modern, interactive, and beautifully styled user interface for the Lumina AI Image Generator.</strong></p>
  
  <p>
    <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React" />
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
    <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js" />
  </p>
</div>

---

> [!NOTE]
> This is the React frontend portion of the Lumina AI project.
> For full full-stack project documentation (including FastAPI Backend and AI engine), please see the [Main README](../README.md) in the root directory.

## 📖 Overview

This directory contains the **React.js Frontend** for Lumina AI. It provides a highly responsive, visually appealing, and snappy interactive experience, bridging the gap between the user's creative ideas and the powerful Stable Diffusion backend.

With a focus on modern UI/UX principles, the application utilizes dynamic glassmorphism aesthetics, fluid micro-animations, and a seamless asynchronous flow for generating and viewing images.

---

## ✨ Interface Features

- **Real-time Generation Feedback:** Intuitive loading states and progress indicators while the AI works on the image.
- **Masonry Image Gallery:** A beautiful, Pinterest-style responsive grid layout to showcase generated images.
- **Dynamic Theming:** Deep integration of modern CSS patterns including dark mode aesthetics, vibrant gradients, and hover effects.
- **Favorites Management:** Heart and un-heart your top generations.
- **Delete Support:** Remove unwanted generations instantly from the UI and backend.

---

## 🚀 Tech Stack Details

- **React (Create React App):** For robust component lifecycle management and state handling.
- **Axios / Fetch:** For handling asynchronous HTTP POST/GET requests to the FastAPI backend.
- **Vanilla CSS3:** 
  - Utilizing `flexbox` and `CSS grid` for intricate layouts.
  - Employing CSS Custom Properties (variables) for consistent theming.
  - Using keyframe animations to enhance interactivity.
- **Lucide Icons / React Icons:** (If applicable) for scalable vector graphics and UI elements.

---

## 📂 Frontend Structure

```text
image-generator/
│
├── public/                 # Static public assets (favicon, index.html)
│
├── src/                    # Main source code directory
│   ├── components/         # Reusable React components
│   │   ├── Generator.js    # The prompt input area and generation UI
│   │   ├── Generator.css   # Styles for the Generator
│   │   ├── Gallery.js      # The masonry grid displaying images
│   │   └── Gallery.css     # Styles for the Gallery
│   │
│   ├── App.js              # The root application component
│   ├── App.css             # Global UI styles and CSS variables
│   ├── index.js            # React DOM rendering entry point
│   └── index.css           # Base styles and resets
│
└── package.json            # Node.js dependencies and run scripts
```

---

## 🛠️ Installation & Setup (Frontend Only)

If you are running the frontend independently (for example, if the backend is hosted on a separate server or terminal), follow these steps:

### 1. Install Dependencies
Make sure you are in the `image-generator` directory, then run:
```bash
npm install
```

### 2. Start the Development Server
```bash
npm start
```
*The application will compile and launch in your default web browser at `http://localhost:3000`.*

> [!IMPORTANT]  
> **CORS Configuration:** Ensure that the backend is running (typically on `http://localhost:8000`) and has CORS enabled to accept requests from the React frontend, otherwise image generation will fail.

---

## 👨‍💻 Author

**Srinivasan Balaji**  
*Full Stack Developer & AI Enthusiast* 🚀  
[GitHub Profile](https://github.com/MisterSRINIVASAN)
