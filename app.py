import os
from flask import Flask
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

vault_url = "https://p4keyvault.vault.azure.net/"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=vault_url, credential=credential)

@app.route("/")
def home():
    try:
        secret = client.get_secret("P4SampleSecret")
        return f"Secret: {secret.value}"
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    # Use PORT environment variable, default to 5000 for local development
    port = int(os.getenv("PORT", 5200))
    app.run(host="0.0.0.0", port=port)