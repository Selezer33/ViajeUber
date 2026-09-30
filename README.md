# ViajeUber

Práctica de programación funcional con Python y Streamlit.
Autoría declarada en el código recibido: **Hannia Macias Gómez**; se conserva.
Repositorio preparado en la cuenta Selezer33 a petición del usuario.

## Ejecutar

Desde la carpeta de este repositorio, con Python 3.12:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run ViajeUber.py
```

El archivo de entrada para un futuro despliegue es `ViajeUber.py`.
Ejecutar desde esta carpeta es necesario por las rutas relativas de algunos JSON.
No se ha desplegado esta aplicación en Streamlit Community Cloud.

## Verificación

```powershell
python -m unittest discover -s tests -v
```

Consulta [la revisión de la lista de cotejo](REVISION_COTEJO.md).
**La práctica no cumple todavía todos los indicadores.**
Las pruebas se ejecutan sobre una copia temporal para no modificar datos del proyecto.
