import httpx
from openai import OpenAI
import config

class PostGenerator:
    def __init__(self, openai_key, tone, topic, proxy=None):
        self.client = OpenAI(api_key=openai_key) if proxy is None or proxy == "" \
                 else OpenAI(api_key=openai_key, http_client=httpx.Client(proxy=proxy))
        self.tone = tone
        self.topic = topic

    def generate_post(self):
        response = self.client.chat.completions.create(
          model=config.openai_model,
          messages=[
            {"role": "system", "content":
                """Ты высококвалифицированный SMM специалист, который будет помогать в генерации текста 
                   для постов с заданной тематикой и заданным тоном.
                """
             },
            {"role": "user", "content": f"Сгенерируй пост для соцсетей с темой {self.topic}, используя тон: {self.tone}"}
          ]
        )
        return response.choices[0].message.content

    def generate_post_image_description(self):
        response = self.client.chat.completions.create(
          model=config.openai_model,
          messages=[
            {"role": "system", "content":
                """Ты ассистент, который составит промпт для нейросети, 
                   которая будет генерировать изображения. Ты должен составлять промпт на заданную тематику.
                """
             },
            {"role": "user", "content": f"Сгенерируй изображение для соцсетей с темой {self.topic}"}
          ]
        )
        return response.choices[0].message.content

if __name__ == "__main__":
    post = PostGenerator(config.openai_key, "креативный", "Польза LPG-массажа", config.proxy)
    print(post.generate_post())
    print("\n")
    print(post.generate_post_image_description())