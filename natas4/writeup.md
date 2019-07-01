# Natas 4

Al entrar vemos que la página dice:

```
Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/" 
```

Es decir, los usuarios autorizados deben venir de la url `http://natas5.natas.labs.overthewire.org/`

Cada vez que ingresamos a una página, el navegador efectúa un request de tipo GET solicitando al servidor la página que queremos visitar. Este request tiene [cabeceras o encabezados](https://es.wikipedia.org/wiki/Anexo:Cabeceras_HTTP) (headers) con información relativa al pedido. Hay una cabecera opcional, [referer](https://es.wikipedia.org/wiki/Referer_(Cabecera_HTTP)), que guarda la dirección desde la cual estamos solicitando la nueva página. En otras palabras, la dirección a la que iríamos si presionamos el botón atrás del navegador.

Esto sugiere la siguiente idea: si editamos ese valor en el pedido que el navegador realiza, podemos hacer creer al servidor que visitamos la página siguiendo un link desde otra página. En este caso, podríamos poner que venimos de la url del desafío natas5.

## Editando un request http

Es común usar programas denominados proxies, que interceptan el tráfico de nuestro navegador antes de que vaya al servidor y permiten editarlo. Son muy útiles para testear y encontrar vulnerabilidades en aplicaciones y páginas web. Dos muy conocidos son [burp](https://portswigger.net/burp) y [zap](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project). Burp es pago pero sus funcionalidades de prueba alcanzan para cosas sencillas. Zap es gratuito.

En este caso, como la modificación del request es muy sencilla, podemos hacerla también directamente desde el navegardor. Los pasos que siguen estan descriptos para Firefox, pero se puede hacer de forma similar en Chrome u otro navegador. Para ello, hay que entrar a la página de natas4 y abrir las herramientas de desarrollador con <kbd>F12</kbd>. Luego vamos a red, y clickeamos sobre el primer request de tipo GET (puede ser necesario recargar la página para verlo). A la derecha se abre un panel donde se puede ver información sobre el request. En la pestaña encabezados, podemos ver los encabezados del request y editarlos presionando el botón <kbd>Editar y reenviar</kbd>. Agregamos al final de los encabezados: `Referer: http://natas5.natas.labs.overthewire.org/`, en una nueva línea, y presionamos enviar. Esto va a agregar un nuevo request GET a la lista del panel de la izquierda. Si lo inspeccionamos haciendo click, en el panel de la derecha veremos que tiene el encabezado `Referer` que añadimos manualmente. En la pestaña respuesta, veremos la respuesta del servidor con la clave del siguiente nivel.
