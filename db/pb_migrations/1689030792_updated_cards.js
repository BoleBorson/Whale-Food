migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("c7odlu37pxqsvsr")

  collection.listRule = ""

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("c7odlu37pxqsvsr")

  collection.listRule = null

  return dao.saveCollection(collection)
})
