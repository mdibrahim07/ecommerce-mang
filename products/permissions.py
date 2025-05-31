def get_permissions(self):
    if self.action in ['create', 'update', 'partial_update', 'destroy']:
        return [IsAdminUser()]
    return [permissions.AllowAny()]
