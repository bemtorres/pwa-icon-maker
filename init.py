from generate_images import generate_splash_images, generate_icons
from sizes import splash_sizes, icon_sizes



image_base_path = "imagen.png"  # Ruta del ícono base


splash_output_dir = "./images/icons/splash"
icon_output_dir = "./images/icons"
background_color = (34, 45, 67)  # Ejemplo de color de fondo (RGB)

# Generar las imágenes splash
generate_splash_images(image_base_path, splash_output_dir, splash_sizes, background_color)

# Generar los íconos
generate_icons(image_base_path, icon_output_dir, icon_sizes)


