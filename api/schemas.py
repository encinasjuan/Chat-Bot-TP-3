from pydantic import BaseModel

class ChatRequest(BaseModel):
    mensaje: str
    role: str = "asistente"
    reset: bool = False

class ChatResponse(BaseModel):
    respuesta: str