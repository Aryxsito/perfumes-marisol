from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import PerfumeForm
from .models import Perfume


def index(request):
    query = request.GET.get("q", "").strip()
    perfumes = Perfume.objects.all()

    if query:
        perfumes = perfumes.filter(
            Q(nombre__icontains=query) | 
            Q(inspiracion__icontains=query) |
            Q(acordes__nombre__icontains=query)
        ).distinct()

    context = {
        "perfumes": perfumes,
        "query": query,
    }
    return render(request, "perfumes/index.html", context)


def perfume_detail(request, pk):
    perfume = get_object_or_404(Perfume, pk=pk)
    return render(request, "perfumes/detail.html", {"perfume": perfume})


@login_required(login_url="login")
def perfume_create(request):
    if not request.user.is_staff:
        messages.error(request, "No tienes permiso para crear perfumes.")
        return redirect("index")
    
    if request.method == "POST":
        form = PerfumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto agregado exitosamente al catálogo.")
            return redirect("index")
    else:
        form = PerfumeForm()

    return render(
        request,
        "perfumes/form_perfume.html",
        {"form": form, "title": "Agregar Perfume"},
    )


@login_required(login_url="login")
def perfume_update(request, pk):
    if not request.user.is_staff:
        messages.error(request, "No tienes permiso para editar perfumes.")
        return redirect("index")
    
    perfume = get_object_or_404(Perfume, pk=pk)

    if request.method == "POST":
        form = PerfumeForm(request.POST, request.FILES, instance=perfume)
        if form.is_valid():
            form.save()
            messages.success(request, "Cambios guardados exitosamente.")
            return redirect("index")
    else:
        form = PerfumeForm(instance=perfume)

    return render(
        request,
        "perfumes/form_perfume.html",
        {"form": form, "title": "Editar Perfume"},
    )


@require_POST
@login_required(login_url="login")
def perfume_delete(request, pk):
    if not request.user.is_staff:
        messages.error(request, "No tienes permiso para eliminar perfumes.")
        return redirect("index")
    
    perfume = get_object_or_404(Perfume, pk=pk)
    perfume.delete()
    messages.success(request, "Producto eliminado del catálogo.")
    return redirect("index")


@require_POST
@login_required(login_url="login")
def update_stock(request, pk):
    if not request.user.is_staff:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            from django.http import JsonResponse
            return JsonResponse({"error": "No tienes permiso para modificar stock."}, status=403)
        messages.error(request, "No tienes permiso para modificar stock.")
        return redirect("index")
    
    perfume = get_object_or_404(Perfume, pk=pk)
    action = request.POST.get("action")

    if action == "increment":
        perfume.stock += 1
    elif action == "decrement" and perfume.stock > 0:
        perfume.stock -= 1

    perfume.save(update_fields=["stock"])
    
    # Si es una petición AJAX, devolver JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        from django.http import JsonResponse
        return JsonResponse({"success": True, "new_stock": perfume.stock})
    
    return redirect("index")


def login_view(request):
    from django.contrib.auth import authenticate, login
    
    if request.user.is_authenticated:
        return redirect("index")
    
    errors = {}
    
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        
        if not username:
            errors['username'] = "El usuario es requerido."
        if not password:
            errors['password'] = "La contraseña es requerida."
        
        if not errors:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenida, {user.first_name or user.username}. Acceso establecido.")
                return redirect("index")
            else:
                errors['general'] = "Usuario o contraseña inválidos."
    
    return render(request, "perfumes/login.html", {'errors': errors})


def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    messages.success(request, "Sesión cerrada exitosamente.")
    return redirect("index")
