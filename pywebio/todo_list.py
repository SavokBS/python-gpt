
from pywebio.output import put_html, put_text

def todo_list():
    put_html("""
    <h1>To-Do List</h1>
    <input type="text" id="todo_text" placeholder="Add a new task">
    <button onclick="addTask()">Add</button>
    <br>
    <br>
    <ul id="todo_list"></ul>
    
    <script>
    var todoList = [];
    
    function addTask() {
        var task = document.getElementById("todo_text").value;
        if (task === "") {
            alert("Please enter a task!");
            return;
        }
        todoList.push(task);
        updateList();
        document.getElementById("todo_text").value = "";
    }
    
    function removeTask(index) {
        todoList.splice(index, 1);
        updateList();
    }
    
    function updateList() {
        var todoListElem = document.getElementById("todo_list");
        todoListElem.innerHTML = "";
        for (var i = 0; i < todoList.length; i++) {
            var listElem = document.createElement("li");
            var checkbox = document.createElement("input");
            checkbox.type = "checkbox";
            checkbox.onclick = function() {removeTask(i)};
            listElem.appendChild(checkbox);
            listElem.appendChild(document.createTextNode(todoList[i]));
            todoListElem.appendChild(listElem);
        }
    }
    </script>
    """)

todo_list()

"""
This code creates a webpage with an input field where users can enter a new task, a "Add" button, and an empty unordered list which will hold the tasks.
when the user enters
"""
