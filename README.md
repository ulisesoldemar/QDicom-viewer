# QDicom-viewer

Visualizador de imágenes DICOM

## Instalación

### Dev
Python, Qt ([PySide2](https://pypi.org/project/PySide2/)) y 
[pipenv](https://docs.pipenv.org/) fueron usados para el desarrollo. 
Revisar [Pipfile](Pipfile), [Pipfile.lock](Pipfile.lock), 
y [requirements.txt](requirements.txt) para las especificaciones 
completas de Python y las dependencias necesarias. Para reproducir 
el entorno, es necesario ejecutar `pip install -r requirements.txt` 
con la [version de python](Pipfile.lock#L8). 
Se recomienda usar [virtualenv](https://virtualenv.pypa.io/en/stable/).

### Prerequisitos

* **PySide2 >= 5.15.2.1** para el entorno gráfico.

## Uso

Ejecutar el script [mainwindow.py](mainwindow.py) para iniciar el entorno gráfico:
```bash
python mainwindow.py
```

## Licencia

[GPL](LICENSE)
