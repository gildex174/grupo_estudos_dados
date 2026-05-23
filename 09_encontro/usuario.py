import re

url = "www.x.com/gildex174"

nome_usuario = re.search(r"^(?:https?://)?(?:www\.)?x\.com/(.+)", url)

print(f"O nome do usuário é: {nome_usuario.group(1)}")
