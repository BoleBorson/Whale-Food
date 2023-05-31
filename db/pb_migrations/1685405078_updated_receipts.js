migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("1nsn9jz5338hrj6")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "vjnalhk0",
    "name": "charge",
    "type": "text",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("1nsn9jz5338hrj6")

  // remove
  collection.schema.removeField("vjnalhk0")

  return dao.saveCollection(collection)
})
