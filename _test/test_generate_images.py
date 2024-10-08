import unittest
import os
import sys

# Añadir la ruta del directorio 'dist' al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from PIL import Image
from generate_images import generate_splash_images, generate_icons
from sizes import splash_sizes, icon_sizes

class TestPWAImageGeneration(unittest.TestCase):

    def setUp(self):
        # Directorios de salida temporales para las pruebas
        self.splash_output_dir = './test_output/splash'
        self.icon_output_dir = './test_output/icons'
        self.image_base_path = 'test_image.png'  # Ruta del ícono base de prueba
        self.background_color = (34, 45, 67)

        # Crear una imagen de prueba para usar en los tests
        self.test_image = Image.new('RGBA', (1024, 1024), (255, 0, 0, 255))
        self.test_image.save(self.image_base_path)

        # Crear los directorios de salida si no existen
        if not os.path.exists(self.splash_output_dir):
            os.makedirs(self.splash_output_dir)
        if not os.path.exists(self.icon_output_dir):
            os.makedirs(self.icon_output_dir)

    def tearDown(self):
        # Elimina los archivos generados por los tests
        for folder in [self.splash_output_dir, self.icon_output_dir]:
            for file_name in os.listdir(folder):
                file_path = os.path.join(folder, file_name)
                os.remove(file_path)
        
        # Eliminar directorios de salida después de las pruebas
        if os.path.exists(self.splash_output_dir):
            os.rmdir(self.splash_output_dir)
        if os.path.exists(self.icon_output_dir):
            os.rmdir(self.icon_output_dir)

        # Eliminar imagen de prueba
        if os.path.exists(self.image_base_path):
            os.remove(self.image_base_path)

    def test_generate_splash_images(self):
        """Prueba que se generen correctamente las imágenes splash"""
        generate_splash_images(self.image_base_path, self.splash_output_dir, splash_sizes, self.background_color)

        # Verificar que las imágenes splash se hayan generado
        for size_name in splash_sizes:
            output_path = os.path.join(self.splash_output_dir, f'splash-{size_name}.png')
            self.assertTrue(os.path.exists(output_path), f"El archivo {output_path} no se generó.")
            
            # Verificar que el tamaño de la imagen sea correcto
            img = Image.open(output_path)
            expected_size = splash_sizes[size_name]
            self.assertEqual(img.size, expected_size, f"El tamaño de la imagen {output_path} es incorrecto.")

    def test_generate_icons(self):
        """Prueba que se generen correctamente los íconos"""
        generate_icons(self.image_base_path, self.icon_output_dir, icon_sizes)

        # Verificar que los íconos se hayan generado
        for size_name in icon_sizes:
            output_path = os.path.join(self.icon_output_dir, f'icon-{size_name}.png')
            self.assertTrue(os.path.exists(output_path), f"El archivo {output_path} no se generó.")
            
            # Verificar que el tamaño del ícono sea correcto
            img = Image.open(output_path)
            expected_size = icon_sizes[size_name]
            self.assertEqual(img.size, expected_size, f"El tamaño del ícono {output_path} es incorrecto.")

if __name__ == '__main__':
    unittest.main()
