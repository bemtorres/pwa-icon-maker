# PWA Icon & Splash Screen Generator

This Python project generates icons and splash screens for Progressive Web Apps (PWA) from a base image. It automatically resizes the base image into the required sizes for both splash screens and icons, making the setup process for your PWA faster and more efficient.

## Features

- Generates multiple splash screen sizes for various devices.
- Creates icons in different sizes, ready to be used in your PWA manifest.
- Simple command-line interface for generating images.

## Requirements

- Python 3.x
- [Pillow](https://python-pillow.org/) library for image manipulation

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bemtorres/pwa-icon-maker.git
   cd pwa-icon-maker
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your base image (e.g., `base_image.png`) in the project root directory.

2. Run the script to generate the icons and splash screens:
   ```bash
   python generate_images.py
   ```

3. The generated images will be saved in the following directories:
   - Splash screens: `./images/icons/splash/`
   - Icons: `./images/icons/`

## Image Sizes

The script generates the following image sizes:

### Splash Screens

- `640x1136`
- `750x1334`
- `828x1792`
- `1125x2436`
- `1242x2208`
- `1242x2688`
- `1536x2048`
- `1668x2224`
- `1668x2388`
- `2048x2732`

### Icons

- `72x72`
- `96x96`
- `128x128`
- `144x144`
- `152x152`
- `192x192`
- `384x384`
- `512x512`

## Customization

You can modify the `splash_sizes` and `icon_sizes` dictionaries in `generate_images.py` to add or change image dimensions based on your specific requirements.

## Testing

To test the script:

1. Ensure that you have a base image (e.g., `base_image.png`) in the project root directory.
2. Run the script:
   ```bash
   python generate_images.py
   ```

3. Verify that the output images have been correctly generated in the `./images/icons/splash/` and `./images/icons/` directories.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Instrucciones de prueba

1. **Preparación**:
   - Coloca una imagen base con el nombre `base_image.png` en el directorio raíz del proyecto.
   - Asegúrate de tener instalada la librería `Pillow`.

2. **Prueba**:
   - Ejecuta el siguiente comando en la terminal:
     ```bash
     python generate_images.py
     ```

3. **Verificación**:
   - Revisa que los íconos y pantallas splash se hayan generado correctamente en los directorios `./images/icons/` y `./images/icons/splash/`.
   - Verifica que los archivos tengan los tamaños adecuados y estén en formato `.png`.

Este `README.md` es ideal para subirlo a GitHub y proporcionar una visión clara del proyecto y su uso. Además, las instrucciones de prueba ayudan a verificar que todo funcione correctamente.