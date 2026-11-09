"""Comprueba tus ejercicios con los ejemplos de la hoja, antes de entregar.

    python comprobar.py        todas las pruebas
    python comprobar.py 2      solo las del ejercicio 2

En VS Code también puedes usar Terminal → Ejecutar tarea… → «Comprobar mis ejercicios».

Estas pruebas son las mismas que pasa el corrector de la asignatura cuando entregas.
No cambies nada de la carpeta .corrector: el corrector usa siempre la versión original.
"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / ".corrector"))

import motor  # noqa: E402

VERDE, ROJO, GRIS, FIN = "\033[32m", "\033[31m", "\033[90m", "\033[0m"
if not sys.stdout.isatty():
    VERDE = ROJO = GRIS = FIN = ""


def leer_configuracion() -> dict:
    try:
        import tomllib
    except ModuleNotFoundError:  # Python anterior a 3.11
        return {"pruebas": "pruebas.json"}
    with open(RAIZ / ".corrector" / "practica.toml", "rb") as f:
        return tomllib.load(f).get("practica", {})


def elegir(pruebas: list, filtro: str) -> list:
    if not filtro:
        return pruebas
    if filtro.isdigit():
        n = int(filtro)
        claves = (f"ejercicio_{n:02d}", f"ejercicio_{n}_", f"ejercicio_{n}.", f"ejercicio {n} ")
        return [p for p in pruebas if any(c in p.run.lower() or c in p.nombre.lower() + " "
                                          for c in claves)]
    filtro = filtro.lower()
    return [p for p in pruebas if filtro in p.nombre.lower() or filtro in p.run.lower()]


def mostrar(r: "motor.ResultadoPrueba") -> None:
    if r.superada:
        print(f"{VERDE}✔{FIN} {r.nombre}")
        return
    print(f"{ROJO}✘ {r.nombre}{FIN}: {r.motivo}")
    if r.tipo == "io":
        if r.entrada:
            print(f"{GRIS}  Se escribe en el teclado:{FIN}")
            for linea in r.entrada.rstrip("\n").split("\n"):
                print(f"    {linea}")
        diferencia = motor.explicar_diferencia(r.esperado, r.salida) if r.salida else ""
        if diferencia:
            for linea in diferencia.split("\n"):
                print(f"  {linea}")
        else:
            print(f"{GRIS}  Salida esperada:{FIN}")
            for linea in r.esperado.split("\n"):
                print(f"    {linea}")
    if r.error.strip():
        print(f"{GRIS}  Error del programa:{FIN}")
        for linea in r.error.strip().split("\n")[-6:]:
            print(f"    {linea}")
    print()


def main() -> int:
    configuracion = leer_configuracion()
    pruebas = motor.cargar_pruebas(RAIZ / ".corrector" / configuracion.get("pruebas", "pruebas.json"))
    elegidas = elegir(pruebas, sys.argv[1] if len(sys.argv) > 1 else "")
    if not elegidas:
        print(f"Ninguna prueba coincide con «{sys.argv[1]}».")
        return 2
    resultado = motor.evaluar(elegidas, motor.ejecutor_local(RAIZ, sys.executable), RAIZ,
                              al_terminar=mostrar)
    total = f"{resultado.puntos} de {resultado.max_puntos} puntos"
    if resultado.puntos == resultado.max_puntos:
        print(f"\n{VERDE}Todo bien: {total}.{FIN} Haz commit y push para entregar.")
    else:
        print(f"\n{total}. Corrige lo que falla y vuelve a comprobar.")
    return 0 if resultado.puntos == resultado.max_puntos else 1


if __name__ == "__main__":
    sys.exit(main())
