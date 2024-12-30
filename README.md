Te propongo una versión actualizada del README que incluye la información sobre la instalación del paquete:

```markdown:README.md
# Orbea Monegros 2024 - Data Analysis

Este proyecto es el entregable de la PEC4 de la asignatura "Programación para la Ciencia de Datos" del Máster Universitario en Ciencia de Datos de la UOC. El proyecto analiza los datos de la prueba de ciclismo Orbea Monegros 2024, incluyendo análisis de participantes, tiempos y clubs ciclistas.

## Estructura del Proyecto

```
monegros/
├── data/
│   └── dataset.csv
├── img/
│   └── histograma.png
├── src/
│   ├── __init__.py
│   ├── ex1_data.py
│   ├── ex2_anonymize.py
│   ├── ex3_histogram.py
│   ├── ex4_clubs.py
│   └── ex5_ucsc.py
├── tests/
│   ├── __init__.py
│   ├── test_ex1.py
│   ├── test_ex2.py
│   ├── test_ex3.py
│   ├── test_ex4.py
│   └── test_ex5.py
├── main.py
├── setup.py
├── README.md
├── LICENSE
└── requirements.txt
```

## Instalación

### Prerequisitos
1. Crear y activar un entorno virtual:
```bash
python -m venv PEC4
.\PEC4\Scripts\activate  # Windows
source PEC4/bin/activate  # Linux/Mac
```

### Opción 1: Instalación en modo desarrollo
```bash
# Instalar en modo desarrollo
pip install -e .
```

### Opción 2: Instalación desde distribución
```bash
# Instalar desde el archivo wheel generado
pip install monegros-analysis

### Opción 3: Instalación manual de dependencias
```bash
# Instalar dependencias
pip install -r requirements.txt
```

### Verificar instalación
```bash
python -c "import monegros; print(monegros.__version__)"
```

## Uso

### Ejecutar todos los ejercicios:
```bash
python main.py
```

### Ejecutar un ejercicio específico:
```bash
python main.py --exercise 1  # Para ejecutar solo el ejercicio 1
```

## Ejercicios

1. **Importación y EDA**: Carga inicial de datos y análisis exploratorio.
2. **Anonimización**: Protección de datos personales y limpieza.
3. **Análisis de Tiempos**: Histograma de tiempos agrupados.
4. **Análisis de Clubs**: Estandarización y análisis de clubs ciclistas.
5. **Análisis UCSC**: Estudio específico del club UCSC.

## Tests

### Ejecutar todos los tests:
```bash
pytest
```

### Ejecutar tests de un ejercicio específico:
```bash
pytest monegros/tests/test_ex1.py  # Para el ejercicio 1
```

### Verificar cobertura:
```bash
pytest --cov=monegros.src monegros\tests\
```

### Verificar estilo de código:
```bash
pylint src/*.py
```

## Estructura de Datos

El archivo CSV contiene las siguientes columnas:
- dorsal: Número de dorsal del ciclista
- biker: Nombre del ciclista
- club: Club ciclista
- time: Tiempo de finalización (formato HH:MM:SS)

## Autor

Pablo Jiménez Cruz


