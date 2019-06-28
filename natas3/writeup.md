# Natas 3

Como en los niveles anteriores, accedemos al código fuente con <kbd>F12</kbd>. Esta vez encontramos un comentario `No more information leaks!! Not even Google will find it this time...`

Los buscadores indexan los sitios web de forma automatizada. Existe una [forma estándar](https://en.wikipedia.org/wiki/Robots_exclusion_standard) para solicitar que ciertos directorios o archivos no se indexen. Para ello se usa un archivo llamado robots.txt. Al ingresar a http://natas3.natas.labs.overthewire.org/robots.txt vemos lo siguiente:

```
User-agent: *
Disallow: /s3cr3t/
```

De esa forma se indica que no se indexe el directorio `s3cr3t`. Si vamos a ese directorio, podemos encontrar un archivo con la clave del nivel siguiente.

## Otra forma: Google dorks

La idea es usar la búsqueda de Google con operadores avanzados para encontrar archivos de configuración o con información sensible. Más info [acá](https://en.wikipedia.org/wiki/Google_hacking).

En este caso podemos Googlear: `site:http://natas3.natas.labs.overthewire.org/ filetype:txt`. Suponiendo que puede haber archivos de texto porque en el nivel anterior la contraseña estaba en un archivo de este tipo.
