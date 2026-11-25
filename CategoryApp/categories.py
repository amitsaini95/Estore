from .models import CategoryModel

def CategoryList(request):
    return {'categories':CategoryModel.objects.all()}