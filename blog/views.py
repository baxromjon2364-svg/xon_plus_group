from django.shortcuts import render, redirect
from .models import Product, OrderRequest,CompletedProject
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, OrderRequest
from django.contrib import messages





# 1. BOSH SAHIFA (INDEX)
def index_view(request):
    if request.method == "POST":
        mijoz_ismi = request.POST.get('ism')
        mijoz_teli = request.POST.get('telefon')
        tanlangan_uskuna_id = request.POST.get('uskuna_id')

        uskuna = Product.objects.filter(id=tanlangan_uskuna_id).first()
        uskuna_nomi = uskuna.nomi if uskuna else "Noma'lum uskuna"

        OrderRequest.objects.create(
            ism=mijoz_ismi,
            telefon=mijoz_teli,
            uskuna_nomi=uskuna_nomi
        )
        messages.success(request, "Arizangiz muvaffaqiyatli qabul qilindi!")
        return redirect('home')
    all_products = Product.objects.all()
    latest_products = all_products.order_by('-id')[:3]
    completed_projects = CompletedProject.objects.all().order_by('-id')[:6]
    context = {
        'products': latest_products,
        'all_products': all_products,
        'completed_projects': completed_projects,
    }
    return render(request, 'index.html', context)


# 2. TO'LIQ USKUNALAR SAHIFASI (PRODUCTS)

def all_products_view(request):
    if request.method == "POST":
        mijoz_ismi = request.POST.get('ism')
        mijoz_teli = request.POST.get('telefon')
        tanlangan_uskuna_id = request.POST.get('uskuna_id')

        uskuna = Product.objects.filter(id=tanlangan_uskuna_id).first()
        uskuna_nomi = uskuna.nomi if uskuna else "Noma'lum uskuna"

        OrderRequest.objects.create(
            ism=mijoz_ismi,
            telefon=mijoz_teli,
            uskuna_nomi=uskuna_nomi
        )
        messages.success(request, "Arizangiz muvaffaqiyatli qabul qilindi!")
        return redirect('all_products')

    products = Product.objects.all().order_by('-id')
    return render(request, 'products.html', {'products': products})





def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        mijoz_ismi = request.POST.get('ism')
        mijoz_teli = request.POST.get('telefon')
        OrderRequest.objects.create(
            ism=mijoz_ismi,
            telefon=mijoz_teli,
            uskuna_nomi=product.nomi
        )
        messages.success(request, f"{product.nomi} uchun arizangiz muvaffaqiyatli qabul qilindi!")
        return redirect('product_detail', pk=pk)

    return render(request, 'product_detail.html', {'product': product})
