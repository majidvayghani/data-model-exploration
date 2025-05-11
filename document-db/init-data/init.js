db = db.getSiblingDB('money_tracker');

db.createCollection('users');
db.createCollection('categories');
db.createCollection('tokens');
db.createCollection('transactions');

db.users.insertMany(require('/docker-entrypoint-initdb.d/users.json'));
db.tokens.insertMany(require('/docker-entrypoint-initdb.d/tokens.json'));
db.categories.insertMany(require('/docker-entrypoint-initdb.d/categories.json'));
db.transactions.insertMany(require('/docker-entrypoint-initdb.d/transactions.json'));