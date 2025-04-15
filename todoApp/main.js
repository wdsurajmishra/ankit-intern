const todos = JSON.parse(localStorage.getItem("todos")) || [];

const todoForm = document.getElementById("todoForm");
const todosContainer = document.getElementById("todos");

function displayTodos() {
  todosContainer.innerHTML = "";
  todos.forEach((todo, index) => {
    todosContainer.innerHTML += `
                          <div class="todo">
                              <h4>${todo.title}</h4>
                              <p>${todo.description}</p>
                                <button class="btn btn-danger" onclick="deleteTodo(${index})">Delete</button>
                          </div>`;
  });
}

displayTodos();

function addTodo(title, description) {
  const newTodo = {
    title: title, 
    description: description,
    completed: false,
  };
  todos.push(newTodo);
  localStorage.setItem("todos", JSON.stringify(todos));
  displayTodos();
}

todoForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const title = document.getElementById("title").value;
  const description = document.getElementById("desc").value;
  addTodo(title, description);
  todoForm.reset();
  alert("Todo added successfully!");
});


