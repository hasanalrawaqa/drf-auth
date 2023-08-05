from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    message = "if  you are not the owner,you can't edit or delete !"
    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True
        
        if request.user == obj.owner :
            return True 
        else : 
            return False 
      

      