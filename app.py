from flask import Flask
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

vault_url = "https://p4keyvault.vault.azure.net/"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=vault_url, credential=credential)

@app.route("/")
def home():
    secret = client.get_secret("P4SampleSecret")
    return f"Secret: {secret.value}"

@app.route("/test")
def test():
    return "App is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

