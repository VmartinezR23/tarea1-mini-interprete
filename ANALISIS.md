# Análisis — Tarea 1

**Integrantes:**
1. Victor Martinez Reyes
2.
3.

**Fork:**
**Rama:**

> Contesten en este archivo. Respuestas breves y concretas: se califica que
> hayan entendido, no la extensión.

---

## 1. Arquitectura

### 1.1 ¿Cuál es la responsabilidad de cada componente?

| Componente | Qué recibe | Qué entrega | De qué es responsable |
|---|---|---|---|
| `lexer` | El texto inicial | Tokens que corresponden al texto |Identifica las partes del texto y las convierte en tokens|
| `parser` | Los tokens del lexer | Una representacion en AST |Verifica que siga la gramatica y genera un árbol de sintaxis|
| `ast` |Los valores para crear nodos | Objetos que representan numeros y operaciones  | Define la estructura de los nodos que representan números y operaciones en un AST|
| `evaluator` |El AST a evaluar| El valor resultante del AST | Evaluar el AST para entregar su valor representado en número |

### 1.2 ¿Qué recorrido sigue una expresión desde que se recibe como texto hasta que produce un resultado?

> Usen `(3 + 4) * 2` como ejemplo y muestren cómo se ve entre etapa y etapa.

| Etapa | Cómo se ve `(3 + 4) * 2` aquí |
|---|---|
| texto | `"(3 + 4) * 2"` |
| tokens |[ PAR_IZQ, NUMERO(3), MAS, NUMERO(4), PAR_DER, POR, NUMERO(2)] |
| AST |*/ \+   2/ \3   4|
| resultado | 14 |

> Para el renglón del AST, dibújenlo **primero ustedes** y después comprueben
> con `python3 interprete.py --arbol "(3 + 4) * 2"`. Si su dibujo y el del
> programa no coinciden, uno de los dos está mal, y averiguar cuál es
> justamente el trabajo.

---

## 2. Las pruebas que ya estaban

### 2.1 ¿Qué pruebas venían incluidas?

| Prueba | Componente | Comportamiento que verifica | ¿Cuántos operadores usa? | ¿Normal, frontera o inválida? |
|---|---|---|---|---|
| test_tokeniza_un_numero_solo | lexer | Verifica que un número se tokenize correctamente como numero y valor de 42 | 0 | Normal |
| test_tokeniza_una_suma | lexer | Verifica que la suma se tokenize correctamente en dos números y el signo de suma | 1 | Normal |
| test_los_espacios_no_producen_tokens | lexer | Verifica que los espacios no generen tokens | 1 | Normal |
| test_tokeniza_parentesis | lexer | Verifica que los parentesis y números se tokenizen correctamente en su tipo correspondiente | 0 | Normal |
|test_construye_el_arbol_de_una_suma | parser | Verifica que se construya el AST de la suma | 1 | normal |
|test_la_multiplicacion_se_agrupa_antes_que_la_suma | parser | Verifica la jerarquia de la multiplicacion agrupandose primero | 2 |normal |
| test_los_parentesis_cambian_la_agrupacion | parser | Verifica que los parentesis cambien segun la jerarquia y agrupacion | 2 | normal |
| test_suma | evaluator | Verifica que se evalue correctamente la suma | 1 | Normal |
| test_resta | evaluator | Verifica que se evalue correctamente la resta | 1 | Normal |
| test_multiplicacion | evaluator | Verifica que se evalue correctamente la multiplicación | 1 | Normal |
| test_division | evaluator | Verifica que se evalue correctamente la division | 1 | Normal |
| test_precedencia_sin_parentesis | evaluator | Verifica el resultado con el orden sin parentesis | 2 | Normal |
| test_precedencia_con_parentesis | evaluator | Verifica el resultado usando parentesis en el orden | 2 | Normal |



> Llenen la tabla **completa**, con las 13. Es tediosa a propósito: la única
> forma de saber qué no está cubierto es caracterizar sistemáticamente lo que
> sí. Cuando terminen, léanla como columna, no como renglones, y pregúntense
> qué combinación **no aparece nunca**.

### 2.2 ¿Qué comportamientos **no** estaban probados?
Que la division entre 0 lance ErrorDeEvaluacion
El menos unario sea invalido a menos que se escriba de la forma (0-x)
Que una entrada invalida sea rechazada con ErrorDeSintaxis
El mensaje de error que indique la posicion dentro del texto
Que los números que contengan  0 a la izquierda se interpreten de manera normal 
Que los operadores de misma precedencia se asocien de manera correcta a la izquierda 

> Ésta es la pregunta importante de toda la tarea. Tómense su tiempo.

---

## 3. Las pruebas que agregaron

### 3.1 ¿Cuáles son casos normales, cuáles frontera y cuáles inválidos?

| Prueba (archivo::nombre) | Entrada | Esperado | Categoría | ¿Por qué esa categoría? |
|---|---|---|---|---|
|test_parser.py::test_menos_unario_invalido| -3| ErrorDeSintaxis | inválida | Porque es un valor que del cual se espera un error|
|test_parser.py::test_parentesis_invalidos|3 + 3 () |ErrorDeSinteaxis | invalida| Los parentesis no contienen ni un número o expresion|
| test_evaluator.py :: division_entre_cero | algún numero entre cero | ErrorDeEvaluacion | Frontera | Porque verifica que el programa maneje bien la excepcion de que no se pueda dividir entre cero |
|test_lexer.py::test_numero_con_ceros_izquierda| 0023 | que sea interpretado como 23 (sin tener en cuenta los 0) | frontera |comprueba el comportamiento en el caso de los ceros a la izquierda|
|test_evaluator.py::test_division_resultado_menor_que_uno| 1 / 5 | 0.2 |frontera |Porque evalua que la divison de el resultado correcto aún siendo menor que 0|
|test_evaluator.py::test_asociatividad_izquierda|10 - 2 - 3 - 1| el resultado 4| normal | porque es un caso habitual de interpretacion |
|test_evaluator.py::test_jerarquia_operaciones| 6 + 3 * 4| 18 | normal | Porque valida el funcionamiento normal del interprete |


---

## 4. Los defectos

### 4.1 ¿Qué defecto reveló primero una prueba nueva?

### 4.2 ¿Por qué el comportamiento observado era incorrecto?

> No basta con "daba mal". Digan contra qué lo están comparando: qué regla,
> qué línea de la semántica declarada del README.

### 4.3 ¿Qué cambio realizaron?

| Defecto | Entrada que lo revela | Daba | Debería dar | Commit rojo | Commit verde |
|---|---|---|---|---|---|
| | | | | | |

### 4.4 ¿Cómo saben que la corrección es general y no sólo hace pasar ese ejemplo?

---

## 5. Diseño

### 5.1 ¿Qué duplicación o señal de mal diseño encontraron?

> Al menos dos. Usen el vocabulario de clase: duplicación, rigidez,
> acoplamiento alto, condicionales repetidos, amplificación del cambio.

### 5.2 ¿Qué refactorización realizaron, y por qué conserva el comportamiento?

> "Las pruebas siguen pasando" es parte de la respuesta, pero no toda.
> ¿Por qué el cambio es equivalente?

### 5.3 ¿Sería pertinente usar Factory Method, Adapter o ninguno?

> Justifiquen. **"Ninguno" puede ser la respuesta correcta.** Si dicen que sí,
> digan qué problema concreto resuelve y qué costo tiene. Si dicen que no,
> digan qué tendría que cambiar en el sistema para que empezara a convenir.

### 5.4 ¿Qué parte del sistema sería más difícil de modificar si se agregara un operador nuevo?

> Por ejemplo `%`. ¿Cuántos archivos hay que tocar? ¿Por qué?

---

## Antes de la declaración: inténtenlo primero ustedes

Usar IA o no es decisión de cada quien, y el curso la permite. Pero **les
pedimos, por favor, que primero hagan el análisis por su cuenta.**

No es una prueba de honestidad. Es que el orden cambia lo que aprenden:

1. **Primero ustedes.** Lean el código, corran las pruebas, escriban sus
   respuestas. Aunque queden incompletas, aunque no encuentren todo.

2. **Después, si quieren, la IA** — pero como contraste, no como sustituto.
   Y entonces contesten dos preguntas, en `DECLARACION_IA.md`:

   - **¿Qué encontró que ustedes no habían notado?**
     Eso es aprendizaje, y se declara sin ninguna pena.

   - **¿Qué *no* encontró, que en este curso sí consideramos un problema?**
     Ésta es la interesante. Una herramienta suele decir que el código
     "funciona bien" y no señalar, por ejemplo, la **duplicación** — porque
     duplicar no rompe nada, el programa corre igual. Pero ustedes ya saben
     por qué eso sí es un mal diseño, y saben nombrarlo. La herramienta no
     tomó esa clase.

> Si invierten el orden se pierden justamente lo segundo: **no se puede notar
> lo que a una herramienta le faltó si uno nunca se formó una opinión propia
> antes de preguntarle.** Y que un programa funcione no implica que esté bien
> diseñado — eso lo dijimos en clase mucho antes de esta tarea.

---

## Declaración de uso de Inteligencia Artificial

Va en `DECLARACION_IA.md`, no aquí. Es obligatoria, pero **no da ni quita
puntos**: es un reporte adicional que se revisa aparte y se les devuelve con
comentarios.

**No se evalúa cuánta IA usaron.** Se evalúa si pueden dar cuenta de lo que
entregaron. *"No usamos"* es una declaración válida y completa; *"lo
descartamos porque..."* es de las mejores respuestas posibles.
