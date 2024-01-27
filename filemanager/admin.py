from django.contrib import admin
from .models import User, Department, File, Folder, Template

# 注册您的模型以在admin界面中使用
admin.site.register(User)
admin.site.register(Department)
admin.site.register(File)
admin.site.register(Folder)
admin.site.register(Template)
