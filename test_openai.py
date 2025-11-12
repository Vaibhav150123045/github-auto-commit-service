from openai import OpenAI
from openai import APIError, RateLimitError, AuthenticationError, PermissionDeniedError
import os

# Replace with your actual API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Hello, are you working?"}],
    )

    print("✅ Success! API responded:")
    print(response.choices[0].message.content)

except AuthenticationError:
    print("❌ Invalid API key or missing key.")
except PermissionDeniedError:
    print("❌ Your account doesn't have access to this model.")
except RateLimitError:
    print("⚠️ You might be out of quota or balance. Check your billing page.")
except APIError as e:
    print(f"🚨 API Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
