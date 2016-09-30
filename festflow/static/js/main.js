jQuery(function($) {'use strict',


	// Navigation Scroll
	$(window).scroll(function(event) {
		Scroll();
	});

	$('.navbar-collapse ul li a').click(function() {  
		$('html, body').animate({scrollTop: $(this.hash).offset().top - 79}, 1000);
		return false;
	});

});

// Preloder script
jQuery(window).load(function(){'use strict';
	$(".preloader").delay(1600).fadeOut("slow").remove();
});

//Preloder script
jQuery(window).load(function(){'use strict';

	// Slider Height
	var slideHeight = $(window).height();
	$('#home .carousel-inner .item, #home .video-container').css('height',slideHeight);

	$(window).resize(function(){'use strict',
		$('#home .carousel-inner .item, #home .video-container').css('height',slideHeight);
	});

});


// User define function
 function Scroll() {
	// var contentTop      =   [];
	// var contentBottom   =   [];
	// var winTop      =   $(window).scrollTop();
	// var rangeTop    =   200;
	// var rangeBottom =   500;
	// $('.navbar-collapse').find('.scroll a').each(function(){
		// contentTop.push( $( $(this).attr('href') ).offset().top);
		// contentBottom.push( $( $(this).attr('href') ).offset().top + $( $(this).attr('href') ).height() );
	// })
	// $.each( contentTop, function(i){
		// if ( winTop > contentTop[i] - rangeTop ){
			// $('.navbar-collapse li.scroll')
			// .removeClass('active')
			// .eq(i).addClass('active');			
		// }
	// })

 };

	//map api
	
	var myCenter=new google.maps.LatLng(23.5509, 87.2904);
var marker;

function initialize()
{
var mapProp = {
  center:myCenter,
  zoom:16,
  mapTypeControl:true,
mapTypeControlOptions: {
    style:google.maps.MapTypeControlStyle.DROPDOWN_MENU
},
  scrollwheel:false,
  mapTypeId:google.maps.MapTypeId.HYBRID
  };

var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);

var marker=new google.maps.Marker({
  position:myCenter,
  animation:google.maps.Animation.BOUNCE
  });

marker.setMap(map);
}

google.maps.event.addDomListener(window, 'load', initialize);

