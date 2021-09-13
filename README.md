# orchids
We will install following libraries for django, django rest framework and django rest knox.
After installing the above library. Add rest_framework and knox to your INSTALLED_APPS, remove rest_framework.authtoken
Make knox’s TokenAuthentication your default authentification class for django-rest-framework, in settings.py file:

Now we will User Registration API Using Django Rest Framework. 
We will create Register Serializer for User Register API.

After creating serializer, we need to create DRF APIView.

In urls.py file add following path –That’s it. Now go to url ( http://localhost:8000/api/register/ ) in your browser.

Login Logout API Authentication using Django Rest Framework

We have already create a app with name accounts. Inside this app we will create our LoginView.

And in accounts/urls.py file.That’s it. Now go to url ( http://localhost:8000/api/login/ ) in your browser

And in accounts/urls.py file.That’s it. Now go to url ( http://localhost:8000/api/logout/ ) in your browser



