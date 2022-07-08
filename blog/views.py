from django.shortcuts import render


# Create your views here.
def BlogHome(request):
    template_name = 'blog/bloghome.html'
    # form =
    context = {
        # 'from': form,
    }
    return render(request, template_name, context)
