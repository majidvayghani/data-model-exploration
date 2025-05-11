db = db.getSiblingDB('money');

db.users.insertMany(require('/docker-entrypoint-initdb.d/users.json'));
db.tasks.insertMany(require('/docker-entrypoint-initdb.d/tasks.json'));
db.projects.insertMany(require('/docker-entrypoint-initdb.d/projects.json'));
db.comments.insertMany(require('/docker-entrypoint-initdb.d/comments.json'));