import sys
from roles import RolePreset
from chat_service import ChatService
from config import settings

def choose_role() -> RolePreset:
    print("¡Elegí un rol inicial:")
    print("1) Profesor 2) Traductor 3) Programador 4) Asistente")
    sel = input("> ").strip()
    mapping = {
        "1": RolePreset.PROFESOR,
        "2": RolePreset.TRADUCTOR,
        "3": RolePreset.PROGRAMADOR,
        "4": RolePreset.ASISTENTE,
    }
    return mapping.get(sel, RolePreset.ASISTENTE)

def print_help():
    print("\nComandos:")
    print("role [profesor|traductor|programador|asistente] -> cambia el rol")
    print("reset -> limpia la memoria")
    print("salir -> termina la app")

def main():
    print(f"🤖 {settings.system_name}")
    role = choose_role()
    chat = ChatService(role=role)
    print_help()

    while True:
        try:
            user = input(f"🧠 {chat.role.value}: ")
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Chau!")
            break
        
        if not user:
            continue

        if user.lower() in ("salir", "salír", "exit", "quit"):
            break

        if user.lower() == "reset":
            chat.reset()
            print("✨ Memoria borrada")
            continue

        if user.lower().startswith("role "):
            # Tratamiento de cambio de rol
            _, new_role_str = user.split(" ", 1)
            new_role_str = new_role_str.lower()
            
            mapping_r = {
                "profesor": RolePreset.PROFESOR,
                "traductor": RolePreset.TRADUCTOR,
                "programador": RolePreset.PROGRAMADOR,
                "asistente": RolePreset.ASISTENTE,
            }

            # Si el nuevo rol está en el mapeo
            if new_role_str in mapping_r:
                chat.set_role(mapping_r[new_role_str])
                print(f"🎭 Rol cambiado a {new_role_str}")
            else:
                print(f"⚠️ Rol inválido. Opciones: profesor, traductor, programador, asistente")
            continue

        if user.lower() == "help":
            print_help()
            continue

        # Pregunta normal
        try:
            answer = chat.ask(user)
            print(f"🤖 {answer}\n")
        except Exception as e:
            print(f"❌ Error no manejado: {e}")


if __name__ == "__main__":
    main()