from dotenv import load_dotenv
import os

load_dotenv()

openai_key = os.getenv('OPEN_AI_KEY')
openai_model = "gpt-3.5-turbo"  # "gpt-4o"
proxy = os.getenv('PROXY')
vk_api_key = os.getenv('VK_API_KEY')
vk_group_id = os.getenv('GROUP_ID')
