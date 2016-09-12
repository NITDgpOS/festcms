jQuery(function($) {'use strict',

	
	// all Parallax Section
	$(window).load(function(){'use strict',
		$("#services").parallax("90%", 0.3);
		$("#clients").parallax("50%", 0.3);
		// var aboutUs = $('#about-us').find('.jumbotron');
		// aboutUs.css('opacity',0);
		// new Waypoint({
			// element: $('#about-us'),
			// handler: function(){
				// aboutUs.addClass('animated fadeInUp');
			// },
			// offset: '90%'
		// });
	});
	
	// portfolio filter
	$(window).load(function(){'use strict',
		$portfolio_selectors = $('.portfolio-filter >li>a');
		if($portfolio_selectors!='undefined'){
			$portfolio = $('.portfolio-items');
			$portfolio.isotope({
				itemSelector : '.col-sm-3',
				layoutMode : 'fitRows'
			});
			
			$portfolio_selectors.on('click', function(){
				$portfolio_selectors.removeClass('active');
				$(this).addClass('active');
				var selector = $(this).attr('data-filter');
				$portfolio.isotope({ filter: selector });
				return false;
			});
		}
	});
	
	//Pretty Photo
	 $("a[data-gallery^='prettyPhoto']").prettyPhoto({
	  social_tools: false
	 });


	// Contact form validation
	var form = $('.contact-form');
	form.submit(function () {'use strict',
		$this = $(this);
		$.post($(this).attr('action'), function(data) {
			$this.prev().text(data.message).fadeIn().delay(3000).fadeOut();
		},'json');
		return false;
	});


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

	// Skill bar Function

	jQuery(document).ready(function(){
	jQuery('.skillbar').each(function(){
		jQuery(this).find('.skillbar-bar').animate({
			width:jQuery(this).attr('data-percent')
		},6000);
	});
});
