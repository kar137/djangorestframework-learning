# Django REST Framework (DRF) Learning Plan

## Overview
This is a **10-day structured plan** to learn **Django REST Framework (DRF)** by following the official documentation. The goal is to dedicate **2 hours daily** to learning DRF concepts and building APIs effectively.

## Prerequisites
Before starting, ensure you have:
- Basic knowledge of Python & Django
- Django installed (`pip install django`)
- DRF installed (`pip install djangorestframework`)
- Postman or an API testing tool

## Learning Schedule

### **Day 1: Introduction & Setup**
🔹 Read: [Overview & Installation](https://www.django-rest-framework.org/#installation)
🔹 Install DRF and set up a Django project
🔹 Learn about the request/response cycle

**Practice:**
✅ Create a Django project
✅ Add DRF to `INSTALLED_APPS` and configure settings

---

### **Day 2: Requests, Responses & API Views**
- Read: [Requests & Responses](https://www.django-rest-framework.org/tutorial/2-requests-and-responses/)
- Learn about `APIView`, `Request`, and `Response`

**Practice:**
- ✅ Create a simple API view
- ✅ Use different HTTP methods (GET, POST)

---

### **Day 3: Serializers**
- Read: [Serializers](https://www.django-rest-framework.org/tutorial/1-serialization/)
- Understand `ModelSerializer` vs `Serializer`

**Practice:**
- ✅ Create a `Serializer` for a model
- ✅ Convert Python objects to JSON and vice versa

---

### **Day 4: Class-Based Views & Mixins**
- Read: [Class-Based Views](https://www.django-rest-framework.org/api-guide/views/)
- Learn about mixins like `ListModelMixin`, `CreateModelMixin`

**Practice:**
- ✅ Refactor API views using generic views
- ✅ Create an API using `ListCreateAPIView` & `RetrieveUpdateDestroyAPIView`

---

### **Day 5: ViewSets & Routers**
- Read: [ViewSets & Routers](https://www.django-rest-framework.org/api-guide/viewsets/)
- Learn about `ModelViewSet` and `SimpleRouter`

**Practice:**
- ✅ Create a `ModelViewSet` for a model
- ✅ Register it with `DefaultRouter`

---

### **Day 6: Authentication (JWT & Token-based)**
- Read: [Authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- Learn `TokenAuthentication` and `JWT` (using `djangorestframework-simplejwt`)

**Practice:**
- ✅ Implement JWT authentication
- ✅ Test authentication with Postman

---

### **Day 7: Permissions & Throttling**
- Read: [Permissions](https://www.django-rest-framework.org/api-guide/permissions/)
- Learn about `IsAuthenticated`, `IsAdminUser`, `Custom Permissions`

**Practice:**
- ✅ Restrict API access based on user roles
- ✅ Implement custom permissions

---

### **Day 8: Pagination, Filtering & Searching**
- Read: [Pagination](https://www.django-rest-framework.org/api-guide/pagination/)
- Read: [Filtering](https://www.django-rest-framework.org/api-guide/filtering/)

**Practice:**
- ✅ Add pagination to API results
- ✅ Implement filtering using Django filters

---

### **Day 9: API Testing & Documentation**
- Read: [Testing](https://www.django-rest-framework.org/api-guide/testing/)
- Learn about Swagger & DRF’s built-in API docs

**Practice:**
- ✅ Write unit tests for APIs using Django’s test framework
- ✅ Set up **Swagger** for API documentation

---

### **Day 10: Deployment & Best Practices**
- Read: [Deployment](https://www.django-rest-framework.org/topics/deployment/)
- Learn about **caching, security, and performance**

**Practice:**
- ✅ Deploy a DRF project on **Render/Heroku**
- ✅ Optimize API performance

---

## Additional Tips
- **Use Postman** to test APIs
- **Take Notes** while reading the documentation
- **Practice Daily** to reinforce concepts

## Next Steps
- Explore **Async Django**
- Learn **Django Channels** for WebSockets
- Contribute to **open-source DRF projects**

Happy Learning! 🚀

