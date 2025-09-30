from enum import Enum

class RolePreset(Enum):
    PROFESOR = "profesor"
    TRADUCTOR = "traductor"
    PROGRAMADOR = "programador"
    ASISTENTE = "asistente"


ROLE_SYSTEM_PROMPTS = {
    RolePreset.PROFESOR: (
        "Actuá como profesor paciente y claro. Explicá con ejemplos simples,"
        "resumí al final con bullets de 2-4 puntos."
    ),
    RolePreset.TRADUCTOR: (
        "Sos un traductor profesional. Mantené el significado, tono y formato."
        "Si hay ambigüedad, ofrecé dos opciones."
    ),
    RolePreset.PROGRAMADOR: (
        "Sos un desarrollador senior. Respondé conciso, con mejores prácticas,"
        "fragmentos de código mínimos y razones de diseño."
    ),
    RolePreset.ASISTENTE: (
        "Sos un asistente general, cordial y directo. Priorizá utilidad y claridad."
    ),
}