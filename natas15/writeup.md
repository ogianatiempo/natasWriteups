# Natas 15

El desafío nos permite ver el código fuente. Podemos ver que el formulario pasa el parámetro username usando un request de tipo POST:

```html
<form action="index.php" method="POST">
Username: <input name="username"><br>
<input type="submit" value="Check existence" />
</form>
```

En particular nos interesa el principio del código php, que contiene la consulta que se va a realizar a la base de datos empleando la información del formulario:

```php
if(array_key_exists("username", $_REQUEST)) {
    $link = mysql_connect('localhost', 'natas15', '<censored>');
    mysql_select_db('natas15', $link);

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysql_query($query, $link);
    if($res) {
    if(mysql_num_rows($res) > 0) {
        echo "This user exists.<br>";
    } else {
        echo "This user doesn't exist.<br>";
    }
    } else {
        echo "Error in query.<br>";
    }

    mysql_close($link);
}
```

Podemos ver que el código pregunta si en el array `$_REQUEST` esta definida la variable `username`. De la documentación de [php](https://www.php.net/manual/es/reserved.variables.request.php) podemos ver que este array contiene los datos del request HTTP sin diferenciar el método (GET, POST o COOKIE).
Sin embargo, vemos que si mediante un request GET pasamos el parámetro debug la consulta se muestra.
Esto nos da la idea que podemos pasar tanto el nombre de usuario como activar el modo debug mediante un request GET. Por ejemplo: [http://natas15.natas.labs.overthewire.org/?username=octa&debug](http://natas15.natas.labs.overthewire.org/?username=octa&debug).

Confirmamos, como también se puede ver en el código fuente, que el parametro `username` se utiliza en la consulta directamente y se encuentra entre comillas.

Esto sugiere probar el siguiente nombre de usuario: `" or 1=1 #`.
Como en el nivel anterior, la consulta resultante devuelve siempre True (cualquier valor o 1=1 evalúa siempre a verdadero). 

> __Nota:__ si hacemos la consulta por GET, es decir a través de la url, hay que codificar el # como %23, sino no aparece en la consulta final (quedaría `" or 1=1 %23`). Más info [acá](https://www.w3schools.com/html/html_urlencode.asp).

A diferencia del nivel anterior, esta vez no nos da la clave. Pero el mensaje resultante pasa de ser `This user doesn't exist` a
`This user exists` porque la consulta es verdadera. Tenemos lo que se conoce como un oráculo, es decir que podemos evaluar el valor de verdad de expresiones si las ponemos en lugar del 1=1. Si la expresión resulta verdadera, veremos el mensaje correspondiente a que el usuario existe. Si evalúa como falsa, veremos el mensaje que dice que el usuario no existe.

Podemos probar usando normalmente la página que existe el usuario `natas16`. Suponemos que la contraseña para este usuario, que está guardada en la base en la columna password, tiene la contraseña del siguiente nivel (el código fuente muestra que esta columna existe).

## Usemos el oráculo para averiguar la contraseña:

Para esto vamos a construir una consulta usando el operardor [LIKE](https://www.w3schools.com/SQL/sql_like.asp) para preguntar si hay un usuario con nombre `natas16` y su contraseña empieza con un determinado caracter. Por ejemplo, para preguntar si comienza con a ingresariamos en username `natas16" AND password LIKE BINARY "a%" #`.

> __Nota:__ usar el tipo BINARY como modificador del texto lo hace case sensitive

- Podemos construir la siguiente url para preguntar si empieza con a: `http://natas15.natas.labs.overthewire.org/index.php?debug&username=natas16%22+AND+password+LIKE+BINARY+%22a%25%22+%23`

- o si empieza con W:
`http://natas15.natas.labs.overthewire.org/index.php?debug&username=natas16%22+AND+password+LIKE+BINARY+%22W%25%22+%23`

Y ver que efectivamente empieza con W. Esto nos da la idea de que se puede automatizar el proceso agregando un caracter por vez. Es decir, ahora que sabemos que empieza con W, ver empieza con Wa, Wb, Wc, etc. En esta carpeta pueden encontrar un script que escribí en Python para resolver este desafío usando esta idea.

Para terminar, este tipo de estrategia se conoce como blind sql injection. La idea general es que si encontramos algo que cambie en la respuesta del servidor según el valor de verdad del resultado de la consulta realizada y logramos una forma de modificar dicha consulta, podemos hacer preguntas a la base que evaluen a verdadero o falso para conseguir información. Cuando no encontramos algo que cambie en la respuesta se puede recurrir a ataques basados en tiempo. Más info [acá](https://www.owasp.org/index.php/Blind_SQL_Injection#Time-based).

Para detectar si algún parámetro de un request es vulnerable a sql injection se puede usar [sqlmap](http://sqlmap.org/). Para explotarlo de forma automatizada como hicimos, hay herramientas como [wfuzz](https://wfuzz.readthedocs.io/en/latest/).

> __Nota:__ En este caso se podía ver en el códgo fuente que la columna password estaba en la tabla. Pero si no lo supiéramos también se pueden averiguar los nombres de las columnas y las tablas de la base con este métedo modificando un poco la consulta.
