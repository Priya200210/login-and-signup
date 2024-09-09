from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
#from .models import Users  
from .models import *
#from .models import Student
#from .models import Student_detials
import json
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.shortcuts import render, get_object_or_404


@csrf_exempt
def Signin(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username') 
            email_adress = data.get('email_adress') 
            password = data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                response = {"success": True, "response": "User authenticated successfully", "user": user.id}
            else:
                response = {"success": False, "response": "Invalid credentials"}

        except Exception as e:
            response = {"success": False, "response": str(e)}

        return JsonResponse(response)

    else:
        return JsonResponse({"success": False, "response": "Method not allowed"})
    

@csrf_exempt
def Signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email_address = data.get('email_address')
            password = data.get('password')

            
            if User.objects.filter(username=username).exists():
                response = {"success": False, "response": "Username already taken"}
            elif User.objects.filter(email=email_address).exists():
                response = {"success": False, "response": "Email already taken"}
            else:
               
                user = User.objects.create_user(username=username, email=email_address, password=password)
                user.save()
                response = {"success": True, "response": "User registered successfully", "user": user.id}

        except Exception as e:
            response = {"success": False, "response": str(e)}

        return JsonResponse(response)

    else:
        return JsonResponse({"success": False, "response": "Method not allowed"})
    

@csrf_exempt
def pages_list(request):
    try:
        pages = Pages.objects.all().values('id', 'articles_name', 'artticles_site')
        return JsonResponse({'pages': list(pages)}, safe=False)
    except Pages.DoesNotExist:
        return JsonResponse({'error': 'No pages found'})
    


@csrf_exempt
def student(request):
    try:
        students = Student.objects.all().values('name','student_id','department')
        return JsonResponse({'student': list(students)},safe=False)
    except student.DoesNotExist:
        return JsonResponse({'error': 'no student found'})
    

@csrf_exempt
def student_view(request):
    if request.method =='GET':
        students = Student.objects.all().values('name','student_id','department')
        return JsonResponse({'student':list(students)}, safe=False)
    else:
        return JsonResponse({'error':"invaild method"}, status = 500)
    
    
@csrf_exempt
def student_object(request,student_id):
    if request.method =="GET":
        students = get_object_or_404(Student, id = student_id)
        context = {
            'student' : students
        }
        return render(request,'studdent_details.html',context)
    else:
        return render(request, ' 404.html', status = 405)


@csrf_exempt
@require_http_methods(["POST", "GET"])
def student_create(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get('name')
            student_id = data.get('student_id')
            department = data.get('department')

            if Student.objects.filter(name=name).exists():
                response = {"success": False, "response": "Student name already taken"}
            elif Student.objects.filter(student_id=student_id).exists():
                response = {"success": False, "response": "Your ID is already taken"}
            else:
                Student.objects.create(name=name, student_id=student_id, department=department)
                response = {"success": True, "response": "Student added successfully!"}
        except Exception as e:
            response = {"success": False, "response": str(e)}
        
        return JsonResponse(response)
    
    elif request.method == "GET":
        response = {"success": False, "response": "Unhandled error"}
        try:
            search = request.GET.get('search', '').strip()
            sort_by = request.GET.get('sort_by', 'student_id')
            order = request.GET.get('order', 'asc')
            page = int(request.GET.get('page', 1))
            page_size = int(request.GET.get('page_size', 10))

            if order == 'desc':
                sort_by = f'-{sort_by}'
            else:
                sort_by = sort_by.strip()

            if search:
                students = Student.objects.filter(Q(name__icontains=search)).order_by(sort_by)
            else:
                students = Student.objects.all().order_by(sort_by)

            paginator = Paginator(students, page_size)

            try:
                pages_paginated = paginator.page(page)
            except PageNotAnInteger:
                pages_paginated = paginator.page(1)
            except EmptyPage:
                pages_paginated = paginator.page(paginator.num_pages)

            students_list = list(pages_paginated.object_list.values('name', 'student_id'))
            response = {
                "success": True,"students": students_list,"current_page": page,"total_pages": paginator.num_pages,"total_items": paginator.count
            }
        except Exception as e:
            response = {"success": False, "response": str(e)}
        
        return JsonResponse(response, safe=False)
    
    else:
        return JsonResponse({"success": False, "response": "Method not allowed"}, status=405)

@csrf_exempt
def list_pages(request,page_id):
    if request.method == 'GET':
        pages = get_object_or_404(Pages,id=page_id)
        context = {
            'page':pages
        }
        return render(request,'page_detials.html',context)
       
    else:
        return render(request, '404.html', status = 405)
    


# @csrf_exempt
# def students_view(request, student_id):
#     if request.method =="GET":
#         try:
#             students = get_object_or_404(Student_detials, id= student_id)
#             my_context = {
#             'student' : students

#         }
#             return render(request,'student_details.html',my_context)
#         except Exception as e:
#             return render(request,'error.html',{'error': "An error occured :{}".format(str(e)), status = 500})
#     else:
#         return render(request, '404.html', status= 405)
    



# @csrf_exempt
# def student_request(request):
#     if request.method == 'GET':
#         try:
#            students = Student_detials.objects.all().values('id','student','student_id','branch')
#            return JsonResponse({'students':list(students)},safe=False)
#         except Exception as e:
#             return JsonResponse({'error':"invaild method"},status = 500)
#         else:
#             return JsonResponse({"sucess":False,"response": "method not allowed"}, status = 405)

    

# @csrf_exempt
    
# def create_page(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             page_id = data.get('id')  
#             articles_name = data.get('articles_name')
#             artticles_site = data.get('artticles_site')
#             if page_id:
#                 try:
#                     page = Pages.objects.get(pk=page_id)
#                     page.articles_name = articles_name
#                     page.artticles_site = artticles_site
#                     page.save()
#                     response = {"success": True, "response": "Page updated successfully", "page_id": page.id}
#                 except Pages.DoesNotExist:
#                     response = {"success": False, "response": "Page not found"}
#             else:
#                 response = {"success": False, "response": "Page ID is required for update"}

#         except Exception as e:
#             response = {"success": False, "response": str(e)}

#         return JsonResponse(response)

#     else:
#         return JsonResponse({"success": False, "response": "Method not allowed"}, status=405)
    
@csrf_exempt
def create_page(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            articles_name = data.get('articles_name')
            artticles_site = data.get('artticles_site')
            price = data.get('price')
            if Pages.objects.filter(articles_name=articles_name).exists():
                response = {"success": False, "response": "articles_name already taken"}
            elif Pages.objects.filter(artticles_site=artticles_site).exists():
                response = {"success": False, "response": "artticles_site already taken"}
            else:
                page = Pages.objects.create(articles_name=articles_name, artticles_site=artticles_site, price=price)
                page.save()
                response = {"success": True, "response": "Page created successfully"}

        except Exception as e:
            response = {"success": False, "response": str(e)}
        return JsonResponse(response)

    elif request.method == 'GET':
        try:
            search = request.GET.get('search', '').strip()
            sort_by = request.GET.get('sort_by', 'price')
            order = request.GET.get('order', 'low')
            page = request.GET.get('page', 1)
            page_size = request.GET.get('page_size', 10)

            if order == 'high':
                sort_by = f'-{sort_by}'
            else:
                sort_by = sort_by.strip()

            if search:
                pages = Pages.objects.filter(
                    Q(articles_name__icontains=search) | Q(artticles_site__icontains=search)
                ).order_by(sort_by)
            else:
                pages = Pages.objects.all().order_by(sort_by)

            paginator = Paginator(pages, page_size)

            try:
                pages_paginated = paginator.page(page)
            except PageNotAnInteger:
                pages_paginated = paginator.page(1)
            except EmptyPage:
                pages_paginated = paginator.page(paginator.num_pages)

            pages_list = list(pages_paginated.object_list.values('articles_name', 'price'))
            response = {'success': True, 'pages': pages_list, 'page': pages_paginated.number, 'total_pages': paginator.num_pages, 'total_item': paginator.count}

        except Exception as e:
            response = {"success": False, "response": str(e)}
        
        return JsonResponse(response)
    
    else:
        return JsonResponse({"success": False, "response": "Method not allowed"}, status=405)
    


# @csrf_exempt
# def student_lists(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             student_name = data.get('student_name')
#             student_id = data.get('student_id')
#             branch = data.get('branch')

            
#             if Student_detials.objects.filter(student_name=student_name).exists():
#                 response = {"success": False, "response": "Student name is already taken"}
#             else:
                
#                 students = Student_detials.objects.create(student_name=student_name, student_id=student_id, branch=branch)
#                 students.save()
#                 response = {"success": True, "response": "Added new student successfully!!"}

#         except Exception as e:
#             response = {"success": False, "response": str(e)}
#         return JsonResponse(response)
    
#     elif request.method == 'GET':
#         search = request.GET.get('search', '').strip()
#         sort_by = request.GET.get('sort_by', 'student_name')
#         order = request.GET.get('order', 'asc')
        
#         if order == 'desc':
#             sort_by = f'-{sort_by}'
#         else:
#             sort_by = sort_by.strip()

        
      
#         if search:
#             students = Student_detials.objects.filter(
#                 Q(student_name__icontains=search) | Q(student_id__icontains=search)
#             ).order_by(sort_by)
#         else:
#             students = Student_detials.objects.all().order_by(sort_by)

   
#         if students.exists():
#             student_list = list(students.values('student_name', 'student_id', 'branch'))
#             response = {'success': True, 'students': student_list}
#         else:
#             response = {"success": False, "response": "No students found"}
        
#         return JsonResponse(response, safe=False)
    
#     else:
#         return JsonResponse({"success": False, "response": "Method not allowed"}, status=405)
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Market, BedroomData
from .serializers import MarketSerializer, BedroomDataSerializer

class MarketApi(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

    # @action(detail=True, methods=['get'])
    # def bedroom_data(self, request, pk=None):
    #     market = self.get_object()
    #     bedroom_data = BedroomData.objects.filter(market=market)
    #     serializer = BedroomDataSerializer(bedroom_data, many=True)
    #     return Response(serializer.data)

class BedroomDataApi(viewsets.ModelViewSet):
    queryset = BedroomData.objects.all()
    serializer_class = BedroomDataSerializer

    # def get_queryset(self):
    #     queryset = BedroomData.objects.all()
    #     market_id = self.request.query_params.get('market_id', None)
    #     if market_id is not None:
    #         queryset = queryset.filter(market_id=market_id)
    #     return queryset

    # @action(detail=False, methods=['get'])
    # def by_market(self, request):
    #     market_id = request.query_params.get('market_id', None)
    #     if market_id is None:
    #         return Response({"error": "market_id is required"}, status=400)
        
    #     market = get_object_or_404(Market, id=market_id)
    #     bedroom_data = BedroomData.objects.filter(market=market)
    #     serializer = self.get_serializer(bedroom_data, many=True)
    #     return Response(serializer.data)