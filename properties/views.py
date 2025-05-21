from django.shortcuts import get_object_or_404, render, redirect
from .models import Property, PropertyImage
from .forms import PropertyForm, AddressForm
from django.templatetags.static import static


# Create your views here.
def index(request):
    properties = Property.objects.all()
    default_image_url = static("images/images/default.jpg")

    for prop in properties:
        real_images = list(prop.images.all())
        real_images_urls = [img.image.url for img in real_images]

        # Fill with default images up to 5
        filled_images = real_images_urls + [default_image_url] * (
            5 - len(real_images_urls)
        )
        prop.carousel_images = filled_images[:5]  # attach to each property

    context = {"properties": properties}

    return render(request, "properties/index.html", context=context)


def register_property(request):
    if request.method == "POST":
        address_form = AddressForm(request.POST)
        property_form = PropertyForm(request.POST)

        if address_form.is_valid() and property_form.is_valid():
            address_obj = address_form.save()
            property_obj = property_form.save(commit=False)
            property_obj.address = address_obj
            property_obj.user = request.user
            property_obj.save()

            images = request.FILES.getlist("images")
            if len(images) > 10:
                error = "You can only have 10 images in total."
                context = {
                    "address_form": address_form,
                    "property_form": property_form,
                    "error": error,
                }

                return render(request, "properties/register_property.html", context)

            for img in images:
                PropertyImage.objects.create(property=property_obj, image=img)

            return redirect("index")
        else:
            print(address_form.errors)
            print(property_form.errors)
    else:
        address_form = AddressForm()
        property_form = PropertyForm()

    context = {
        "address_form": address_form,
        "property_form": property_form,
    }

    return render(request, "properties/register_property.html", context)


def edit_property(request, pk=None):
    property_obj = get_object_or_404(Property, pk=pk)

    if request.method == "POST":
        property_form = PropertyForm(request.POST, instance=property_obj)
        address_form = AddressForm(request.POST, instance=property_obj.address)

        if address_form.is_valid() and property_form.is_valid():
            address_obj = address_form.save()
            property_obj = property_form.save(commit=False)
            property_obj.address = address_obj
            property_obj.save()

            existing_images_count = property_obj.images.count()
            new_images = request.FILES.getlist('images')
            total_after_upload = existing_images_count + len(new_images)

            if total_after_upload > 10:
                error = "You can only have 10 images in total."
                context = {
                    "address_form": address_form,
                    "property_form": property_form,
                    "property": property_obj,
                    "error": error,
                }
                
                return render(request, "properties/edit_property.html", context)

            # Delete selected images
            delete_ids = request.POST.getlist("delete_images")
            PropertyImage.objects.filter(
                id__in=delete_ids, property=property_obj
            ).delete()

            # Add new images
            for img in new_images:
                PropertyImage.objects.create(property=property_obj, image=img)

            return redirect("index")
        else:
            print(address_form.errors)
            print(property_form.errors)
    else:
        address_form = AddressForm(instance=property_obj.address)
        property_form = PropertyForm(instance=property_obj)

    context = {
        "address_form": address_form,
        "property_form": property_form,
        "property": property_obj,
    }

    return render(request, "properties/edit_property.html", context)


def delete_property(request, pk=None):
    property_obj = get_object_or_404(Property, pk=pk)

    property_obj.delete()
    return redirect("index")
