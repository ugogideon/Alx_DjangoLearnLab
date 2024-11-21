## Permissions and Groups in Django

### Custom Permissions:
- `can_view`: Allows viewing books.
- `can_create`: Allows creating new books.
- `can_edit`: Allows editing existing books.
- `can_delete`: Allows deleting books.

### User Groups and Permissions:
- **Editors**: Can create and edit books.
- **Viewers**: Can only view books.
- **Admins**: Can view, create, edit, and delete books.

### Enforcing Permissions in Views:
- The `@permission_required` decorator is used to restrict access to certain views based on user permissions.
