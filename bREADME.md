# Blog + Migración

Nota: Instalar potsman

Nota: Cuando una seccion tiene paginas unicas en estilos por lo general es una pagina estatica
	ya que las dinamicas por lo general utilizan templetes donde condicionan todo para que el contenido vaya cambiando
	pero la plantilla es la misma.
	
	Siempre que vamos a implementar contenido que es dinamico empezamos con el backend.
	este va  a crear los modelos(post (con sus atributos)) que van a ser empujados a la base de datos (entendiendo como modelo la estructura de la pagina que vamos 
	a utilizar header=title - categoria, main=description etc)

20. Ahora para migrar un proyecto lo que tenemos que hacer es crear una carpeta nueva dentro de la carpeta contenedora 
	llamada blog_personal(en mi caso) Curso_DRF/blog_personal
21. Ahora en el proyecto que teniamos seleccionamos todo menos env, node_modules y package-lock.json
	y lo pegamos en blog_personal
22. Ahora en una terminal creamos nuevamente un ambiente virtual python -m virtualenv env y lo activamos
23. Ahora ejecutamos pip install -r requirements.txt
24. Ahora en otra terminal ejecutamos npm i (es como crear el ambiente virtual para react) y con esto ya tenemos nuestra migracion
25. Ahora desde el cmd nos ubicamos en cd apps (Antes de empezar publicarlo en Github y trabajamos desde staging)
26. Ahora en el cmd creamos una nueva aplicacion python ..\manage.py startapp blog (ver posicionamiento en el directorio)
27. Ahora en cmd creamos otra aplicacion llamada python ..\manage.py startapp categoty
28. Ahora le creamos un archivo a cada uno llamado urls.py
29. Ahora despues de crear los modelos vamos a hacer una migracion ejecutando cd .. y python manage.py makemigrations
	con esto se crean los modelos para las tablas
30. Ahora para hacer la migracion de estas tablas ejecutamos python manage.py migrate
31. Ahora creamos un nuevo archivo en category/ llamado serializers.py
32. Ahora creamos las vistas
33. Ahora ejecutamos python manage.py createsuperuser y creamos un super usuario y agregamos unas cuatas categorias y subcategorias
34. Ahora probamos la primera vista con postman | class ListCategoriesView
35. Ahora en blog creamos un archivo llamado serializers.py
36. 
