# Sistema de Gestión de Países

Sistema de gestión de datos de países con operaciones CRUD, filtros, ordenamiento y estadísticas.

## Requisitos

- Python 3.10 o superior
- Archivo CSV con formato: `PAIS,POBLACION,SUPERFICIE EN KILOMETROS CUADRADOS,CONTINENTE`

## Uso
```bash
python main.py
```

## Estructura del CSV
```csv
PAIS,POBLACION,SUPERFICIE EN KILOMETROS CUADRADOS,CONTINENTE
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
```

## Arquitectura del Proyecto
```
proyecto/
│
├── main.py                 # Archivo principal con todas las funciones
├── paises.csv             # Base de datos (generado automáticamente)
└── README.md              # Documentación
```

### Módulos Funcionales

**Persistencia de Datos**
- `cargar_paises_desde_csv()` - Carga datos al iniciar
- `guardar_paises_en_csv()` - Guarda cambios automáticamente
- `abrir_archivo()` - Manejo de archivos
- `validar_encabezado()` - Valida formato CSV
- `procesar_linea()` - Procesa cada registro

**Operaciones CRUD**
- `agregar_pais()` - Crea nuevos países
- `actualizar_datos_poblacion_superficie()` - Modifica datos
- `verificar_pais_existe()` - Valida duplicados

**Búsqueda y Filtrado**
- `buscar_pais_nombre()` - Búsqueda por nombre
- `filtrar_paises_por_rango()` - Menú de filtros
- `filtrar_por_continente()` - Filtra por continente
- `filtrar_por_rango_poblacion()` - Filtra por población
- `filtrar_por_rango_superficie()` - Filtra por superficie

**Ordenamiento**
- `paises_ordenados_por_rango()` - Menú de ordenamiento
- `ordenar_por_nombre()` - Orden alfabético
- `ordenar_por_poblacion()` - Orden por población
- `ordenar_por_superficie()` - Orden por superficie
- `ordenar_por_campo_texto()` - Bubble sort para texto
- `ordenar_por_campo_numerico()` - Bubble sort para números

**Estadísticas**
- `estadistica_paises_cargados()` - Dashboard de estadísticas
- `validar_formato_nombres()` - Valida mayúsculas/minúsculas
- `obtener_pais_mayor_poblacion()` - Máximo
- `obtener_pais_menor_poblacion()` - Mínimo
- `calcular_promedio_poblacion()` - Promedio poblacional
- `calcular_promedio_superficie()` - Promedio superficial
- `contar_paises_por_continente()` - Agrupación por continente

**Utilidades**
- `convertir_a_entero()` - Validación numérica
- `calcular_densidad_poblacional()` - Cálculos adicionales
- `mostrar_menu()` - Interfaz principal

## Funcionalidades

1. **Agregar país**: Ingresa nuevo país con validaciones
2. **Actualizar datos**: Modifica población y/o superficie
3. **Buscar país**: Búsqueda por nombre (coincidencia parcial)
4. **Filtrar países**: Por continente, población o superficie
5. **Ordenar países**: Por nombre, población o superficie
6. **Estadísticas**: Mayor/menor población, promedios, países por continente
7. **Salir**: Cierra el programa

## Características Técnicas

- Sin clases, lambdas ni excepciones
- Sin variables globales
- Funciones modulares (una responsabilidad por función)
- Persistencia automática en CSV
- Validaciones completas de datos
- Algoritmo Bubble Sort para ordenamiento
- Búsqueda por coincidencia parcial (case insensitive)

## Flujo de Datos
```
Inicio → Cargar CSV → Menú Principal
                          ↓
         ┌────────────────┼────────────────┐
         ↓                ↓                ↓
    Operaciones      Consultas        Estadísticas
         ↓                ↓                ↓
    Guardar CSV      Mostrar          Mostrar
         ↓                              
    Menú Principal ←──────────────────────┘
```



## Autores

Ariel Gibbon
José Ricardo Miranda
