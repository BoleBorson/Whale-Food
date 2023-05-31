migrate((db) => {
  const collection = new Collection({
    "id": "1nsn9jz5338hrj6",
    "created": "2023-05-25 00:21:51.935Z",
    "updated": "2023-05-25 00:21:51.935Z",
    "name": "receipts",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "zrd8xgae",
        "name": "data",
        "type": "json",
        "required": false,
        "unique": false,
        "options": {}
      },
      {
        "system": false,
        "id": "kzi5nte0",
        "name": "user",
        "type": "relation",
        "required": false,
        "unique": false,
        "options": {
          "collectionId": "_pb_users_auth_",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": []
        }
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("1nsn9jz5338hrj6");

  return dao.deleteCollection(collection);
})
