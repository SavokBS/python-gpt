import uuid
from pywebio.input import text_input
from pywebio.output import put_html, put_text

def pastebin():
    put_html("""
    <h1>PyWebIO Pastebin</h1>
    <textarea id="text_area"></textarea><br>
    <button onclick="pywebio.submit()">Submit</button>
    """)
    
    text = text_input()
    text_id = str(uuid.uuid4())
    file_name = f"{text_id}.txt"
    with open(file_name, "w") as f:
        f.write(text)
    
    put_html("""
    <br><br>
    <p>Your text has been saved. Share this link to retrieve it later:</p>
    <a href='/retrieve/{}'>http://localhost:8888/retrieve/{}</a>
    """.format(text_id, text_id))

def retrieve(text_id):
    file_name = f"{text_id}.txt"
    try:
        with open(file_name, "r") as f:
            text = f.read()
    except FileNotFoundError:
        put_html("<h1>Invalid Link</h1><p>The link you followed is invalid or has expired.</p>")
        return
    put_html("<h1>Retrieved Text</h1><pre>" + text + "</pre>")

"""
Uhm.. Uhm. Set up other stuff by yourself.
"""
