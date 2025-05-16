#making a to do list manager which has features like adding a task, mark it as done, edit a task, delete a task, view all task, view only pending or done tasks. our to-do list saves the deadline too

tasks = {}
task_id = 1
while True:
    actions = input("What would you like to do? (add/view/edit/delete/mark/exit/view done/view pending): ").lower()
    if actions == "add":
        task = input("Enter the task discription: ")
        deadline = input("Enter the deadline date (YYYY-MM-DD): ")
        tasks[task_id] = {"task" : task, 
                          "status": "pending",
                          "deadline": str(deadline)}
        print("Task added with task ID,", task_id)
        task_id += 1
    elif actions == "view":
        print(tasks.items())
    elif actions == "edit":
        task_id = int(input("Enter the task ID of the task you want to edit: "))
        if task_id in tasks:
            new_task = input("Enter the task you want to replace previous one with: ")
            tasks[task_id]["task"] = new_task
            print("Task replaced successfully!!")
        else:
            print("Invalid task ID!!")
    elif actions == "delete":
        task_id = int(input("Enter the task ID of the task that you want to delete: "))
        if task_id in tasks:
            del tasks[task_id]
            print("Task ", task_id, "deleted")
        else:
            print("Invalid task ID")
    elif actions == "mark":
        task_id = int(input("Enter the task ID of the task you want to mark done: "))
        if task_id in tasks:
            tasks[task_id]["status"] = "Done"
            print("Task is now marked as'Done'!!")
        else:
            print("Invalid task ID")
    elif actions == "view done":
        print("\nCompleted tasks")
        found = False
        for task_id, task_info in tasks.items():
            if task_info["status"].lower() == "Done" :
                print(task_id, task_info['task'])
                found = True
        if not found:
            print("You havent finished anything yet lazy ass!")

    elif actions == "view pending":
        print("\nPending tasks")
        found = False
        for task_id, task_info in tasks.items():
            if task_info["status"].lower() == "pending" :
                print(task_id, task_info['task'])
                found = True
        if not found:
            print("Good job no work is left for today! ")       


    