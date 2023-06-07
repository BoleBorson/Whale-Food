from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Define the labeled dataset
data = [
    ("apple", "Fruits"),
    ("banana", "Fruits"),
    ("orange", "Fruits"),
    ("broccoli", "Vegetables"),
    ("carrot", "Vegetables"),
    ("lettuce", "Vegetables"),
    ("beef", "Meat"),
    ("chicken", "Meat"),
    ("pork", "Meat"),
    ("milk", "Dairy"),
    ("cheese", "Dairy"),
    ("yogurt", "Dairy"),
    ("bread", "Bakery"),
    ("bagel", "Bakery"),
    ("croissant", "Bakery"),
    ("salmon", "Seafood"),
    ("shrimp", "Seafood"),
    ("tuna", "Seafood"),
    ("soup", "Canned Goods"),
    ("beans", "Canned Goods"),
    ("corn", "Canned Goods"),
    ("chips", "Snacks"),
    ("cookies", "Snacks"),
    ("nuts", "Snacks"),
    ("soda", "Beverages"),
    ("juice", "Beverages"),
    ("water", "Beverages"),
    ("ice cream", "Frozen Foods"),
    ("pizza", "Frozen Foods"),
    ("vegetables", "Frozen Foods")
]

# Split the dataset into input and output arrays
X, y = zip(*data)

# Convert the input array to a bag-of-words representation
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Train a Naive Bayes classifier on the labeled dataset
clf = MultinomialNB()
clf.fit(X, y)

# Use the trained classifier to predict the category of a new food item name
new_item = "apple"
new_item_vec = vectorizer.transform([new_item])
predicted_category = clf.predict(new_item_vec)[0]

print(predicted_category)  # Output: "Fruits"