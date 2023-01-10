from pywebio.output import put_html

def example_webio():
    put_html("""
    <h1>Example pywebio program</h1>
    <input type='text' id='input_text' placeholder='Type something here'><br>
    <button onclick='pywebio.submit()'>Submit</button>
    <br><br>
    <div id='output'></div>
    """)

    inputs = input()
    text = inputs.inputs['input_text']
    put_html("""
    <script>
    document.getElementById("output").innerHTML = "You typed: """+text+""""
    </script>
    """)
    
example_webio()

"""
In this example, the put_html function is used to write the HTML for the webpage. The webpage contains a text field, a button and a div element. On clicking the submit button, it calls pywebio.submit() which submits the form and the entered text is saved in the inputs variable and we access it by calling inputs.inputs['input_text'].
And the text entered is then displayed on the webpage using JavaScript code by setting innerHTML of the output div element.
"""
