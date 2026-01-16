/is_up (GET): Returns "OK", 200

/tasks (GET): Main page that shows the current tasks
/tasks/calendar (GET): An alternative view of the tasks. Shows task in the calendar.

/tasks/new (GET): Shows the form for creating a new task
/tasks/edit?task_id=<task_id> (GET, POST): Shows the form for editing a task with <task_id> id if the method is get. If the method is post, applies changes.

/add_task (POST): Adds a new task.

/tasks/delete?task_id=<task_id> (POST): Deletes the <task_id> task from the db.

