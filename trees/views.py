from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView 



from .models import Square, Tree


class TreeDetailView(DetailView):
    queryset = Tree.display.all()
    


class TreeListView(ListView):
    square = None
    paginate_by = 6 #mudar para 4 depois

    def get_queryset(self):
        queryset = Tree.display.all()

        
        square_slug = self.kwargs.get("slug")
        if square_slug:
            self.square = get_object_or_404(Square, slug=square_slug)
            queryset = queryset.filter(square=self.square)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["square"] = self.square
        context["squaries"] = Square.display.all()
        return context