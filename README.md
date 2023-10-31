# Ejercicio Loose Change
En este ejercicio haremos un software para devolver el cambio con el menor número de monedas posibles.
También crearemos test unitarios automatizados con pytest.

## Registrar markers
En el raíz del proyecto, creamos el fichero `pytest.ini`y en el registraremos los markers:
```bash
[pytest]
markers = 
    <custom_marker>: <descripción opcional>
```
En cada uno de los ficheros `test_.py` importamos `pytest` y utilizamos los decoradores `@pytest.mark.<custom_mark>`:
```python
import pytest

@pytest.mark.<custom_marker>
def test_custom_test():
    assert funcion(parametros) == <resultado esperado>:
```

## Ejecutar tests
- Para ejecutar todos los casos tests, en el terminal:
```bash
$ pytest
```

- Para ejecutar casos tests por el marker:
```bash
$ pytest -v -m "custom_marker"
```

- Para ejecutar casos tests por el nombre:
```bash
$ pytest -v -k "nombre_fichero"
```