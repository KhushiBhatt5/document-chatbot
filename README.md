<<<<<<< HEAD
# 🤖 AI Document Chatbot

A beautiful, modern chatbot application that lets you upload PDF and TXT files and chat with an AI assistant about their contents using Google's Gemini AI.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2.8-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 📄 **Multi-Format Support**: Upload and process both PDF and TXT files
- 💬 **Intelligent Chat**: Ask questions about your uploaded documents
- 🎨 **Premium UI**: Modern, glassmorphic design with smooth animations
- 🔄 **Session Management**: Maintain chat history and uploaded files per session
- ⚡ **Real-time Processing**: Instant file upload and text extraction
- 🎯 **Context-Aware**: AI responses based on all uploaded files in your session

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone or download this project**

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure your API key**
   - Open the `.env` file in the project root
   - Replace `YOUR_API_KEY_HERE` with your actual Gemini API key:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```

6. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## 📖 Usage

1. **Upload Files**: Click the "Upload File" button in the sidebar to upload PDF or TXT files
2. **Ask Questions**: Type your question in the input box and press Enter or click Send
3. **Get Answers**: The AI will analyze your uploaded files and provide relevant answers
4. **New Chat**: Click "New Chat" to start a fresh session with no files or history

## 🛠️ Technology Stack

- **Backend**: Django 5.2.8
- **AI Model**: Google Gemini 1.5 Flash
- **PDF Processing**: pypdf
- **Environment Management**: python-dotenv
- **Frontend**: Vanilla HTML/CSS/JavaScript with custom animations

## 📁 Project Structure

```
chatbot_project/
├── chat/                      # Main Django app
│   ├── models.py             # Database models
│   ├── views.py              # View logic
│   ├── utils.py              # File processing & AI utilities
│   ├── urls.py               # URL routing
│   └── templates/chat/       # HTML templates
├── chatbot_core/             # Django project settings
├── media/uploads/            # Uploaded files storage
├── db.sqlite3               # SQLite database
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
└── manage.py               # Django management script
```

## 🔧 Configuration

### Supported File Types

- **PDF** (.pdf) - Extracts text from all pages
- **TXT** (.txt) - Reads plain text files with UTF-8 or Latin-1 encoding

### Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## 🎨 Features in Detail

### Premium UI Design
- Glassmorphism effects with backdrop blur
- Smooth gradient backgrounds
- Micro-animations on interactions
- Typing indicators for AI responses
- Loading states for file uploads
- Responsive design for mobile devices

### Smart File Processing
- Automatic file type detection
- Error handling for corrupted files
- Multiple encoding support for text files
- Session-based file management

### AI Integration
- Context-aware responses using all uploaded files
- Error handling for API failures
- Configurable system instructions
- Multi-turn conversation support

## 🐛 Troubleshooting

### API Key Issues
- **Error**: "Gemini API Key not configured"
- **Solution**: Make sure your `.env` file has a valid API key

### File Upload Errors
- **Error**: "Unsupported file type"
- **Solution**: Only PDF and TXT files are supported

### Database Errors
- **Solution**: Run `python manage.py migrate` to create/update database tables

### Server Won't Start
- **Solution**: Make sure port 8000 is not in use, or specify a different port:
  ```bash
  python manage.py runserver 8080
  ```

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 💡 Future Enhancements

- [ ] Support for more file formats (DOCX, XLSX, etc.)
- [ ] User authentication and multiple user support
- [ ] File deletion functionality
- [ ] Export chat history
- [ ] Dark/Light theme toggle
- [ ] Voice input support

## 📧 Support

If you encounter any issues or have questions, please open an issue on the project repository.

---

Made with ❤️ using Django and Google Gemini AI
=======
# document-chatbot
AI-powered chatbot that answers questions from PDF and text files.
>>>>>>> c25cf25955ed677b08fae98abb0adf9cbbd2b210
