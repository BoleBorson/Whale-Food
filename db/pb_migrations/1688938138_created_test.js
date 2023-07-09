migrate((db) => {
  const collection = new Collection({
    "id": "be17nufwxi27l0o",
    "created": "2023-07-09 21:28:58.930Z",
    "updated": "2023-07-09 21:28:58.930Z",
    "name": "test",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "vjq0nnng",
        "name": "charge",
        "type": "text",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
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
  const collection = dao.findCollectionByNameOrId("be17nufwxi27l0o");

  return dao.deleteCollection(collection);
})
