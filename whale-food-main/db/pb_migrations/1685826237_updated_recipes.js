migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("qffb4bfmom0c6vx")

  // remove
  collection.schema.removeField("lljqqjyr")

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("qffb4bfmom0c6vx")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "lljqqjyr",
    "name": "fa",
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
})
