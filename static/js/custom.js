let autocomplete;

function initAutoComplete(){
autocomplete = new google.maps.places.Autocomplete(
    document.getElementById('id_full_address'),
    {
        types: ['geocode', 'establishment'],
        //default in this app is "IN" - add your country code
        //componentRestrictions: {'country': ['us']},
    })
// function to specify what should happen when the prediction is clicked
autocomplete.addListener('place_changed', onPlaceChanged);
}

function onPlaceChanged (){
    var place = autocomplete.getPlace();

    // User did not select the prediction. Reset the input field or alert()
    if (!place.geometry){
        document.getElementById('id_full_address').placeholder = "Start typing...";
    }
    else{
        // console.log('place name=>', place.name)
    }

    // get the address components and assign them to the fields
    //console.log(place);

    // loop through the address components and assign other address data

    let streetName = '';
    let streetNumber = '';
    console.log(place.address_components);
    for(var i=0; i < place.address_components.length; i++){
        for(var j=0; j < place.address_components[i].types.length; j++){
            // get country
            if(place.address_components[i].types[j] == 'country'){
                $('#id_country').val(place.address_components[i].long_name);
            }
            // get state
            if(place.address_components[i].types[j] == 'administrative_area_level_1'){
                $('#id_state').val(place.address_components[i].short_name);
            }

            // get city
            if(place.address_components[i].types[j] == 'administrative_area_level_2'){
                $('#id_city').val(place.address_components[i].long_name);
            }

            // get neighborhood
            if(place.address_components[i].types[j] == 'sublocality_level_1'){
                $('#id_neighborhood').val(place.address_components[i].long_name);
            }

            // get Street Address
            if(place.address_components[i].types[j] == 'route'){
                streetName = place.address_components[i].long_name
            }

            // get Street Number
            if(place.address_components[i].types[j] == 'street_number'){
                streetNumber = place.address_components[i].long_name;
            }

            // get Zip Code
            if(place.address_components[i].types[j] == 'postal_code'){
                $('#id_zip_code').val(place.address_components[i].long_name);
            } else {
                $('#id_zip_code').val("");
            }
        }
    }

    // AFTER THE LOOP, set the full street address
    if (streetName || streetNumber) {
        let fullAddress = streetName;
        if (streetNumber) {
            fullAddress += `, ${streetNumber}`;
        }
        $('#id_street_address').val(fullAddress);
    }
}

