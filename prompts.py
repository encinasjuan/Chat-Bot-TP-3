from typing import List, Dict
def build_system_prompt(role_instructions: str) -> str:
base = (
"Sos un chatbot de consola que responde en español de forma clara y útil. "
"Si el usuario pide código, incluí explicaciones breves. "
"Evitá información inventada y pedí aclaraciones si faltan datos.\n\n"
)
return base + f"Contexto de rol: {role_instructions}"
def collapse_history(history: List[Dict[str, str]]) -> List[Dict[str, str]]: