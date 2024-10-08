from PIL import Image
import os

def generate_splash_images(image_path, output_dir, sizes, background_color=(255, 255, 255)):
    """Genera imágenes de splash con un fondo de color y el ícono centrado."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Abrir la imagen base (ícono)
    icon = Image.open(image_path).convert("RGBA")
    
    for size_name, size in sizes.items():
        # Crear la imagen de fondo (splash) con el color de fondo
        splash_image = Image.new('RGB', size, color=background_color)
        
        # Redimensionar el ícono manteniendo la proporción
        icon_ratio = min(size[0] / icon.width, size[1] / icon.height) * 0.5  # Ajusta el ratio si es necesario
        new_icon_size = (int(icon.width * icon_ratio), int(icon.height * icon_ratio))
        resized_icon = icon.resize(new_icon_size, Image.LANCZOS)
        
        # Calcular la posición para centrar el ícono
        icon_position = (
            (size[0] - resized_icon.width) // 2,
            (size[1] - resized_icon.height) // 2
        )
        
        # Pegar el ícono en el fondo
        splash_image.paste(resized_icon, icon_position, resized_icon)
        
        # Guardar la imagen
        output_path = os.path.join(output_dir, f'splash-{size_name}.png')
        splash_image.save(output_path, "PNG")
        print(f"Imagen {size_name} generada y guardada en {output_path}")

def generate_icons(image_path, output_dir, sizes):
    """Genera íconos de varios tamaños."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Abrir la imagen base (ícono)
    icon = Image.open(image_path).convert("RGBA")
    
    for size_name, size in sizes.items():
        # Redimensionar el ícono al tamaño requerido
        resized_icon = icon.resize(size, Image.LANCZOS)
        
        # Guardar el ícono redimensionado
        output_path = os.path.join(output_dir, f'icon-{size_name}.png')
        resized_icon.save(output_path, "PNG")
        print(f"Ícono {size_name} generado y guardado en {output_path}")


def generate_images(image_path, output_dir, sizes, prefix):
    """Genera imágenes a partir de un archivo base para los tamaños especificados"""
    # Cargar imagen base
    image = Image.open(image_path)
    
    # Crear carpeta de salida si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generar imágenes para cada tamaño
    for name, size in sizes.items():
        resized_image = image.resize(size, Image.LANCZOS)
        output_path = os.path.join(output_dir, f'{prefix}-{name}.png')
        resized_image.save(output_path)
        print(f'Imagen generada: {output_path}')