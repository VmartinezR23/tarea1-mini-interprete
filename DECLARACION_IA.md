# Declaración de uso de Inteligencia Artificial

**Actividad:** Tarea 1
**Integrantes:** Victor Martínez Reyes
**Fecha:** 19-oct-2026

> Esta declaración es obligatoria en toda tarea, práctica y en el proyecto final.
> **No da ni quita puntos**: es un reporte adicional que se revisa aparte y se
> devuelve con comentarios. **No se evalúa cuánta IA usaron**, sino si pueden
> dar cuenta de lo que entregaron.

---

## 0. ¿Se usó IA en esta actividad?

- [ ] **No.** Firmen la última sección y terminen. Con eso queda completa.
- [ ° ] **Sí.** Contesten los cinco puntos.

---

## 1. Herramienta(s) utilizada(s)

| Herramienta | Versión o modelo, si lo saben |
|ChatGPT| GPT-6|
| | |

> Cuenta también el autocompletado del editor (Copilot y similares). Si sólo
> fue eso, basta con decirlo en un renglón y seguir al punto 4.

---

## 2. Objetivo del uso

| Para qué la usamos | En qué parte del entregable |
|La utice para las dudas que tenia en algunos pasos con git y para aprender más sobre el, ademas de para automatizar y hacer un poco más rapido la parte 2.1 (que escribiera el nombre de cada prueba para no colocar uno por uno)| 2.1 y en el pull request (ya que tenia dudas del proceso)|
| | |

> Sean específicos. *"Para la tarea"* no dice nada.
> *"Para generar las pruebas de `minimo_de_llaves`"* sí.

---

## 3. Prompts principales

Textuales, tal como los escribieron. No los limpien ni los reescriban.
```

(prompt 1)
```
hola chat, cómo funciona una rama en git y como se fusiona esta con el main
```
(prompt 2)
```
que significa?
python3 -m venv venv
source venv/bin/activate

```
(prompt 3)
```
dame el copiar y pegar en el formato que te proporcione de estas pruebas (solo agrega el nombre de la prueba)
def test_suma():
    assert interpretar("3 + 4") == 7
def test_resta():
    assert interpretar("10 - 3") == 7
def test_multiplicacion():
    assert interpretar("6 * 7") == 42
def test_division():
    assert interpretar("10 / 2") == 5
def test_precedencia_sin_parentesis():
    assert interpretar("3 + 4 * 2") == 11
def test_precedencia_con_parentesis():
    assert interpretar("(3 + 4) * 2") == 14
---

## 4. Cómo se incorporó o se descartó lo obtenido

**Éste es el punto que más pesa.**

| Qué produjo la herramienta | ¿Aceptado, modificado o descartado? | Por qué | Dónde quedó (archivo / commit) |
|infromación sintetizada acerca de git|parcialmente aceptado ya que termine investigando más a fondo por otro medio| me parecio que la información era un poco general y no abarcaba tanto como yo queria para lograr entender | en un apunte aparte|
|la definicion de cada prueba en el formato para el README|aceptado|era correcta la informacion y era algo que no influia en el codigo u otra parte de importancia| en ANALISIS.md|
| | | | |

> **"Lo descartamos" es una respuesta excelente**, si dicen por qué.
> Una declaración donde todo se aceptó sin cambios es una declaración que
> no muestra criterio.

### 4.1 Si la usaron para el análisis: el contraste

Se les pidió intentarlo primero por su cuenta. Si lo hicieron así:

no aplica

| | |
|---|---|
| ¿Qué encontró la herramienta que ustedes **no** habían notado? | |
| ¿Qué **no** encontró, que en este curso sí consideramos un problema? | |

> La segunda es la que más nos interesa. Una herramienta suele no señalar la
> duplicación de código, porque el programa funciona igual. Ustedes ya saben
> por qué eso sí importa.
>
> Si no usaron IA para el análisis, escriban *"no aplica"*.

### 4.2 ¿Cómo verificaron que lo que incorporaron era correcto?

Analice que cada caso estuviera excatamente como en los archivos test y que tuviera el formato establecido para integrarlo de una correcta forma en el archivo ANALISIS.md
> Una prueba que escribieron, una ejecución, un contraste contra las notas de
> clase o contra el enunciado. *"Lo revisamos"* no es una verificación.

---

## 5. Reflexión

### 5.1 ¿Qué limitación concreta observaron **en esta actividad**?
Para información acerca de un tema hay veces que la da de manera "general" por lo que si quieres saber algo más detallado tienes que o preguntarle de nuevo o investigar en otro sitio
> Concreta. No *"a veces se equivoca"*, sino *"propuso pruebas sólo para
> m = 4 y nunca para órdenes impares, porque no conocía la definición del
> laboratorio"*.

### 5.2 ¿Qué harían distinto la próxima vez?

Investigar de forma independiente la infromación necesaria que vaya a ocupar y en todo caso, usar solamente la IA para hacer procesos repetitivos los cuales sean faciles de identificar que lo que entrega este correcto para agregarlo al proyecto.
---

## Firma

Victor Martinez Reyes

> Declaramos que entendemos y podemos explicar todo lo que entregamos,
> independientemente de las herramientas que hayamos utilizado.

| Nombre | Número de cuenta |
|Victor Martinez Reyes| 323144834|
| | |
