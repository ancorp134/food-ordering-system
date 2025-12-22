from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .service import get_cart,save_cart,delete_cart

# Create your views here.


class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user_id = request.user.token.get("user_id")
        cart= get_cart(user_id)

        if not cart:
            return Response({"status" : "Cart is Empty"},status=status.HTTP_200_OK)
        
        return Response(cart,status=status.HTTP_200_OK)
    
    def delete(self,request):
        user_id = request.user.token.get("user_id")
        cart= get_cart(user_id)

        if not cart:
            return Response({"status" : "Cart is Empty"},status=status.HTTP_200_OK)
        
        return Response({"status" : "Cart is Cleared"},status=status.HTTP_200_OK)
    


class CartItemAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request):
        user_id = request.user.token.get("user_id")
        payload = request.data
        cart= get_cart(user_id)

        if not cart:
            cart = {
                "restaurant_id" : payload["restaurant_id"],
                "items" : []
            }

        if cart["restaurant_id"] != payload["restaurant_id"]:
            return Response(
                {"detail": "Cart can contain items from only one restaurant"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        for item in cart["items"]:
            if item["menu_item_id"] == payload["menu_item_id"]:
                item["quantity"] += payload["quantity"]
                save_cart(user_id,cart)
                return Response(cart,status=status.HTTP_201_CREATED)
            
        cart["items"].append({
            "menu_item_id": payload["menu_item_id"],
            "quantity": payload["quantity"],
            "price": payload["price"]
        })

        save_cart(user_id, cart)
        return Response(cart, status=status.HTTP_201_CREATED)

        


class CartItemDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self,request,item_id):

        user_id= request.user.token.get("user_id")
        cart = get_cart(user_id)
        payload = request.data

        if not cart:
            return Response({"detail": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)
        
        print(item_id)
        for item in cart["items"]:
            print(item["menu_item_id"])
            if str(item["menu_item_id"]) == str(item_id):
                item["quantity"] = payload["quantity"]
                save_cart(user_id,cart)
                return Response(cart,status=status.HTTP_200_OK)
            

        return Response({"detail": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
    


    def delete(self,request,item_id):

        user_id= request.user.token.get("user_id")
        cart = get_cart(user_id)
    

        if not cart:
            return Response({"detail": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)
        
        cart["items"] = [item for item in cart["items"] if str(item["menu_item_id"]) != str(item_id)]

        save_cart(user_id,cart)
        return Response(cart,status=status.HTTP_200_OK)


        