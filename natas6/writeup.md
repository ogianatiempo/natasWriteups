# Natas 6

En este caso cambia un poco la onda del desafío. Hay un link que nos permite ver el código fuente de la página. En el código hay un [formulario html](https://www.w3schools.com/html/html_forms.asp) que manda por método POST información que podemos ingresar:

```html
<form method=post>
Input secret: <input name=secret><br>
<input type=submit name=submit>
</form>
```

Vemos que el parámetro que manda se llama `secret` y contiene el texto que ingresamos en el recuadro para ingresar texto.

Además, vemos que la página contiene código php. Este código no lo podemos ver presionando <kbd>F12</kbd> porque se evalúa en el servidor y al usuario le llega el resultado de dicha evaluación. Pero el desafío da la ventaja de conocerlo:

```php
<?

include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>
```

Por un lado vemos que usa un [include](https://www.php.net/manual/es/function.include.php). Esto incluye y __evalúa__ el código de otro archivo, que en este caso es `secret.inc`. Por otro lado, pregunta si en el array `$_POST` existe la clave `submit`.

El [array post](https://www.php.net/manual/es/reserved.variables.post.php) es un array asociativo, es decir que tiene claves y valores asociados a dichas claves, que contiene la información recibida por medio del request de tipo `POST`. Podemos ver esta información viendo el request desde la vista de desarrollador como hicimos en otros desafíos luego de enviar información mediante el formulario. En este caso enviamos como Input secret la letra a. Se puede ver que el método del request es efectivamente `POST` y en el cuerpo del request se envía la información `secret=a&submit=Enviar+Consulta`. La clave `submit` existe en el cuerpo del request y en el array cuando se llega a la página presionando el botón para enviar el formulario porque el mismo tiene como nombre `submit`. El valor de esta clave suele ser el texto del botón. Como el mismo puede variar, el código sólo pregunta si la clave existe.

Si la clave `submit` existe, el código asume que se llegó a la página a través del formulario y compara el valor del campo de texto del formulario, que se encuentra en el array `$_POST` asociado a la clave `secret`, con la variable `$secret`. Si coinciden, muestra la contraseña del siguiente nivel.

No vemos en el código la definición de la variable `$secret` por lo que podemos suponer que esta en el archivo incluido.

Si intentamos ver el archivo con el navegador yendo a `natas6.natas.labs.overthewire.org/includes/secret.inc` vemos que la página esta vacía. Si la clave está definida en el código php, como el código se evalúa en el servidor, no la podríamos ver y habría encontrar la forma de acceder al código o lograr imprimir el valor de la variable. Por ejemplo, como el archivo parece ser accesible podríamos tratar de incluirlo en un archivo php de nuestra creación para luego imprimir la variable.

En este caso, si exploramos el código fuente de `secret.inc` podemos ver el valor de la variable `$secret` en un comentario html. Si volvemos al formulario e ingresamos ese valor, podremos ver la clave del siguiente nivel.
