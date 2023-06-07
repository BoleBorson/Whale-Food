import openai
import json

openai.organization = "org-Q0ykhTU2Crpdy2XGZ4nAbhOi"
openai.api_key = "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"

def format_receipt(receipt_text):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """
                I have text from a reciept that needs to be formatted,
                I want a list of all of the items on the receipt and their price, 
                the store it was purchased from,
                the total price of the items, and the type of purchase that it was (grocery, entertainment, shopping, misc).
                This is a sample json object of how I want the data returned, do your best to infer
                the correct values but if it is not possible still return the valid json object, 
                and just have the values as
            \n\n
            {
                "store": "walmart",
                "total": 300.01,
                "type": "grocery"
                "items": [
                    {
                        "name": "bread",
                        "price": 5.99
                    }
                ]
            }
            \n\n
            """ + receipt_text}
        ]
    )
    return res.choices[0].message.content