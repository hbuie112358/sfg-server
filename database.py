from dotenv import load_dotenv
import os
from supabase import create_client, Client

load_dotenv()  # Loads environment variables from .env file into the current environment

# retrieves values from the environment variables and assigns them to Python variables
supabase_url: str = os.getenv("SUPABASE_API_URL")
supabase_key: str = os.getenv("SUPABASE_SERVICE_KEY")

if not supabase_url or not supabase_key:
    raise ValueError("Missing Supabase credentials in environment variables.")

# Create Supabase client
supabase: Client = create_client(supabase_url, supabase_key)