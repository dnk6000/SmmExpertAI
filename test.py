from generators.text_gen import PostGenerator
from generators.image_gen import ImageGenerator
from social_publishers.vk_publisher import VKPublisher
import config as conf

post_gen = PostGenerator(conf.openai_key, tone="креативный", topic="Польза LPG-массажа", proxy=conf.proxy)
content = post_gen.generate_post()
img_desc = post_gen.generate_post_image_description()

img_gen = ImageGenerator(conf.openai_key, proxy=conf.proxy)
image_url = img_gen.generate_image(img_desc)

vk_pub = VKPublisher(conf.vk_api_key, conf.vk_group_id)
vk_pub.publish_post(content, image_url)

print(content)
print(image_url)