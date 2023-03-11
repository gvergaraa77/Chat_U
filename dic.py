oracion='''
Si deseas más información sobre la ruta contra la violencia de la Universidad de la Guajira, visita nuestra página web: https://www.uniguajira.edu.co \n
Si quieres otra información, puedes seleccionar otro número de la lista. \n
Si deseas terminar la conversación, escribe 'fin'. \n
'''
cuestionario='''
¡Excelente! ¿Qué información deseas conocer?\n
1. ¿Qué es la Ruta contra la violencia?\n
2. ¿Dónde puedo comunicarme dentro de la universidad para hacer una denuncia?\n
3. ¿Dónde puedo comunicarme si no estoy en la universidad?\n
4. ¿Cómo puedo saber si soy víctima de violencia?\n
5. ¿A qué tienen derecho las víctimas de violencia?\n
6. ¿Qué casos de violencia se atienden en la Universidad?\n
7. ¿Qué otros tipos de violencia existen?\n
8. ¿Qué pasa luego de la denuncia?\n
9. ¿Qué puedo hacer si no estoy de acuerdo con la decisión de la universidad?\n
10. ¿Qué puedo hacer si no estoy de acuerdo con la decisión de la universidad?\n

Por favor escribe el número de la información que deseas conocer seguido de un espacio y tu documento de identidad. Por ejemplo: 7 1048316285
'''
dic1={
    "hola":'''
¡Hola! Bienvenido a la ruta contra la violencia de la Universidad de la Guajira, le habla su amigo virtual SICV, mucho gusto en conocerte. ¿Deseas que te brinde alguna información?\n Responde 'Sí' para recibir la información o 'No' si gustas terminar la conversación :D.
''',
    "no":'''
¡Gracias por tu tiempo! Escríbenos pronto.
''',
    "si":'''
Listo! antes de brindarte la información nos gustaría que aceptarás nuestra política de tratamiento de datos. Si deseas aceptar y continuar con la conversación, responde 'aceptar', en caso contrario, escribe 'no'.\n
''',
    "aceptar":cuestionario,
"fin": '''
¡Gracias por tu tiempo! Nos sería de mucha utilidad si visitas el siguiente link para darnos tu opinión sobre el servicio brindado: https://www.uniguajira.edu.co  \n ¡Nos vemos pronto!
''',
}
dic2={   
    "1": '''
    Es una medida procedimental con información pertinente sobre los tipos de violencia, estamentos públicos e institucionales vinculados a la atención, denuncia, acompañamiento y seguimiento y sus formas de contacto como forma de prevención y protección frente a las mujeres víctimas de cualquiera de los casos contemplados dentro del marco de la política y protocolo sobre equidad de género para la mujer en la Universidad de la Guajira.
    ''',
    "2": '''
Oficina desarrollo humano
Área de Bienestar Social Universitario
Al lado de la cafetería principal

Correo
bienestarmigra@uniguajira.edu.co
''',
"3": '''
Línea 123
Todos los servicios de emergencias disponibles en el país

Linea 155
Orientación para mujeres víctimas de violencia

Línea 018000522020
Denuncia para el delito de trata de personas

Centro de atención integral de las víctimas de violencia sexual
Calle 12, No # 12-89

Fiscalía
122.018000919748
denunciaanonima@fiscalia.gov.co
Denuncia para casos de violencia sexual e intrafamiliar

Unidades de reacción inmediata (URI)
Atención de casos de violencia basados en género
Contacto: 318 3472087
Dirección: Palacio de Justicia, 2 piso 
Cll. 7, Cra 15.
    ''',
"4":'''
¡Cuidado! La violencia aumentará
1 Bromas hirientes 
2 Silenciar, prohibir las expresiones 
3 Chantajear 
4 Engañar 
5 Ignorar, ley del hielo 
6 Celar 
7 Culpabilizar 
8 Descalificar 
9 Ridiculizar, ofender 
10 Humillar en público
11 Indicar cómo vestir o maquillar 
12 Rompe objetos 
13 Controlar 

¡Reacciona! No te dejes destruir 
14 Prohibir usar métodos anticonceptivos
15 Controlar dinero que no le pertenece
16 Destruir objetos personales
17 Manosear sin consentimiento
18 Caricias agresivas 
19 Golpear “jugando” 
20 Pellizcar, rasguñar 
21Empujar, jalonear 
22 Cachetear 
23 Patear 
24 Encerrar, aislar 

Urge ayuda profesional 
25 Acoso, hostigamiento 
26 Amenazar con objetos o armas 
27 Amenazas de muerte
28 Forzar la relación 
29 Abuso sexual 
30 Violar 
31 Mutilar
32 Secuestro 
33 Asesinar 
''',

"5": '''
-Atención integral mediante servicios con cobertura suficiente, accesible.
-Recibir orientación, asesoramiento jurídico y asistencia técnica legal con carácter gratuito, inmediato y especializado.
-Recibir información clara, completa, veraz y oportuna con relación con sus derechos, los mecanismos y procedimientos contemplados en las leyes. 
-Dar su consentimiento informado para los exámenes médico-legales en los casos de violencia sexual y escoger el sexo del facultativo para la práctica de los mismos dentro de las posibilidades ofrecidas por el servicio. 
-Recibir información clara, completa, veraz y oportuna en relación con la salud sexual y reproductiva. 
-Ser tratada con reserva de identidad al recibir la asistencia médica, legal, o asistencia social respecto de sus datos personales. 
-Recibir asistencia médica, psicológica, especializada e integral en los términos y condiciones establecidos en el ordenamiento jurídico. 
-La verdad, la justicia, la reparación y garantías de no repetición frente a los hechos constitutivos de violencia. 
-A decidir voluntariamente si puede ser confrontada con el agresor en cualquiera de los espacios de atención y en los procedimientos administrativos, judiciales o de otro tipo. 
''',
"6":'''
Acoso o Bullying
Acciones físicas o psicológicas, con pretensión de hacer daño y repetidas en el tiempo, que se dirigen a una persona que no puede defenderse, sufriendo exclusión y soledad

Acoso virtual o cyberbullying
Hostigamiento a través de redes sociales o medios virtuales como por ejemplo mensajes de texto, correos electrónicos, la publicación de fotos o imágenes con el fin de humillar o maltratar a otro, mensajes degradantes, burlas, insultos, chismes, ofensivos, amenazas, creación de grupos para agredir o burlarse de una persona

Discriminación
El que arbitrariamente se impida, obstruya o restrinja el pleno ejercicio de los derechos de las personas por razón de su raza, nacionalidad, sexo u orientación sexual, discapacidad y demás razones

Hostigamiento 
Por causas raza, etnia, identidad de género y orientaciones sexuales no normativas: referida a la exposición de personas pertenecientes a grupos étnicos minoritarios o a los sectores LGBTI, etc.

Violencia basada en el género
Prácticas que busquen atentar contra la integridad de una persona, sin importar el nivel de afectación o gravedad, sustentadas en la idea de su pertenencia a un género (mujeres u hombres) o por no cumplir lo que se espera de este en el plano de lo social

Violencia sexual
Acto sexual o la tentativa de consumar un acto sexual, comentarios o insinuaciones sexuales no deseados, o las acciones para comercializar o utilizar de cualquier otro modo la sexualidad de una persona

Abuso sexual
Está relacionado con las circunstancias que ubican al agresor en una situación de superioridad o ventajosa frente a la víctima. Las circunstancias de superioridad pueden ser por relaciones de autoridad o poder, edad, incapacidad física o psicológica de la víctima entre otras
''',
"7": '''
-Feminicidio: Se considera feminicidio la muerte de una mujer por ser mujer o por su identidad de género (mujer trans). El feminicidio no solo ocurre cuando se odia a las mujeres sino también cuando la violencia es empleada como medio para ejercer control sobre la mujer, sus decisiones vitales, su sexualidad; cuando la violencia es empleada como medio de represión o castigo por el ejercicio de sus derechos. Hay feminicidio cuando la mujer es instrumentalizada, disciplinada o cosificada mediante la violencia. El feminicidio se produce en contextos de diminución pública o privada, por lo que la ley penal desarrolla circunstancias indicativas que sirven de ayuda para entender que se ha producido, pero que no son taxativas ni se requieren para que se entienda la real ocurrencia de dicho delito 
-Violencia física: Es un acto que intenta provocar o provoca dolor o daño físico. Se presenta a traves de diversos actos de agresión como: golpes, quemaduras, patadas. puñetazos, mordiscos, entre otros. En su forma más extrema, la violencia física lleva al homicidio. 
-Violencia verbal: Comprende el menosprecio en privado o en presencia de otras personas, ridiculización, uso de malas palabras, insultos, amenazas, entre otros.  
-Violencia sexual: Se refiere a acciones como la violación o intento de violación, actividades sexuales forzadas, y en el caso de las mujeres, abuso en relación la reproducción (embarazo forzado, aborto forzado, esterilización forzada)
-Violencia psicológica: Comprende conductas amenazantes, que no necesariamente implican violencia física o verbal, o conductas como ignorar, descuidar intencionalmente, aislar a la persona, retener información, entre otras. 
-Violencia socioeconómica: Incluye acciones como quitarle a la víctima sus ganancias, no permitirle tener un ingreso separado (condición de “ama de casa” forzada, trabajo no remunerado en el negocio familiar), o ejercer violencia física que la incapacite para el trabajar. 
-Violencia institucional: La violencia institucional contra la mujer se da por parte de las autoridades encargadas de la ruta de atención y de materializar sus derechos, al no aplicar los enfoques de género, al desconocer sus competencias relacionadas con la protección integral de la mujer, al naturalizar las violencias e invisibilizar las violencias emocionales y al revictimizar a través de patrones de desigualdad y discriminación. Las autoridades deberán administrar justicia con perspectiva de género y garantizar el acceso a la justicia sin discriminaciones, teniendo en cuenta las medidas de protección establecidas en la Ley 1257 de 2008. 
-Violencia Intrafamiliar: La Ley 294 de 1996 y la Ley 575 de 2000 determinaron que este tipo de violencia se configura cuando una persona, dentro de su contexto familiar, es víctima de daño físico o psíquico, amenaza, agravio, ofensa o cualquiera otra forma agresión por parte de otro miembro del grupo familiar. 

Para efectos de la Ley 294 de 1996, integran la familia: 
a. Cónyuges o compañeros permanentes. Esta expresión también se aplica a los integrantes de las parejas del mismo sexo. 
b. El padre y las madres de la familia, aunque no convivan en un mismo hogar.
c. Los ascendientes o descendientes de los anteriores y los hijos adoptivos. 
Todas las demás personas que de manera permanente se hallaren integrados a la unidad doméstica.

De acuerdo con lo señalado por la Ley 1959 de 2019 modificó el articulo 229 de la Ley 599 de 2000 y amplió el concepto y alcance del delito de violencia intrafamiliar, el cual se amplió a: 
a. Los cónyuges o compañeros permanentes, aunque se hubieren separado o divorciado
b. El padre y la madre de familiar, aun cuando no convivan en el mismo hogar, si el maltrato se dirige contra el otro progenitor. 
c. Quien, no siendo miembro del núcleo familiar, se encargado del cuidado de uno o varios miembros de una familiar en su domicilio, residencia o cualquier lugar en el que se realice la conducta. 
''',
"8": '''
-Denuncia de la presunta situación violenta
-Recepción de la denuncia de parte de cualquiera de los estamentos
-Atención e intervención
-Remisión por parte de bienestar a las oficinas de apoyo 
-Direccionamiento a entidades externas si es el caso
-Seguimiento a las acciones emprendidas 
-Campus libre de violencia 
''',
"9": '''
Según La OMS, la violencia repercute en la educación, la salud y el bienestar de las víctimas a lo largo de toda su vida. Asimismo, y dentro del marco educativo la exposición a la violencia puede ocasionar un bajo rendimiento académico debido a problemas cognitivos, emocionales y sociales. En ese sentido, para las instituciones educativas es vital contar con medidas de prevención y protección para generar un proceso que enseñe e instruya la comunidad educativa y proporcione una serie de servicios que garanticen la promoción de los derechos sexuales y reproductivos y la prevención de la violencia de género, sentando las bases que conduzcan a lograr un campus universitario más equitativo y pacífico, y en mayor medida a la sociedad Guajira.
''',
"10": '''

''',
}

