from pathlib import Path

import cv2
import matplotlib.pyplot as plt

def mostrar(imagem, titulo=""):
    if imagem.ndim == 3:
        rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
        plt.imshow(rgb)
    else:
        plt.imshow(imagem, cmap="gray")
    plt.title(titulo)
    plt.axis("off")
    plt.show()

caminho = Path.cwd().resolve() / "video.mp4"

if not caminho.exists():
    print("Arquivo padrão não encontrado")
    caminho = Path.cwd().resolve() / input("Digite o nome do arquivo da pasta com o a extensão: ")

cap = cv2.VideoCapture(caminho)
print("Vídeo aberto?", cap.isOpened())

quadros = []
while True:
    ret, quadro = cap.read()
    if not ret:
        break
    quadros.append(quadro)

meio = len(quadros) // 2
quadro_meio = cv2.imwrite('frame_meio.jpg',quadros[meio])
mostrar(quadros[meio], "Quadro do meio")

total = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(f"total de quadros pela função do OpenCV: {total}")
print('Total de quadros pela contagem da lista:', len(quadros))

fps_lido = cap.get(cv2.CAP_PROP_FPS)
largura = cap.get(cv2.CAP_PROP_FRAME_WIDTH)    # largura
altura = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)   # altura
print(f'fps={fps_lido} | total de quadros={total} | duração do video={len(quadros)/fps_lido} segundos | tamanho={largura}x{altura}')

# Um vídeo é representado como uma sequência temporal de imagens reproduzidas. 
# Cada uma dessas imagens (quadros) é uma matriz de pixels, onde cada pixel é composto por três canais de cor em BGR no OpenCV e convertido para RGB e tons de cinza durante a execução, fps são os quadros por segundos.
quadro_meio_cinza = cv2.cvtColor(quadros[meio], cv2.COLOR_BGR2GRAY)
mostrar(quadro_meio_cinza, "Quadro do meio cinza")

pasta_frames = Path.cwd().resolve() / "frames"
pasta_frames.mkdir(exist_ok=True)

for i, q in enumerate(quadros):
    cv2.imwrite(f"frames/{i:03d}.jpg", q)
print(f"{len(quadros)} quadros salvos na pasta 'frames/'.")

cap.release()