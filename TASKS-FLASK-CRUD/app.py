from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete


tasks = []
task_id_control = 1 # criamos essa variavel fora, pois se criassemos dentro do metodo acabaria resetando e tendo varias tasks com id 1

@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control # usado para o programa conseguir usar uma variavel de fora do metodo.
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', ""))
    task_id_control += 1 # essa adição acaba sendo necessário usar o global para conseguirmos usar a task_id_control
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks ]

    output = {
                  "tasks": task_list,
                  "total_tasks": 0
            }
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)