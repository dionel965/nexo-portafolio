from django.shortcuts import render


def inicio(request):
    return render(
        request,
        "atlas/inicio.html",
        {
            "titulo_pagina": "Atlas filosófico — Inicio",
            "seccion_activa": "inicio",
        },
    )


def estoicismo(request):
    return render(
        request,
        "atlas/tema.html",
        {
            "titulo_pagina": "Estoicismo — Atlas filosófico",
            "seccion_activa": "estoicismo",
            "tema": "Estoicismo",
            "resumen": "Enfoque en distinguir lo que depende de nosotros de lo que no, cultivar la templanza y actuar con serenidad ante los contratiempos.",
            "cita": "No nos afectan las cosas mismas, sino la opinión que tenemos sobre ellas.",
            "autor_cita": "Epicteto",
        },
    )


def existencialismo(request):
    return render(
        request,
        "atlas/tema.html",
        {
            "titulo_pagina": "Existencialismo — Atlas filosófico",
            "seccion_activa": "existencialismo",
            "tema": "Existencialismo",
            "resumen": "La idea de que existimos primero y definimos nuestro sentido a través de nuestras elecciones, asumiendo la responsabilidad de lo que hacemos.",
            "cita": "El hombre está condenado a ser libre.",
            "autor_cita": "Jean-Paul Sartre",
        },
    )


def etica(request):
    return render(
        request,
        "atlas/tema.html",
        {
            "titulo_pagina": "Ética — Atlas filosófico",
            "seccion_activa": "etica",
            "tema": "Ética",
            "resumen": "Reflexión sobre qué hace que una acción sea justa, responsable o deseable en la convivencia diaria.",
            "cita": "La excelencia no es un acto, sino un hábito.",
            "autor_cita": "Aristóteles",
        },
    )


def tecnologia(request):
    return render(
        request,
        "atlas/tema.html",
        {
            "titulo_pagina": "Tecnología — Atlas filosófico",
            "seccion_activa": "tecnologia",
            "tema": "Tecnología",
            "resumen": "Preguntas sobre cómo las herramientas digitales moldean nuestra atención, privacidad, trabajo y forma de relacionarnos.",
            "cita": "Primero configuramos nuestras herramientas y luego ellas nos configuran a nosotros.",
            "autor_cita": "John Culkin",
        },
    )