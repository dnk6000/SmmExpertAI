import httpx
from openai import OpenAI

class ImageGenerator:
    def __init__(self, openai_key, proxy=None):
        self.client = OpenAI(api_key=openai_key) if proxy is None or proxy == "" \
                 else OpenAI(api_key=openai_key, http_client=httpx.Client(proxy=proxy))

    def generate_image(self, prompt):
        response = self.client.images.generate(
          model="dall-e-3",
          prompt=prompt,
          size="1024x1024",
          quality="standard",
          n=1,
        )

        image_url = response.data[0].url
        return image_url

if __name__ == "__main__":
    import config
    import text_gen

    post_gen = text_gen.PostGenerator(config.openai_key, "креативный", "Польза LPG-массажа", config.proxy)
    post = post_gen.generate_post()
    image_descr = post_gen.generate_post_image_description()
    print(post)
    print("\n")
    print(image_descr)

    image = ImageGenerator(config.openai_key, config.proxy)
    print(image.generate_image(image_descr))