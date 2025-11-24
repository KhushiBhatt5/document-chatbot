from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatSession, UploadedFile, ChatMessage
from .utils import extract_text_from_pdf, extract_text_from_txt, get_llm_response
import json

def get_or_create_session(request):
    session_id = request.session.get('chat_session_id')
    if session_id:
        try:
            return ChatSession.objects.get(id=session_id)
        except ChatSession.DoesNotExist:
            pass
    
    session = ChatSession.objects.create()
    request.session['chat_session_id'] = session.id
    return session

def index(request):
    session = get_or_create_session(request)
    messages = session.messages.all().order_by('timestamp')
    files = session.files.all().order_by('-uploaded_at')
    return render(request, 'chat/index.html', {'messages': messages, 'files': files})

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        session = get_or_create_session(request)
        file = request.FILES['file']
        
        # Save file
        uploaded_file = UploadedFile.objects.create(session=session, file=file)
        
        # Extract text based on file type
        file_extension = file.name.lower().split('.')[-1]
        
        if file_extension == 'pdf':
            text = extract_text_from_pdf(uploaded_file.file.path)
            uploaded_file.processed_text = text
            uploaded_file.save()
        elif file_extension == 'txt':
            text = extract_text_from_txt(uploaded_file.file.path)
            uploaded_file.processed_text = text
            uploaded_file.save()
        else:
            uploaded_file.delete()
            return JsonResponse({
                'status': 'error', 
                'message': 'Unsupported file type. Please upload PDF or TXT files only.'
            }, status=400)
            
        return JsonResponse({
            'status': 'success', 
            'filename': file.name, 
            'id': uploaded_file.id,
            'file_type': file_extension.upper()
        })
    return JsonResponse({'status': 'error'}, status=400)

@csrf_exempt
def ask_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question = data.get('question')
        
        if not question:
            return JsonResponse({'error': 'No question provided'}, status=400)
            
        session = get_or_create_session(request)
        
        # Save user message
        ChatMessage.objects.create(session=session, sender='user', text=question)
        
        # Gather context from all files in session
        context = ""
        for file in session.files.all():
            context += f"--- File: {file.file.name} ---\n{file.processed_text}\n\n"
            
        # Get chat history for context (optional, but good for flow)
        history = []
        # We could fetch previous messages here if we want multi-turn context
        # For now, let's just send the current question and file context
        history.append({'role': 'user', 'parts': [question]})
        
        # Get LLM response
        answer = get_llm_response(history, context)
        
        # Save bot message
        ChatMessage.objects.create(session=session, sender='bot', text=answer)
        
        return JsonResponse({'answer': answer})
    return JsonResponse({'status': 'error'}, status=400)

def clear_chat(request):
    # Create a new session
    session = ChatSession.objects.create()
    request.session['chat_session_id'] = session.id
    return redirect('index')
