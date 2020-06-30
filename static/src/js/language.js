odoo.define('google_lang.language', function (require) {
    "use strict";
    var ajax = require('web.ajax');

        $(document).ready( function()
        {
//            $('#citybox').hide();
//            $('#statebox').hide();
console.log(' Alhumdolilah')
console.log('12')

function googleTranslateElementInit() {
	console.log('me called')
  new google.translate.TranslateElement({pageLanguage: 'en'}, 'google_translate_element');
}

//$("#postal_code").keyup(function(){
//console.log($('#postal_code').val());
  //  $("#postal_code").css("background-color", "pink");
  //});

        });

    //var A = ...;

   // return A;
});