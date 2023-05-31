migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("1nsn9jz5338hrj6")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "r3fohthi",
    "name": "rec",
    "type": "file",
    "required": false,
    "unique": false,
    "options": {
      "maxSelect": 1,
      "maxSize": 5242880,
      "mimeTypes": [],
      "thumbs": [],
      "protected": false
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("1nsn9jz5338hrj6")

  // remove
  collection.schema.removeField("r3fohthi")

  return dao.saveCollection(collection)
})
