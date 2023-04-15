from .models import Basket

def basketsLength(request):
   if request.user.is_authenticated:
      baskets = Basket.objects.filter(user=request.user)
   else:
      baskets = []
   
   return {"basketsLength":len(baskets)}

