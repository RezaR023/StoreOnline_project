Also you can use the  following jupyter notebook file as README file:
"Django_Course1.ipynb"
-------------------------------
# <font color="blue">Django course, part 1:</font>

## <font color="blue">1- Djangot fundamentals</font>

##### Django is a free and open-source framework for building web applications with Python

#### the most popular frameworks are: 
    - Dajango
    - Flask
    - Tornado
    - Bottle
    - Falcon
    - Hug

As an example: we wanna build an application and publish it in rezabuy.com. This website will have two parts or two applications. A front-end that is the part that is loaded inside a web browser on a client machine. The back-end is the part that runs on a web server, and is resposlibe for data processing, validating business rules, etc. After pointing your browser to rezabuy.com. This address is called URL (Uniform resource locator). It is basically a way to locate a source on the interent. The source can be web page, image video, pdf, so on. Then, your browser sends a request to the server to say for example show the home page. The web sever takes this request and returns a reponse. This data exchange is defined by a protocol called HTTP, Hypertext Transfer Protcol. It defines how servers and clients can communicate.
    Two methods of sending reponse to the clients: One option is to generate the requested page (HTML) on the server and return it to the client. We use HTML (Hypertext Markup Language, a simple language for representing web pages and their content). So, in other hand, one option is to generate the web page on the server and return an HTML document to the clients. The other option is to return only data (like the list of products) needed on the requested page and have the client to generate the page.
    So, In the second case, the server essentially become a gateway to the data. On the server, we can provide endpoints that the clients can talk to, to get or save various pieces of data. So, we can provide an endpoint to get the list of products, and another endpoint to get the list of orders someone has placed. All these endpoints represent the interface that clients can use to talk to the server.

In technical term, we say the server provides an API (application programming interface) to clients.

Clients: REACT, ANGULAR, VUE (are used by front-end developers)

Server side tools for building backends: Django, ASP.NET CORE (for C# developers), EXPRESS (used by JavaScripts developers)

To setup the development environment: 

1- Update your python 

2- Make sure you istulled the pipenv 

3- Have code editor like VSCode

### Create your first Django project:

$mkdir storefront & cd storefront

$ pipenv install django

To activate:

$ pipenv shell

To deactivate:

$ exit

To start a new project:

$ django-admin

$ django-admin startproject storefront

If you want to use the current derectory to create the django project:

$ django-admin startproject storefront .

To run the project:

$ django-admin runserver

The convinient way of running the project is:

$ python manage.py 

$ python manage.py runsrver [local prot like 8000 or 9000]

#### To use the integrated terminal in VSCode:
In the command plattue (ctrl + Shift + p), search "python interpreater" and select the "enter interprater path". We need to address the path of the python interprater inside our virtual environment. To find the related path:

$ pip --venv

Select and copy the path and paste in the "enter interprater path" and append \Scripts\python.exe
something like:
"C:\Users\Elham\.virtualenvs\storeonline-zd3b2xDA\Scripts\python.exe"

Then open a new integrated terminal and run your Django project inside the integrated terminal.

#### Creating your first App

Every Django project is a collection of various apps with different functionality.

Shortcuts: ctrl+b shows (collapses) the project folders and files.
Shortcut" ctrl+l clears the termincal window.

Every Django project, by default, has some installed apps that are listed in the 'settings.py'. These apps are:
- Admin app: gives admin interface for managing data
- Auth app: for authenticating users
- Content types app
- Sessions app: which is kind of legecy. Asession is a temporary memory on the server for managing the users data. No need usually these days. You can delete this app.
- Messages app: is used to display one time notification to the user.
- Staticfile app: to serve the static files, like images, CSS files, and so on.

#### To creat a new app:

$ python manage.py startapp [app's name]

$ python manage.py startapp playground

Then, in the explorer panel, you see you app folder with some special files and structure in it:
- Migration folder for generating database tables.
- admin.py, Admin module, where we define how the admin interface for this app is going to look like.
- app.py : for configuring the app
- models.py: where we define the model classes for this app. We use model classes to pull out data from the database and present to the user.
- test.py: where we write our unit tests.
- view.py: what we have here is essentially a request handler
##### Each time you create an app you should add it in the list of installed Apps in the 'settings.py' file.

#### Writing view:
Http is a request response protocol. So, every data exchange involves a request and response. This is where we use view.py in Django and define our view function. 

A view function is a function that takes a request and returns a response. More accurately, it is a request handler. In some frameworks, called "action". In Django, it is called a "view".

An example of defining view function:


```python
import os, sys
import django
```


```python
from django.http import HttpResponse

def say_hello(request):
    # In real cenario, you can pull data from db, transform, 
    # send email in this function
    return HttpResponse('Hello World')
```

Now we need to map this view to a URL. So, when you get a request at that URL, this function will be called.

#### Mapping URLs to views:
To do so, make a file called, urls.py (or what ever you want), in the the project's folder (playground folder). In this module, we are going to map our URLs to our view functions.

In the urls.py:


```python
from django.urls import path
# from the current folder, we import view module. 
# So, we can reference our view functions.
from . import view 
```

Nov we should define a special variable called, urlpatterns and set it to an array of URL pattern objects. We use the path function to create a URL pattern object.


```python
# URLConf
urlpatterns = [
    
    path('playground/hello/', views.say_hello)
]
```

So, every app can have its own URL configuration.

But, now we need to import this URL configuration into the main URL configuration for this project in the main folder (storeonline folder). To do so, as mentioned in docstrings (read  Including another URLConf)


```python
# First we need to import the include function
from django import include
```

Then add a URL to urlpatterns in this module (in the main folder):


```python
urlpatterns = [
    ...
    path('playground/',include('playground.urls'))
]
```

By the above configuration, no the urlpatterns variable in the playground needs to be edited like the followngs:


```python
# URLConf
urlpatterns = [
    
    path('/hello/', views.say_hello)
]
```

So, when ever we change the codes, Django web sever automatically restart itself.

### Using Templates:
To use template to return html content to the client:

In the playground app, add a folder named, 'templates' and in this folder create a file called 'hello.html'

In the hello.html (write a h1 and click tab):

<h4> Hello Worlds </h4>

Now back to the views.py and instead or returning the HttpResponse, we are going to use the render function to render a template an return HTML markup to the client. To do so, edit the say_hello function as follows:


```python
from django.shortcuts import render

def say_hello(request):
    return render(request, 'hello.html')
```

In the hello.html, you can render dynamic variables. To do so, in the view.py:


```python
from django.shortcuts import render

def say_hello(request):
    return render(request, 'hello.html', {'name':'Reza'})
```

and edit your hello.html:


```python
<h1> Hello {{name}} </h1>
```

Also you can write some logic:


```python
{% if name%}
<h1> Hello {{name}} </h1>
{%else%}
<h1> Hello world </h1>
{% endif %}
```

These days, we offtenly do not use the templates in Django projects. For the most part, we use Django to build APIs that return data, not html content.

### debugging Django applications in VSCode:
If you want run your app line by line and see where the bug is, click on the "run and debug" in explorer panel of VSCode. Then click "create a launch.json file" icon and select Django. In the launch.json file, add "9000" under the "runserver" in the "args" of configuraions list if your server is running on the 8000 port. Then, you put a break point in a specific like and go to the "run abd debug" panel" and click start. F10 to go step forwar nd F11 go into functions and classes.

### Using Django debug toolbar:
 First, search "Django debug toolbar" in google and find the related website. Then, follow the instruction for installing the tool. Please note that your html codes should an standard html coding with html and body

## <font style="color:blue;">2- Building a data Model</font>

Models are used to store and retrieve data

#### introduction to data modelling:

What entities or concpets do we have in an eCommerce application? For starters, we need the concept of the product with attributes like title, description, price, inventory that in a real cenario, a product entity maight have other attributes. It depends on the requirements of our application.

Quite offten, our products are devided in different categories, like shoes, beaty products, fruits, and so on. So, we need another entity called collection or category with an attribute called title. Now, we need to add a relationship or an association between these entities. So, we can start from one end and navigate to the other end. For example, we can get a collection and find all the products in that collection.

Now, lets assume that in our application a produce blonges to just one collection and collection can have multiple products. So, we have "one-to-many" relationship between collection and product. Other relations are one-to-one and many-to-many. In the collection, you have an attribute called featured-attribute (one-to-zero). Every entity has an attribue that is automatically created by Django.

In every e-commerce application, we have a concept of shopping cart. So, we have an entity or a model or a class called cart with an attribute called "created_at". Let's assume that we need to know when each cart is created. So, every now we can do a cleanup and remove carts that are 30 days off.

There is a relation or association between products and carts. Because a cart can have multiple products and a product might be in different carts. So, here we have "many-to-many" relationship. Sometimes a relationship between two entities can have attributes. For example, if a product is in a shopping cart, we need to know have many instances of that product we have in the shopping cart. so, this relationship itself should have an attribute called quantity (and a entity called CartItem).

The next concept or entity is customer. It can have attributes like name, email, username, password, and so on. A customer can have many orders and each order belong to one customer. In this case there is one-to-many relationship between customers and orders. The order entity mighy have multiple attributes like placed_at (when), etc.. An order can contain multiple products and a product can be in multiple orders.So, there is many-to-many relationship between orders and products. Similar to the shopping cart example, this relationship itself needs an attribute called quantity (the entity called OrderItem). Another entity is tag. We have many-to-many rlationship between products and tags, because a tag can be referenced by different produts and vice versa.

A Django project contains several apps and each app has its own data model. So, there are different apps to organize our entities in different apps. 

One way is to have a single app called store and drop all our entites (Products, Collection, Cart, CartItam, Order, OrderItem, Customer, etc.) there. Then we can bundle an distribute this app by a pip. So, any one can install this app in their project and get all these models and functionalities around them. So, for the next appications, we do not need to rewrite the same functionality over and over. But there is a problem here. As this app grows and gets more and more complex, it gets bloated with to many things, like too many models, too many views and so on. This is what we call Monolith, like a large, heavy peice of stone. So, our app become hard to understand, maintain, and reuse.

another solution is to break down this project into four smal apps:
- The products app which represents a product catalog with three entities ( product, collection, and tag)
- The customer app for managing the customes.
- The shopping cart app for adding the shopping cart functionalities (Cart, CartItem, ...)
- The order app for adding the ordering functionalities (Order, OrderItem,...)
BUt, this is a poor way of breaking down a solution. First look at the dependencies of these app. For example the orders app dependent on the shopping cart app which is dependent on the product app. So, for the next ecomerce project, we need to install each of these app one by one (pipenv install products, carts, ...). Another problem is that if you update one of the app you maight be encountered with version confliction and causes the breaking the entire project. 

The midleware position is to separate the tag app and put other apps into a single App. So, here we have a tag app with entities like Tags and TagItem (that can be a product, video, etc.. The main app contains these entities: Products, Collection, Customer, Cart, CartItem, Order, and OrderItem. In this case, no coupling or dependency is between to apps.

So, back to VSCode and create to new apps: Store and tags:

$ python manage.py startapp store

$ python manage.py startapp tags

Next step is to add them into the installed app list in the setting.py

### Creat Model Classes:


To create our frist model class like "Product class", "Customer class", ect., in the store app, open the "model.py".
On top of this module, we have:

$ from django.db import models

The module "models" have a bunch of usefull classes that are used in defining model classes. In the followings you see two model classes for products and customers:


```python
class Product(models.Model):
    # To create your primery key
    # sku = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=225)
    birth_date = models.DateField(null=True)
```

By googling "django field types", you can find "Model field references" where in the right side of the page, you will find all the built-in "field types" like "Boolan fields" for storing boolean types, "CharFields" for storing a sequence of char fields, and so on.

Somtimes we need to limit the list of values that we stored in a field. For example in the customer class, let's define a new field called "membership". Now, let's assume that this field, we can have one of the values "B" for "Bronze", "S" for "Silver", and "G" for "Gold" membership. To do this, go back to our documentation where all field types are shared options mentioned in the document. One of this options is "Choices":


```python
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'SILVER'),
        (MEMBERSHIP_GOLD, 'GOLD'),
    ]
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=225)
    birth_date = models.DateField(null=True)
    
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
```

To create the order class:


```python
class Order(models.Model):
    PENDING_STATUS = 'P'
    COMPLETE_STATUS = 'C'
    FAILD_STATUS = 'F'

    PAYMENT_STATUS = [
        (PENDING_STATUS, 'Pending'),
        (COMPLETE_STATUS, 'Complete'),
        (FAILD_STATUS, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    paymant_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS, default=PENDING_STATUS)
```

#### Defining one-to-one relationship:

After creating your model classes, you need to emplement a relationship between two models.
For example, you have a new class called "Address" and each customer should have one and only one address (one to one relationship):


```python
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True)
```

As you database relationship has two ends, a "parent" and a "child" ends. Please note that the parent end or class should be defined before the child class. So, the "customer" class sould be created before the "child" class. Then, in the child class you should specify the parent class.

The options of the "on_delete" argument in the OneToOneField class of models modules: - models.CASCADE (when you delete a customer, the associated address automatically will also be deleted), - models.SET_NULL (After deleting the partent info the chiled not ganna get deleted by it will be set to NULL), - models.SET_DEFAULT (it will be set to the default value), models.PROTECT (frist you have to delete the child information and then you can delete the information of the partent).

"primary_key=True" in the argument of the OneToOneField, you can have only one customer for each addresses, since the primary key does not allow duplicate values.

#### Defining many-to-many relationship

#### Generic relationship

Create a new app called 'likes':

$ python manage.py startapp likes

Then create a generic model class called LikedItem:


```python
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
```

## <font style="color:blue;">3- Setting up the database</font>

Django supports many database managment systems. The most basic one that is set up by default is 'SQLite' that is a basic lightweight database engine. You should use it in low traffic website. For any serious project, you should use 'PostgreSQL', 'MySQL', 'MariaDB', 'Oracle' that are officially supported by Django. We will just focus on 'SQLite', and 'MySQL'.

#### Creating migrations

In Django, we use migrations to create or update or databse tables.
In the therminal window:

$ python manage.py makemigrations

Then, Django will create a migration file for each app. By click <h4>"ctrl + click"</h4> to open each migration file from terminal.

If you want to quickly jump to for example product class <h4>"ctrl + T"</h4> to go to symbol in workspace and open the product class. Another example press Ctrl+T and write "installed_apps" to open the setting.py and show the list of installed apps

Use <h4>F2</h4>
to rename a variable or class name

Now, as an example, let's add a new field called "slug" in the product class:

slug contains letters, numbers, hyphen, and underscore to make it easier for search engines to find our searches. So, it is a search engine optimization technique.


```python
class Product(models.Model):
    .
    .
    # one option is using "default='-'" and another option is "null=True"
    slug = models.SlugField(default='-')
```

#### Running migrations

By running migrations, Djange generates our sqlite databse schema. To do so:

$ python manage.py migrate

To open sqlite, install an extension called "sqlite" or install "DB browser for sqlite"

From the top, in view menu and open the command pallette. <h4>shift+ctrl+P</h4> is its shourcut. Then, search for "sqlite open database". In the explorer pannel in VSCode, you see all sqlite databases.

Another command is (for example for store app 0003:

$ python manage.py sqlmigrate [sepcific app] [seqence number of its migrations]

$ python manage.py sqlmigrate store 0003

show the actual sql statement Django sends to our database.

#### Customizing Database Schema

Sometime you need more control over databse schema. For example, we wanna override a name of a table or you wanna add an index to couple of columns and so on. To do so, let's open 'Customer' class using "ctrl + T". In this class, we want to define a inner class for metadata:

class Customer(models.Model):
    .
    .
    class Meta:
        # to find the options for Meta class, google django model metadata
        # and open the first link. Then, you see all the options in the right side.
        db_table = 'store_custoemrs'
        # We use indexes to speedup the queries.
        indexes = [
            models.Index(fields=['last_name','first_name'])
        ]

Then, create and run the migration

$ python manage.py makemigration

$ python manage.py migrate

#### Reverting (undo) migrations

There are a couple of ways to undo the previous migrations we applied.

1- If we want to selectively undo what we did in previous try, for example you wanna edit the "class Meta", do your changes and make a new migration.

2- If you want to undo everything you did in your previous try, you can completely revert the last migration. So, look at the migrations in store app, th last sequence number (here 0005) should be revert to (0004). So, open up a terminal window and type:

$ python manage.py migrate store 0004

Now, to verify, check the customer table in SQLITE EXPLORER and see the changes. Also, look the migration table and see the last migration has been gone.

But, the changes are still in the code! Go to the migration folder in the store app and see the last migration is still there. Do, if you run the migrate:

$ python manage.py migrate

the last migration will be back. To revert it properly, we should delete the last migration as well as all manually delete the changes we made in the code. Another way is to use a version control system like 'Git':

$ git log --oneline

$ git reset --hard HEAD~1

#### Installing MySQL & Connecting to MySQL

#### Installing DataGrip and connecting to MySQL

Open DataGrip (or MySQL workbench) and click new project. In a new query console type:

> CREATE DATABASE storefront

execute the query to create the databse.

#### Using MySQL in Django

The next step is to connect Django to MySQL. To do that, we need to install a package called "mysqlclient":

$ pipenv install mysqlclient

Before that, check your installation your mysql.To do so, open a new terminal window (we are ganna connect mysql using root user and a password):

$ mysql -u root -p

Then enter your password. If you got an error indicating mysql command not found, it maybe because MySQL is not installed properly or MySQL is not in your PATH.

The next step is to change our databse settings. Go to the setting module. Use

<h4>shift+ctrl+O</h4>
or use "Go menu">"got to symbol editors" and type "databses" to jump to database settings. It shows the default databse engine that is 'sqlite3' and it name. So, edit it like this:


```python
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'storefront',
        'HOST':'localhost',
        'USER':'root',
        'PASSWORD':'your MySQL password'
    }
}
```

Now back to terminal window and run the server, you should notget any error at this time. Then, run the migrate:

$ python manage.py migrate

Go to the DataGrip (MySQL workbench) and do a refresh to see yout storefront database.

#### Running a custom SQL

Sometimes we need a full cotrol over generating or updataing our database schema. All we have to do is creating an empty Django migration and there we can write any arbitrary SQL code. To do so, in the terminal (create an empty migration in the store app):

$ python manage.py makemigrations store --empty


```python
Open the empty migration and add the followings in the 'operation list':

operations = [
        #RunSQL is a class that is defined in the migration module,
        #the first argument is constructor for upgrading database 
        #and the second is for downgrading the database. 
        # If you do not set the second option you won't be able to revert it.
        migrations.RunSQL("""
            INSERT INTO store_collection(title)
            VALUE ('collection1')
        ""","""
            DELETE FROM store_collection
            WHERE title = 'collection1'
        """)
    ]
```

Back into the terminal and run a migrate:

$ python manage.py migrate

To unapply the last migration:

$ python manage.py migrate store 0004

#### Generating Dummy Data

To populating our database with some dummy data, use the following website:

www.mockaroo.com

Then, drag and drop or import the generated and downloaded data to DataGrip

## <font style="color:blue;">4- Django ORM (Object relational mapper)</font>

In relational databases, we store data as rows in tables. When you put data in a relational database, you map these rows into objects. In past, you had to do it manually. So, you had to write SQL codes:


```python
sql = 'SELECT * FROM product'
result = execute(sql)
for row in result:
    product = Product()
    product.title = row['title']
    product.price = row['price']
    ...
```

Here ORM comes to help. Object-relational mapper mapes objects to relational records and frees us from repeating codes. You can code in an object-oriented programming language like python. The ORM then translate our python codes into SQL codes at the run tume. 

#### Reseting the Database

Create virtual env

$ pipenv install

Then, in DataGrip (SQL workbench), click right on the localhost>new>query console and type:

>CREATE DATABASE storefront

In the terminal:

$ pipenv shell

The next step is to run all our migrtions to create our tables:

$ python manage.py migrate

The next is populating our database tables with data. To do so, in DataGrip, right click on the storefront database and open a new query console and drag and drop your data to it. On the top of the DataGrip, select the schema to storefront and select all data (ctrl+A) and execute them. The final step is to start our server:

$ python manage.py runserver

#### Managers and query sets

The first thing about the Django ORM is the concept of managers and query sets. To undrstand this concept, as an example, open say_hello() function in playground>view.py and write some pieces of codes there. Now, from store module, import the Product class on top of th view.py:

> from store.models import Product 

Every model in Django has an attribute called "objects" and this returns a manager object that you can talk to your database though it. Here we have bunch of methods for querying or updating data, for example a method called "all()" used to pull all the objects in the products table. Also, we have "get()" for getting a single object, "filter()" for filtering data and so on.

Most of these methods returns a query set. So, when we call this method, we do not get a list of product. Instead, we get a query set object. A query set is an object that encapsulate a query. So, when will this happen? On senario is when we iterate over a query


```python
def say_hello(request):
    query_set = Product.objects.all()
    
    for product in query_set:
        print(product)
        
    return render(request, 'hello.html', {'name': 'Reza'})

```

Then, open the "hello page" and open Django debug toolbar. Look at the SQL tab for check.

Another senario is when we convert the query set to a list. So, if we call a list function:


```python
def say_hello(request):
    query_set = Product.objects.all()
    
    list(query_set)
    query_set[0:5]
    query_set[0]
        
    return render(request, 'hello.html', {'name': 'Reza'})

```

This query set will be avaluated. Another senrio is to access individual elements like "query_set[0:5]"

To do a complex query:


```python
def say_hello(request):
    query_set = Product.objects.all()
    query_set = Product.objects.filter().filter().order_by()
        
    return render(request, 'hello.html', {'name': 'Reza'})
```

#### Retriving objects

There are different methods to retrieve objects. The first method is "all()" method and gives a query set. Sometimes we want to get a single object like the product with id=1. Then, we use the "get()" method and we pass a few parameters like "get(id=1)". Or "get(pk=1)" where Django automotically translate this to a name of primary key field. The primary key can be "id", "code", or what ever you want. The "get()" method returns an actual object not a query set. So, we can not sort, filter and so on with the results. Now, refresh the page and look at the SQL tab.


```python
def say_hello(request):
    product = Product.objects.get(id=1)
        
    return render(request, 'hello.html', {'name': 'Reza'})
```

Please note that if it can not find an object, it wil throw an EXPECTION. For example, if you set "get(pk=0)". So, we need to wrap our code inside a try-except block:


```python
from django.core.exceptions import ObjectDoesNotExist

def say_hello(request):
    try:
        product = Product.objects.get(pk=0)
    except ObjectDoesNotExist
        pass
    return render(request, 'hello.html', {'name': 'Reza'})
```

The more optimzed way is that use "filter()" method istead of "get()" method. This method returns a query set. Right away we can call the "first()" method. If the "first()" mthod is empty, it retuens "None". :


```python
def say_hello(request):
        product = Product.objects.filter(pk=0).first()
    return render(request, 'hello.html', {'name': 'Reza'})
```

Sometime, we need to check the existence of an object. So, instead of "first()" method, we use "exists()" method where it's type is a bollean value:


```python
def say_hello(request):
        # It's type i bollean value
        exists = Product.objects.filter(pk=0).exists()
    return render(request, 'hello.html', {'name': 'Reza'})
```

#### Filtering objects:

Let's talk about filtering data. For example we want to find all the products that are 20 dollars:


```python
def say_hello(request):
        queryset = Product.objects.filter(unit_price=20)
    return render(request, 'hello.html', {'name': 'Reza', 'products':list(queryset)})
```

Or to find all the products with prices greater than 20 dollars and so on. To find all the lookup types like __gt, __gte, __lt, and so on, you can search for "queryset api". Head over the first website and you will find the "Field lookups" on the right side.


```python
def say_hello(request):
        queryset = Product.objects.filter(unit_price__gt=20)
        queryset = Product.objects.filter(unit_price__gte=20)
        queryset = Product.objects.filter(unit_price__lt=20)
        queryset = Product.objects.filter(unit_price__lte=20)
        queryset = Product.objects.filter(unit_price__range=(20,30))
        
        queryset = Product.objects.filter(collection_id = 1)
        queryset = Product.objects.filter(collection_id__gt = 1)
        queryset = Product.objects.filter(collection_id__range = (1,2,3))
        
        queryset = Product.objects.filter(title__contains = 'coffee')
        queryset = Product.objects.filter(title__icontains = 'coffee')
        queryset = Product.objects.filter(title__startswith = 'coffee')
        queryset = Product.objects.filter(title__istartswith = 'coffee')
        queryset = Product.objects.filter(title__endswith = 'coffee')
        
        # for dates:
        queryset = Product.objects.filter(last_update__year=2021)
        queryset = Product.objects.filter(last_update__month=...)
        queryset = Product.objects.filter(last_update__date=...)
        
        # null description
        queryset = Product.objects.filter(description__isnull=True)
        
        # orgumnts from other tables like product table and 
        # call collection_id for orderitem
        queryset4 = OrderItem.objects.filter(product__collection_id=3)
        
    return render(request, 'hello.html', {'name': 'Reza', 'products':list(queryset)})
```

Now, got to the "hello.html" and after if block we are going to render an unordered list which represents the results:


```python
<html>
    <body>
        {%if name%}
        <h1> <font color="red"> Hello {{name}} </font> </h1>
        {% else %}
        <font color='blue'> TEST world </font>
        {% endif %}
        <ul>
            {% for product in products %}
            <li>{{ product.title }}</li>
            <li>{{product.description}}</li>
            {% endfor %}
        </ul>
    </body>
</html>
```

Do the pdf exercises!!!


```python
<ul>
            {% for cust in customer_info %}
                <li>
                    first name is:  {{ cust.first_name}}, The last name is: {{cust.last_name}}
                </li>
                <li>
                    Email:  {{cust.email}}
                </li>
            {% endfor %}
        </ul>
```

#### Complex lookups using Q objects:

How we can apply multiple filters. for example, the products that inventory<10 and price<20:


```python
# product>inventory<10 and price<20    ### AND operator ###
queryset = Product.objects.filter(inventory__ls=10, unit_price__lte=20)
queryset = Product.objects.filter(inventory__ls=10).filter(unit_price__lte=20)
queryset = Product.objects.filter(Q(inventory__ls=10) & Q(unit_price__lte=20))

# product>inventory<10 and price<20    ### OR operator ###
from django.db.models import Q

queryset = Product.objects.filter(Q(inventory__ls=10) | Q(unit_price__lte=20))

# for not operator ~
queryset = Product.objects.filter(Q(inventory__ls=10) | ~Q(unit_price__lte=20))
```

#### Referencing fields using F objects:

Sometimes, when filtering data, we need to reference a particular field. Here we use F object that we can reference particular field. For example, we want to compare two fields like find all the products where "inventory==unit_price":


```python
from django.db.models import Q, F
# product: inventory = unit_price
queryset = Product.objects.filter(inventory = F('unit_price'))
```

We can also reference a filed to a related table using F objects. 


```python
# product: inventory = collection: id
queryset = Product.objects.filter(inventory = F('collection__id'))
```

#### Sorting data:


```python
say_hello(request):

    # Acending order
    queryset = Product.objects.order_by('title')
    # decending order
    queryset = Product.objects.order_by('-title')
    # combined
    queryset = Product.objects.order_by('unit_price','-title')
    # to reverse the procedure
    queryset = Product.objects.order_by('unit_price','-title').reverse()
    # combined filter and order
    queryset = Product.objects.filter(collection__id=1).order_by('unit_price')
    ----------
    # to pick the first product after ordering
    product = Product.objects.order_by('unit_price')[0]
    product = Product.objects.earliest('unit_price')
    # in decending order it reutrns the first object
    product = Product.objects.latest('unit_price') 
    return render(request, 'hello.html', {'product':product})
```

#### Limiting results:

A product table has a thousand products. But, quite offen, we do not want to show all the list of products in one list. To limit the showed results:


```python
product = Product.objects.all()[:5]
product = Product.objects.all()[5:10] # 5,6,7,8,9 with an offset from 5
```

#### Selecting fields to query:

So, we have seen that when we query objects, by default, all of the fields are read from the database. But, if we only interested in subset of these fields. In thise case, we use "values" method and specify the fields we want to query:


```python
product = Product.objects.values('id','title')
# we can read the related fields like collection:title
### Using double underscore notation, we can access the related field. 
#You can check with SQL query set in the running page.
product = Product.objects.values('id','title', 'collection__title')
```

WHen you use "values" method, the results are a dictionary. To convert them to tuple:


```python
product = Product.objects.values_list('id','title', 'collection__title')
```

#### Difering fields:

Another method is "only()" that we can specifiy the fields we want to read from the database:


```python
product = Product.objects.only('id','title', 'collection__title')
```

The difference between "only()" method and "values()" method is that we get the instances of product class with "only()" method whereas the "values()" method will get dictionary object.

Another method is "defer()" method which is oposit of "only()" method and you exclude some fields.


```python
product = Product.objects.defer('description')
```

#### Selecting related objects:

Sometimes, we need to preload a bunch of objects together. For example, We are loading all the products:


```python
say_hello(request):
    queryset = Product.objects.all()
```

Now let's go to our template, say "hello.html" and render the collection of each product next to each title:


```python
<html>
    <body>
        <ul>
            {% for prod in products %}
            <li>{{ prod.title }} - {{prod.collection.title}} </li>
            {% endfor %}
        </ul>
    </body>
</html>
```

If you refresh the page, the application is hanging because Django is sending thousands extra queries to the database to read "collection " of all these products. Because when we ask for products, Django is going to query for product table. It is not going to query the related tables. So, here we need to preload the products with their collections. To do that, before we call "all()" method, we use "select_related" method:


```python
say_hello(request):
    queryset = Product.objects.select_related('collection').all()
```

Now, back to the browser and refresh the page. 

Now, let's spand the relationship. We want to preload another field as part of this query:


```python
say_hello(request):
    queryset = Product.objects.select_related('collection__SomeOtherField').all()
```

We have another method called "prefetch_related". We use "select_related" method when the other end of the relationship has one object or instance (one-to-many relationship). For example, a "product" has a one "collection". But, we use "prefetch_related" when the other end of the relationship has many objects (many-to-many relationship). The example is the "promotions" of a "product". So, to preload the "promotions", we use "prefetch_related" method:


```python
say_hello(request):
    queryset = Product.objects.prefetch_related('promotions').all()
```

Also, we can combine these two methods:


```python
queryset = Product.objects.prefetch_related('promotions')
            .select_related('collection').all()
```

An Exersise:

- Write a query to get the last five orders with their customers and items (inclduing products):


```python
from store.models import Product, Order
say_hello(request):
    queryset1 = Order.objects.select_related('customer').ordered_by('-placed_at')[:5]
    # The next step is to preload the items of these orders, say queryset1
    queryset1 = Order.objects.select_related('customer').
                prefetch_related('orderitem_set').ordered_by('-placed_at')[:5]
    # The last is to load the product referenced in each orderitem:
    queryset1 = Order.objects.select_related('customer').
                prefetch_related('orderitem_set__product').ordered_by('-placed_at')[:5]
```

#### Aggregating objects:

Sometimes, we want to compuste summaries or quantities like "MAX", "average", and so on. Here, we use "aggregate()" method:


```python
from django.db.models.aggregates import Count, Max, Min, Sum, Avg
say_hello(request):

    result = Product.objects.aggregate(count=Count('id'), 
                                       Min_price=Min('unit_price'))
    result = Product.objects.filter(collection__id=1)
            .aggregate(count=Count('id'), Min_price=Min('unit_price'))
        
    return render(request, 'hello.html', {'res':result})
```

#### Annotating objects:

Sometimes, we want to add additional attributes to our objects while quering them. Here we use "annotate()" method. For example, we want to add a new field for each customer called "is_new". You cannot set a boolean values like (True, False) to this new field. You can set an expression object like "value", "F" (to reference a field in a same or another table), "func" (for calling database options), "aggregate", etc.. To check, got to the browser and refresh the page and check the SQL:


```python
from django.db.models import Value, F

queryset = Customer.objects.annotate(is_new=Value(True))
queryset = Customer.objects.annotate(New_id=F('id')+1)
```

#### Calling database functions


```python
from django.db.models import  Func
from django.db.models.functions import Concat

# For example for concatinating two strings
queryset = Customer.objects.annotate(full_name=Func(F('first_name'), 
                    Value(' '), F('last_name'), function='CONCAT'))
# There is another way to get the same result using Concat class instead of func class
queryset = Customer.objects.annotate(full_name=
                    Concat('first_name', Value(' '), 'last_name'))
# search for other "django database functions" like working with dates,
# mathematical functions and so on.
```

#### Grouping data:

Let's say we want to see the number of orders each customer has placed. So, we are going to "annotate()" customers with a new field called "orders_count" and here we want to use the "Count" class. Now, what field we use to count te number of orders. As Customer class is a ForeinKey for Order class, django will create a reverse relationship between target class that is Order class and Customr class. So, in the Customer class we will have a field called "order_set":


```python
queryset = Customer.objects.annotate(orders_count='order_set')# you get an error!
queryset = Customer.objects.annotate(orders_count='order')# it is true!
```

#### Working with expression wrappers:

We talked about the expression class which is the base class for all types of experssions. Derivitives of this class are "Value", "F", "func", "Aggregate", and "ExpressonWrapper". We use "ExpressionWrapper" when bulding complex expressions. For example we want to annotate our product and give a "discounted_price":


```python
from django.db.models import ExpressionWrapper
discnt = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
queryset = Customer.objects.annotate(discounted_price=discnt)
```

#### Quering generic relationship:

Early in the course we created the "tags" app with two models. We have Tag() and TaggedItem(). In the later, we decided to use ContentType framework to decouple this app from the "store" app. So, this app knows absolutely nothing about the store app. It dose not know we have a model called product. So, with this decoupling, we can reuse this app in any other project. Now. let's see how we can find the tags for a given product. So, let's go to our database in DataGrip and look at the "django_content_type" table. In this table, we can see all the models we have in our application. Now, look at the "taggeditem" table. It has few columns like id, object_id, content_type_id, and tag_id. To find the tags for a given product, first we have to find the "content_type_id" of the product model. So, once we find it, we can go to the "taggeditem" table and write a query to  filter all records where content_type_id is equal to that for product model and object_id equals the id of the product whose tags we want to find out. Now, let's to implement this in code:

Back to playground>views.py. First, we need to find the "content_type_id" for the product model that we use "ContentType.objects"


```python
from django.contrib.contenttype.models import ContentType
from store.models import Product
from tags.models import TaggedItem

say_hello(models.Model):
    contnt_typ = ContentType.objects.get_for_model(Product)
    
    # In the taggeditem table, we have a column called "tag_id" which is a
    # foreinKey to the "tags" table. So, the actual tag is stored in "tags" table.
    # So, we need to proload the tag_id field. Otherwise we have a lot of extra
    # queries to the database.So, we call "select_related('tag')" to preload the
    # tag field.
    queryset = TaggedItem.objects \
        .select_related('tag') \
        .filter(
            content_type = contnt_typ,
            object_id = 1
    )
return render(request, 'hello.html', {'tags':list(queryset)})
```

#### Custom managers:

So, from previous lesson, our "tags" app was decoupled from "store" app. But writing code like the above code is not ideal. Everytime we want to tags for a given object, we have write the above code. The better way is to build a custom manager for the TaggedItem model. 

Go to tags>models.py to create custom manager:


```python
class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        contnt_typ = ContentType.objects.get_for_model(obj_type)
        return TaggedItem.objects \
            .select_related('tag') \
            .filter(
                content_type = contnt_typ,
                object_id = obj_id
            )
```

Now, we need to use this manager in the taggedItem model:


```python
class taggedItem(models.Model):
    # add a new attribute called "objects" and send it to an instance of 
    # TaggedItamManager() class
    objects = TaggedItemManager()
    .
    .
```

Now go back to playground>views.py and use this new method to get the tags for a given object:


```python
say_hello(models.Model):
    TaggedItem.objects.get_tags_for(product, 1)
```

#### Understanding QuerySet cache:

#### Creating objects:


```python
from store.models import Order, OrderItem, Product, Customer

def say_hello(request):
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(pk=1)
    collection.save()
    
    # or
    Collection.objects.create(name='a', featured_product_id=1)
```

#### Updating objects:


```python
from store.models import Order, OrderItem, Product, Customer

def say_hello(request):
    collection = Collection(pk=11)
    collection.title = 'Video Games'
    collection.featured_product = Product(pk=1)
    collection.save()
    
    # another option is:
def say_hello(request):
    collection = Collection.objects.get(pk=11)
    collection.featured_product = None
    collection.save()
    # or
    Collection.objects.update(featured_product=None)
```

#### Deleting objects:

We can delete a single object or multiple objects. 


```python
def say_hello(request):
    # delete a single object
    collection = Collection(pk=11)
    collection.delete()
    # delete multiple objects:
    Collection.objects.filter(id__gt=5).delete()
```

#### Transactions:

Sometimes we want to make multiple changes in our database in an atomic way, meaning changes should be saved all together or if one of the changes failes, all changes should be roud back. A typical example is saving an order with its items. So, let's create a typical order object. Then, set the customer field and then save the order before we can save its items. This is how relational database works:


```python
def say_hello(request):
    order = Order()
    order.customer_id =1
    order.save()
    
    return rendre(request, 'hello.html', {'name':'Mosh'})
```

Then, we can create on OrderItem and set few fields like setting the order, product_id, quantity, and unit_price and finally save the order:


```python
def say_hello(request):
    order = Order()
    order.customer_id =1
    order.save()
    
    item = OrderItem()
    item.order = order
    item.product_id = 1
    item.quantity = 1
    item.unit_price = 10
    item.save()
    
    return rendre(request, 'hello.html', {'name':'Mosh'})
```

Now, imagine while saving the OrderItem, something crazy happens, we get an exception. what is going to happen? In this case we have an Order without an OrderItem. We do not want this to happen. This is where we use "Transaction()". So, we wrap both these operations (Order and OrderItem) inside a transaction and either both of these will be commited together or one of these operations fails, then all changes will be roud back. To do so, import "transaction" module. In "transaction" we have function called "atomic" that can be used as a decorator. It will wrap the entire view function (here say_hello()) into a transaction. 


```python
from django.db import transaction

# To wrap the entire function, use decorator:
@transaction.atomic()
def say_hello(request):
    #
    # ... how some peice of code that you do not want to wrap into a transaction
    # first remove the decorator @transaction.atomic()
    with transaction.atomic():
        order = Order()
        order.customer_id =1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save()
    
    return rendre(request, 'hello.html', {'name':'Mosh'})
```

#### Executing Raw SQL Queries:

When executing queries using Django ORM is very complex, say with a lot of annotations, filters, and so on, you can write your own query by your hand and execute it directly using Django ORM. Here, we use "raw()" method to execute raw SQL queries:


```python
def say_hello(request):
    queryset = Product.objects.raw('SELECT * FROM store_product')
    queryset2 = Product.objects.raw('SELECT id, title FROM store_product')
    return rendre(request, 'hello.html', {'result':list(queryset)})
```

Somtimes we wanna execute queries that do not map to our model object. In those cases, we can access the database directly and bypass the model layer. So, instead of using the "raw()" method, we import "connection" module and use "cursor()" function for creating a cursor object. The cursor object has a execute() method that can pass any SQL statement:


```python
from django.db import connection

def say_hello(request):
    cursor = connection.cursor()
    cursor.execute('SELECT ...')
    cursor.execute('INSERT ..., update, and delete')
    # and so on!!
    cursor.close()
    
    ### The better way is use With statement:
    with connection.cursor() as cursorz:
        cursor.execute('SELECT ...')
        cursor.execute('INSERT ..., update, and delete')
        # To execute stored procedures, use a method called "callproc()":
        # We can call a stored procedure like get_customers and 
        # give it a bunch of parameters [1,2, 'a', ...]
        cursor.callproc('get_custoemrs', [1, 2, 'a'])
    
    return rendre(request, 'hello.html', {'result':list(queryset)})
```

## <font style="color:blue;">5- Admin interface</font>

we will talk about the admin interface for managing our data. We will talk about 
- Various ways to customize the admin interface
- How to add computed columns
- Loading related objects
- Add searching and filtering
- Implement custom actions
- Add data validations

That are used for managing data.

#### Setting up the Admin site or Admin app

Every Django project comes with an admin interface which we can access at (http:.../admin). To create a new user in terminal window:

$ python manage.py createsuperuser

Then, it asks for user name, email and password. Now, we have an admin user. Let's log in. You encounter with an error compleining abour "session() app". Because the admin app dependents to session app and you may removed it by accident. So, we need to add it back to the list of installed_apps. So, back to the project, in the list of INSTALLED_APPS:

> 'django.contrib.sessions'

Then, execute the migrate command:

$ python manage.py migrate

to generate the related table for this app. Then, we have new table called "django_session" for storing temporarily users' data. Refresh the page and see the admin interface. The users and groups are stored in the tables of the "auth app". To reset the password in terminal:

$ python manage.py changepassword admin

To change the titles of the admin homepage like "header: Django administration" and "label: site administration":

Back to the project, open the storefront folder and go to the urls module. In this module, all the urls of admin app are hoocked up at (path('admin/', admin.site.urls) ). Here we can use a bit of customization:

> admin.site.site_header = 'StoreFront Admin'

> admin.site.index_title = 'Admin'

#### Registering models:

Let's see how we can register our models, so we can manage them in the admin site. Back to the project and got the store folder. Every django app has a module called "admin.py". And this is where we write all the codes for customizing the administration panel for that app. So, first thing to do is registering our models for the admin site. So, the admin module was already added on the top. In the store>admin.py, For example, we want to register the collection moedel:

> from . import models

> admin.site.register(models.Collection)

> admin.site.register(models.Product)

To show the title of each collection: Go to the Collection class. To change the string representation of an object, we use magic __ str __ method:


```python
class Collection(models.Model):
    . . . 
    def __str__(self):
        return self.title
    
    # To order the titles of collections:
    class Meta():
        ordering = ['title']
```

#### Customizing the list page:

How customize the list page? To add new columns to the list of, for example, admin page, make editable, how to change the number of items and so on. So, back to admin module (admin.py). First, we need to add a new class called ProductAdmin(admin.ModelAdmin). With this class we can specify how view and edit the our products:


```python
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price']
    list_editable = ['unit_price']
    list_per_page = 10
    
admin.site.register(models.Product.ProductAdmin)
```

The shorter way is to use register decorator:


```python
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price']
    list_editable = ['unit_price']
    list_per_page = 10
```

To find the complete list of options here for ModelAdmin, google "Django ModelAdmin", on the right side you can find the "Model Admin options".

#### Adding the computed columns:

Let's see how we can add computed columns in the list of products. For example we want to add a new column called "inventory_status" in which it shows low if the inventory is less than 10 otherwise it is ok. To implement this, back to our Product admin class, we want to display "inventory_status" in the list_display. If you add just "inventory", you see just numbers:


```python
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price','inventory_status']
    list_editable = ['unit_price']
    list_per_page = 10
    
    #To implement sorting based on inventory_status, use admin.display decorator
    @admin.display(ordering='inventory')
    def inventoryz_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'
```

#### Selecting related objects:

Let's talk about loading related objects. for example, in the list of products, we want to add a column to show the collection of each product. So, back to the product admin class, add 'collection' field to the list_display. Because the 'collection' is a related field, Django will show a string representation of the collection here. Back to the Collection class, we over wrote the __ str __ mothod. So, when showing the products, for each product, Django will call this method to get the title of the collection of that product. If we do not want to show the string representation of a collection, in other word, we want to show a particluar field of collection model, we cannot use for example "collection __ title" to reference at particulr field like title field. We can define a method for this purpose "def collection_title()". But, using this method will execute some extra queries, because for each product, Django is sending an extra query to the database to read the collection of that product:


```python
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price','collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    
    def collection_title(self, product):
        return product.collection.title
```

The more efficient way (executing less queries) is to use a special attribute called "list_select_related()":


```python
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price','collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    def collection_title(self, product):
        return product.collection.title
```

#### Overriding the base QuerySet

Sometimes we need to override the base queryset used in rendering a list page. For example, in the list of collection, we want to add a column showing the number of products in each collection. So, create a class called CollectionAdmin and add 'title' and 'product_count' in the list_display:


```python
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','products_count']
```

But, our collection do not have a field called 'products_count'. So, we need to treat this like a computed field and define a new method called "products_count". But, again the collection object do not have 'product_count' field. So, this is where we need to override the queryset on this page and annotate our collections with the number of their products. 

Every ModelAdmin has a method called "get_queryset()" which we can override:


```python
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','products_count']
    
    # to sorting based on products_count use decorator:
    @admin.display(ordering='products_count')
    def products_count(self, collection):
        return collection.products_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product'))
```

#### Providing links to other pages:

Let's see how we can add links. For example, when we click on the links in Collections, we can see the products in each collection. So, back to the "product_count" method. We should return an html link. To do so, we should import a utility function on the top:


```python
from django.utils.html import format_html
```

Use "ctrl + -" to jump back to where we were.

In the products_count function, add a 'format_html' method to write a bit of html code. In html, we can represent a link using "<a>ancher element! for example showing the number of products </a>" element (here google.com is used as a test link):


```python
from django.utils.html import format_html

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','products_count']
    
    # to sorting based on products_count use decorator:
    @admin.display(ordering='products_count')
    def products_count(self, collection):
        return format_html('<a href="http://google.com">{}</a>',
                           collection.products_count) 
```

Now let's see how we can send our users to the products page. Look at the url page, that is .../amin/store/product/. We do not want to hard code to this url, because this url can potentially change in the future. We should ask Django to give us the url of this page. To do that, we need to import another utility function:


```python
from django.urls import reverse
```

Then, go back to our method and call reverse function and give it a espacial argument:

> reverse('admin:app_model_page')

> reverse('admin:store_product_changelist')


```python
from django.utils.html import format_html
from django.urls import reverse

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','products_count']
    
    # to sorting based on products_count use decorator:
    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = reverse('admin:store_product_changelist')
        return format_html('<a href="{}">{}</a>', url
                           collection.products_count) 
```

To apply a filter, we need to append a querystring to the url. So, we type a ? mark followed by collection__id=1. So, we need to add this part dynamically. Here we need to import "urlencode" function:


```python
from django.utils.html import format_html, urlencode
from django.urls import reverse

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','products_count']
    
    # to sorting based on products_count use decorator:
    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (reverse('admin:store_product_changelist')
              + '?'
              + urlencode({
                  # Since a query string contains multiple key-value pairs
                  # so, that is why we use a dictionary
                  # We use str function to change number to string
                  'collection__id':str(collection.id)
              }))
        return format_html('<a href="{}">{}</a>', url, 
                           collection.products_count) 
```

#### Adding search to the list page:

To add searching to, for example, the customer page:


```python
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    . 
    .
    .
    search_fields = ['first_name','last_name']
    search_fields = ['first_name__istrartwith','last_name_istartwith']
```

#### Add filtering to the list page:

To implement filtering to, for example, products page and filter our products by their collections and last update:


```python
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']
    .
    .
    list_filter= ['collection','last_update']
```

We also can create our own custom filters. Say, let's we want to add a filter here to see only products with low inventory. So, back to the admin module, create a new class called InventoryFilter(admin.SimpleListFilter) or any other arbitrary name. Here we should send a couple of attributes like "title" that will be appeared as a title of our filtering, and second is "parameter_name" with any arbitrary name that will be used in the quert string. There are two metods we need to implement here. 

One of them is "lookups()" that we can specify what items should appear in the list of filtered objects. In this method, we return a list of tuples. Each tuple represents one of the filters. In each tuple, the first value is an actual value used for filtering. This can be anything. The second value is a human readable discription. 

The second method is "queryset()" and this is where we implement the filtering logic:


```python
# In the admin model:
class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'
    
    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]
    
    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)

        
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']
    .
    .
    list_filter= ['collection','last_update', InventoryFilter]
```

#### Creating custom acations:

Defining custom actions: Every list page comes with a delete action for deleting multiple objects in one goal. We can extend this list and register our custom actions. For example let's say define a custom action for clearing the inventory of a bunch of products in one goal. So, we want to set the inventory to zero. Back to the product adming class and difine a new method called "clear_inventory" or any other arbitrary name. Here yo uneed three parameters: self, request (which represents the current http request), and queryset (which contains the objects the user has selected). In this metod you can do anything to updating objects. To show a message to the user, we call "self.message_user". Every module admin contains this method to show a message to the user:


```python
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions =['clear_inventory']
    .
    .
    
    list_display = ['title', 'unit_price']
    .
    .
    
    @admin.action(description='Clear_inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.'
        )
```

Here we also can show error messages. When calling "message_user" method we can specify the type of message as the third argument. First we need to import "messages" model from django.contrib and padd the third argument:


```python
    @admin.action(description='Clear_inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.',
            messages.ERROR
        )
```

#### Customizing forms:

Let's see how we can customize the form, or adding or updating models. For example, in the product page, click "ADD PRODUCT" to add a product. You see a form and we want to customize it. Back to the "ProductAdmin" class. You can set "fields" to the list of fields we want to show to the user.  Another attribute called "exclude" which is the opposite of fields. So, with this attribute we can exclude certain fields. Wh also have "readonly_fields" for making some fields read-only case. 

To auto-populate a field, like auto populating the "slug" field when tou fill out the title, use "prepopulated_fields" to a dictionary. In this dictionary, we can specify how each field in this form can prepopulated. 


```python
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions =['clear_inventory']
    .
    .
    # fields render what you want to show to the user.
    fields = ['title','slug']
    .
    # To exclude some fields
    exclude = ['promotions']
    # To make read only
    readonly_fields = ['title']
    # To prepopulate the slug field
    prepopulated_fields = {
        'slug': ['title','...']
    }
    .
    
    @admin.action(description='Clear_inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.'
        )
```

Now look at the collection field where we have drop down list to show all the collection titles. If there are many collection titles, showing the drop down list will have a couple of issues, to working with it as well as the performance issue. So, we have to convert it to autocomplete field. Back to ProductAdmin class and add it. If you get an error indicating the collection should be included in the search field. So Back to CollectionAdmin class and use "search_fields" attribute:


```python
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','products_count']
    .
    .
    # Add collection to the search field.
    search_fields = ['title']
    
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions =['clear_inventory']
    .
    .
    autocomplete_fields = ['collection']
    
    
```

If you want to find all the options available to customize the form, google "django modeladmin" and look at ModelAdmin options. 

#### Adding data validation:

By default, our forms include basic data validation logic. For example, because we have defined all the fields in product model as required fields, none of them are nullable and if you try to save the form of "ADD PRODUCT", without supply any data, we get the validation errors like "This field is required" and so on. So, how we can customize this validation here. For example, making the description field nullable. Back to the product class and make the description field (null=True). Please note that this argument applies to our database. To make this field optional in the admin interface, we should set another argument (null=True, blank=True). Then, make migration and migrate and apply to the database. 

$ python manage.py makemigration

$ python manage.py migrate

What about the "unit_price". We can not type any character like strings since the type of this field is decimal and it only accept numbers. But, we are still free to set zero or negative numbers. To set a validation limit for this, we need to import MinValueValidator from django.core.validators. In this module, we have a bunch of validators. For a complete list of vlidators, google "django validators" and you can see like EmailValidator, URLValidator, MaxValueValidator, MinValueValidator, and so on. Then, go to the Product model and add an argument including a list of validator objects in the unit_price field.


```python
from django.core.validators import MinValueValidator

class Prodcut(model.Model):
    .
    .
    unit_price = models.Decimalfield(
        max_digits=6,
        decimal_places=2,
        validator= [MinValueValidator(1, message=...)]
    )
```

#### Editing children using inlines:

As an example, currently we can create a new order but there is no way to manage the items from the order. To do so, back to store>admin.py, before the OrderAdmin class, create a new class called OrderItemInline(admin.TabularInline) or OrderItemInline(admin.StackedInline):


```python
class OrderItemInline(admin.StackedInline):
class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    model = models.OrderItem
    # To manage the number of place holders
    extra =0
    # To set the min and max number of items from order
    min_num = 1
    max_num = 10
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    .
    .
    indlines = [OrderItemInline]
        
```

#### Using Generic relations:

In the product form, we want to add a new section for managing the tags. So, back to our code, First go to the tags app, in its admin module (tags>admin.py), we need to register our tag model, so, we can manage our tags in the admin interface. So, in tags>admin.py:


```python
from .models import Tag

@admin.register(Tag)
class TagAdmin(model.ModelAdmin):
    search_fields = ['label']
```

to see the label of each tag, as we discussed before, we need to override the __ str __ method in the Tag class. Go to tags.models.py>Tag class:


```python
class Tag(models.Model):
    laber = models.CharField(max_length=255)
    
    def __str__(self):
        return self.label
```

Now, using Inlines, we can manage the tags in our product form. Let's open up the store>admin.py and before the ProductAdmin class, we create an inline class for managing the tags called TagInline :


```python
from django.contrib.contenttypes.admin import GenericTabularInline


class TagInline(GenericTabularInline):
    # in tags>admin.py, add search_fields = ['label']
    autocomplete_fields = ['tag']
    model = TaggedItem

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions =['clear_inventory']
    .
    inlines = [TagInline]
```

This is how we can use Generic relationships in our forms. But, there is a problem in our implementation.

#### Extending pluggable apps:

In the admin module of the store app, we had to import the TaggedItem from tags.models. It means that store app has a dependency to the tags app. So, we can not build and deploy them independently. Ideally, our apps should be self contained. So, we can easily plug them to the new projects. So, we need to decouple the two apps. To do so, we are going to create a new app called "store_custom" and this is the customization of the store app which knows about both "store" and "tags" apps. This is specific to our project. So, in the terminal:

$ python manage.py startapp store_custom

In the admin module of store_custom, we are going to combine features from our two apps. So, in store_custom>admin.py:


```python
from store.admin import ProductAdmin
from tags.models import taggedItem

from django.contrib.contenttypes.admin import GenericTabularInline

# The class TagInline from the store>admin.py should moved to here
class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem
    
# We need to create a new ProdctAdmin which extends the generic ProductAdmin
# that comes with our reusable app (here is store app) and in this
# new implementation we are going to reference the TagInline class:

class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]
    
# Now we have new ProductAdmin and we need to unregister the old one an register
# this new one:
admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
```

The final step is to register the new app in the "INSTALLED_APPS". Use "ctrl + t" as a shortcut to go to installed apps list.


```python
 
```
