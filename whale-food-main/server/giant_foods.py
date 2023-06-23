import requests
import json

# Make a GET request to the API endpoint
url = "https://giantfood.com/api/v6.0/products/2016435934/50000351?catTreeId=805&sort=itemsPurchased+desc,+name+asc&filter=&start=0&flags=true&substitute=false&nutrition=false&extendedInfo=false&facetExcludeFilter=true&includeSponsoredProducts=true&facet=specials,categories,brands,nutrition,sustainability,newArrivals,privateLabel"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = json.loads(response.text)
    
    # Access the relevant information from the response
    has_nutrition = data["response"]["hasNutrition"]
    category = data["response"]["category"]["categoryName"]
    nutrition_facets = data["response"]["facets"]["nutrition"]
    brands = data["response"]["facets"]["brands"]
    categories = data["response"]["facets"]["categories"]
    
    # Process the data further or perform desired operations
    # ...

else:
    print("Error: Failed to fetch data from the API")
