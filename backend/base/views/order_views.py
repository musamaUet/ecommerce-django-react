from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from base.models import Order, OrderItem, ShippingAddress, Product
from base.serializers import ProductSerializer, OrderSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user = request.user
    data = request.data
    orderItems = data['orderitems']
    if orderItems and len(orderItems) == 0:
        return Response({ 'detail': 'No Order Item'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        print('user', user)
        # (1) Create Order
        order = Order.objects.create(
            user=user,
            paymentMethod=data['paymentMethod'],
            taxPrice=data['taxPrice'],
            shippingPrice=data['shippingPrice'],
            totalprice=data['totalPrice']
        )
        print('order', order)
        # (2) Create Shipping Address
        shipping = ShippingAddress.objects.create(
            order=order,
            address=data['shippingAddress']['address'],
            city=data['shippingAddress']['city'],
            postalCode=data['shippingAddress']['postalCode'],
            country=data['shippingAddress']['country']
        )
        # (3) Create Orderitems and set order to OrderItems relationship
        for i in orderItems:
            product = Product.objects.get(_id=i['product'])
            item=OrderItem.objects.create(
                product=product,
                order=order,
                name=product.name,
                qty=i['qty'],
                price=i['price'],
                image=product.image.url
            )
            # Update Product Stock
            product.countInStock -= item.qty
            product.save()
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderById(request, pk):
    user = request.user
    try:
        order = Order.objects.get(_id=pk)
        if user.is_staff or order.user==user:
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        else:
            return Response({'detail':'Not authorized to view this order'},status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print('err', err)
        return Response({'detail':'Order does not exists'}, status=status.HTTP_400_BAD_REQUEST)