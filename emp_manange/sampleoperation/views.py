# from django.shortcuts import render
# from django.http import JsonResponse
# from django.db import IntegrityError
# from sampleoperation.models import emp

# def create_user(request):
#     if request.method == 'POST':
#         fullname = request.POST.get('fullname', None)
#         if fullname:
#             try:
#                 user = emp.objects.create(fullname=fullname)
#                 return JsonResponse({'message': 'User created successfully'})
#             except IntegrityError:
#                 return JsonResponse({'error': 'User with this fullname already exists'}, status=400)
#         else:
#             return JsonResponse({'error': 'Fullname is required'}, status=400)
#     else:
#         return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)



from django.http import JsonResponse
from asyncpg.exceptions import UniqueViolationError
from sampleoperation.models import emp
from asgiref.sync import sync_to_async

# async def create_user(request):
#     if request.method == 'POST':
#         fullname = request.POST.get('fullname', None)
#         if fullname:
#             try:
#                 import time,random 
#                 time.sleep(random.randint(5,10))
#                 print(" dsafsd")
#                 # Use sync_to_async to call the synchronous function in an asynchronous context
#                 user = await sync_to_async(emp.objects.create)(fullname=fullname)
#                 return JsonResponse({'message': 'User created successfully'})
#             except UniqueViolationError:
#                 return JsonResponse({'error': 'User with this fullname already exists'}, status=400)
#             except Exception as e:
#                 return JsonResponse({'error': str(e)}, status=500)
#         else:
#             return JsonResponse({'error': 'Fullname is required'}, status=400)
#     else:
#         return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


async def create_user(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname', None)
        if fullname:
            try:
                
                user = await emp.objects.create(fullname=fullname)
                return JsonResponse({'message': 'User created successfully'})
            except UniqueViolationError:
                return JsonResponse({'error': 'User with this fullname already exists'}, status=400)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Fullname is required'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
