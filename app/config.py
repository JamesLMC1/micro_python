import os

from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "").rstrip("/")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
PORT = int(os.getenv("PORT", "8000"))

REST_URL = f"{SUPABASE_URL}/rest/v1"
