from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from reviews.models import Review
from app.permissions import GlobalDefaultPermission
from reviews.serializers import ReviewModelSerializer


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer
