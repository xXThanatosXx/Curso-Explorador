from PIL import Image

def convert_to_300dpi(input_image_path, output_image_path):
    with Image.open(input_image_path) as img:
        # Cambiar la resolución a 300 dpi
        img.save(output_image_path, dpi=(300, 300))

# Ruta de la imagen de entrada y salida
input_image_path = 'D:\Shadow\GitHub\Curso-Explorador\Misión Dos\Foto.jpg'
output_image_path = 'D:\Shadow\GitHub\Curso-Explorador\Misión Dos\Foto_salida.jpg'

convert_to_300dpi(input_image_path, output_image_path)
