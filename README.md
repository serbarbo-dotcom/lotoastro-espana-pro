# LotoAstro España PRO

Web estática para Bonoloto, La Primitiva y Euromillones. Frecuencias oficiales acumuladas desde el inicio, selecciones semanales, horóscopos chino y occidental/griego, calendario maya Tzolk’in, signo solar indio sideral aproximado, Luna y numerología. La relación con números de lotería es una fórmula recreativa propia, sin capacidad predictiva.

## Publicar

1. Crear un repositorio llamado `lotoastro-espana-pro`, con rama `main`.
2. Subir el contenido de esta carpeta respetando `.github/workflows/pages.yml`.
3. En Settings → Pages → Source elegir **GitHub Actions**.
4. En Actions ejecutar **Actualizar estadísticas y publicar LotoAstro** si no comenzó al subir los archivos.
5. Abrir el enlace mostrado en la ejecución de Pages.

El repositorio debe permitir Pages en tu plan. La web está pensada para acceso público. No contiene claves ni datos personales: cada visitante introduce su perfil y lo guarda en su navegador.

## Estadísticas y actualización

`stats.json` contiene una copia fechada de acumulados oficiales. El workflow intenta actualizarla en la publicación cada día a las 03:17 UTC y cuando cambia `main`. El horario de Actions puede retrasarse. Las tareas programadas de repositorios públicos pueden detenerse tras 60 días sin actividad; se reactivan en Actions.

El botón «Actualizar datos» carga el último archivo publicado, sin un servidor privado ni llamadas desde el móvil a SELAE. Si falla la fuente se conserva la copia del repositorio con su fecha. La descarga actualizada forma parte del artefacto publicado, sin modificar archivos del repositorio.

El historial sorteo a sorteo es local: solo incluye lo que el visitante registra o importa. El acumulado de frecuencias no se presenta como un archivo completo de resultados individuales.

## Comprobaciones locales

- `node test.mjs`
- `python update_stats.py` (requiere conexión)
- `python -m http.server 8000`

Los perfiles y jugadas de otra dirección web no se transfieren automáticamente: descargar copia en «Mis jugadas» y restaurarla aquí. El sitio no vende apuestas.
