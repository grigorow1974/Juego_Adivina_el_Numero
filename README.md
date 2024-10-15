# Adivina el Número - Juego en Python

Este es un sencillo juego de adivinanza donde el jugador debe intentar adivinar un número secreto dentro de un rango. El juego puede jugarse en modo solitario o con dos jugadores, y ofrece diferentes niveles de dificultad. Al finalizar, se almacenan estadísticas de las partidas, incluyendo el nombre del jugador, el nivel, el resultado y el número de intentos usados.

## Características

- **Modos de juego:**
  - Modo Solitario
  - Modo 2 Jugadores
- **Niveles de dificultad:**
  - Fácil (20 intentos)
  - Medio (12 intentos)
  - Difícil (5 intentos)
- **Estadísticas almacenadas:**
  - Jugador
  - Nivel de dificultad
  - Resultado (Ganó/Perdió)
  - Número de intentos usados

## Requisitos

Este proyecto requiere Python 3.x y las siguientes bibliotecas:

- `pandas`
- `openpyxl` (para manejar archivos Excel)

## Funcionamiento del Juego
  - Modo Solitario: El jugador debe adivinar un número generado aleatoriamente por la computadora entre 1 y 1000.
  - Modo 2 Jugadores: Un jugador ingresa un número secreto entre 1 y 1000, mientras que el otro jugador debe adivinarlo.
  - Niveles de Dificultad: Cada nivel define el número de intentos que el jugador tiene para adivinar el número secreto.
  - Al final de cada partida, se guarda el resultado en un archivo Excel (estadisticas.xlsx), y las estadísticas pueden ser consultadas directamente desde el menú principal.

## Estadísticas
Al seleccionar la opción de "Estadística" desde el menú principal, el juego solicita tu nombre y te muestra tus partidas guardadas, incluyendo:

  - Nivel de dificultad
  - Resultado (si ganaste o perdiste)
  - Número de intentos usados

## Contribuir

Si deseas contribuir a este proyecto, puedes seguir los siguientes pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -m 'Añadir nueva funcionalidad').
Haz push a la rama (git push origin feature/nueva-funcionalidad).
Abre un Pull Request en GitHub.
