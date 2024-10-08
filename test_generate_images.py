import os
import unittest
from PIL import Image
from generate_images import generate_images, splash_sizes, icon_sizes

class TestImageGeneration(unittest.TestCase):

    def setUp(self):
        """Configura la imagen base y los directorios de prueba."""
        self.image_base_path = 'test_image.png'
        self.splash_output_dir = './test_images/icons/splash'
        self.icons_output_dir = './test_images/icons'

        # Crear una imagen base de prueba
        image = Image.new('RGB', (1024, 1024), color = 'blue')
        image.save(self.image_base_path)

    def tearDown(self):
        """Limpia las imágenes generadas y la imagen base después de la prueba."""
        # Eliminar las imágenes generadas
        if os.path.exists(self.splash_output_dir):
            for file in os.listdir(self.splash_output_dir):
                os.remove(os.path.join(self.splash_output_dir, file))
            os.rmdir(self.splash_output_dir)

        if os.path.exists(self.icons_output_dir):
            for file in os.listdir(self.icons_output_dir):
                os.remove(os.path.join(self.icons_output_dir, file))
            os.rmdir(self.icons_output_dir)

        # Eliminar la imagen base
        if os.path.exists(self.image_base_path):
            os.remove(self.image_base_path)

        # Eliminar directorios principales
        if os.path.exists('./test_images/icons'):
            os.rmdir('./test_images/icons')
        if os.path.exists('./test_images'):
            os.rmdir('./test_images')

    def test_generate_splash_images(self):
        """Prueba que las imágenes splash se generen correctamente con los tamaños adecuados."""
        generate_images(self.image_base_path, self.splash_output_dir, splash_sizes, 'splash')

        for size, dimensions in splash_sizes.items():
            image_path = os.path.join(self.splash_output_dir, f'splash-{size}.png')
            self.assertTrue(os.path.exists(image_path), f"Imagen splash {size} no fue generada.")
            
            with Image.open(image_path) as img:
                self.assertEqual(img.size, dimensions, f"El tamaño de la imagen splash {size} no es correcto.")

    def test_generate_icon_images(self):
        """Prueba que los íconos se generen correctamente con los tamaños adecuados."""
        generate_images(self.image_base_path, self.icons_output_dir, icon_sizes, 'icon')

        for size, dimensions in icon_sizes.items():
            image_path = os.path.join(self.icons_output_dir, f'icon-{size}.png')
            self.assertTrue(os.path.exists(image_path), f"Ícono {size} no fue generado.")
            
            with Image.open(image_path) as img:
                self.assertEqual(img.size, dimensions, f"El tamaño del ícono {size} no es correcto.")

if __name__ == '__main__':
    unittest.main()
