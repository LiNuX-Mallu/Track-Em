from django.shortcuts import render
# Create your views here.
import os

def main(request):
 with open("data/data","w") as f:
  f.write(str(dict(request.GET)))
  f.flush()
  os.fsync(f)
 return render(request,"ui.html")

