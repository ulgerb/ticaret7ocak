from .models import Basket

def basketsLength(request):
   baskets = Basket.objects.filter(user=request.user)
   
   return {"basketsLength":len(baskets)}