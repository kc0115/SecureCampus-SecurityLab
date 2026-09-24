@app.route("/buscar")
def buscar():
    nombre = request.args.get("nombre", "")
    resultado_html = """
    <html>
    <head>
      <title>Resultado - SecureCampus</title>
    </head>
    <body>
      <h1>Resultado de búsqueda</h1>
      <p>Estudiante buscado: {{ nombre }}</p>
      <a href="/">Regresar</a>
    </body>
    </html>
    """
    return render_template_string(resultado_html, nombre=nombre)