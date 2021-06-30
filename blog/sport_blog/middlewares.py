# from time import time
#
#
# # from .models import Logger
#
#
# class MetrikaMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         print('-----------BEFORE')
#         st = time()
#         response = self.get_response(request)
#         print('----------AFTER')
#         print(f'Time execute: {time() - st}; path: {request.path}')
#
#         return response
#
#
# class SimpleMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         print('-----------SimpleMiddleware BEFORE')
#         # Code to be executed for each request BEFORE
#         # the view (and later middleware) are called.
#
#         response = self.get_response(request)
#         print('-----------SimpleMiddleware AFTER')
#         # Code to be executed for each request/response AFTER
#         # the view is called.
#
#         return response
#
#
# # class LoggerMiddleware:
# #     def __init__(self, get_response):
# #         self.get_response = get_response
# #
# #     def __call__(self, request):
# #         response = self.get_response(request)
# #         st = time()
# #         utm = request.GET.get('utm')
# #         if utm:
# #             time_exec = time() - st
# #             metrika = Logger(utm=utm, time_exec=time_exec)
# #             metrika.save()
# #
# #         return response
