# NOMBRE DE LA PRÁCTICA

Este es tu repositorio de NOMBRE DE LA PRÁCTICA. La hoja, con el contexto, los pasos y las pistas
de cada ejercicio, está en Moodle.

## Qué hay aquí

| Fichero | Ejercicio |
|---|---|
| `ejercicio_01_saludo.py` | Saludo |
| `comprobar.py` | Comprueba tus ejercicios con los ejemplos de la hoja |

Cada fichero de ejercicio empieza con un comentario. Escribe tu programa debajo. No cambies la
carpeta `.corrector/`.

## Antes de entregar: comprueba

En VS Code: **Terminal → Ejecutar tarea… → Comprobar mis ejercicios**. O en el terminal:

```bash
python comprobar.py        # todos los ejercicios
python comprobar.py 1      # solo el ejercicio 1
```

`comprobar.py` ejecuta tus programas con las entradas de los ejemplos de la hoja y compara tu
salida con la del ejemplo. Si algo falla, te enseña la primera línea distinta, con los espacios
marcados con `·`, y la columna en la que difiere.

## Cómo se entrega

Cada vez que haces `push`, tu trabajo queda entregado. Haz un commit cada vez que termines un
ejercicio:

```bash
git add ejercicio_01_saludo.py
git commit -m "Ejercicio 1 terminado"
git push
```

## Dónde ves tu corrección

El corrector de la asignatura pasa las mismas pruebas que `comprobar.py` a lo que has subido. Unos
minutos después de tu `push`, en la página de tu repositorio, en **Releases**, aparece una
**Corrección** con el resultado de cada prueba.
