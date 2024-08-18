ANTES DE COMENZAR: Asegure que en el <<platformio.ini>> seleccione su dipositivo: 
Para las varitas dos modelos son utilizados el ESP32-S3 y el ESP32-C3.

Si su dispositivo es C3:

[env:lolin_c3_mini]

platform = espressif32

board = lolin_c3_mini


Si su dispositivo es S3:

[env:lolin_s3_mini]

platform = espressif32

board = lolin_s3_mini


Ademas cambiar los IO de los botones.
El GY521 esta conectado a los pines I2C defecto de su dispositivo, para mayor informacion de que pines son consulte la hoja de datos de su dispositivo.
La direccion default del GY521 es (0x68) y la alterna en caso de que no funcione la default es la (0x69)


![image](https://github.com/user-attachments/assets/d076ea9f-7035-48fc-9074-379cb54fd162)


![image](https://github.com/user-attachments/assets/a9512727-2cdd-49a5-8e8e-41c0c6a3a3f5)

¿Como funciona el ejemplo?

Si todo funciona de manera correcta en la terminal a 115200 baudios deberia poder observar la salida del GY521. Al ser presionado el boton debe encender el LED que se encuentra en la cabeza de la varita. Ejemplo:
![IMG_3368](https://github.com/user-attachments/assets/0393371c-87f1-4b95-b10b-5476692fc6e6)


