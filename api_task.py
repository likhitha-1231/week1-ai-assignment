import requests

print("=" * 40)
print("      DAILY MOTIVATION QUOTE")
print("=" * 40)

url = "https://zenquotes.io/api/random"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\nQuote:")
    print(data[0]["q"])

    print("\nAuthor:")
    print(data[0]["a"])

else:
    print("Failed to fetch quote.")