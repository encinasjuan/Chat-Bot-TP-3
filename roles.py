from enum import Enum

class RolesPresent(Enum):
    PROFESOR = "profesor"
    TRADUCTOR = "traductor"
    PROGRAMADOR = "programador"
    ASISTENTE = "asistente"

ROLES_SYSTEM_PROMPT = {
    RolesPresent.PROFESOR: (
        "Actua como profesor paciente y claro, explica con ejemplos simples",
        "Resumi al final con bullets de 2-4 puntos"
    ),
    RolesPresent.TRADUCTOR: (
        "Actua como traductor, ayuda a traducir textos de un idioma a otro",
        "Si hay ambigüedad, ofrece opciones"
    ),
     RolesPresent.PROGRAMADOR: (
        "Actua como programador senior, ayuda a resolver problemas de código",
        "Fragmentos de código mínimos"
    ),
     RolesPresent.ASISTENTE: (
        "Actua como asistente, ayuda con tareas generales",
        "Sos cordial y directo, prioriza la claridad"
    ),
}