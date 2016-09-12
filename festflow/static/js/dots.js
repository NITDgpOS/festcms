	/*********************
       Device Detection
    *********************/

	var isWebkit = /Webkit/i.test(navigator.userAgent),
		isChrome = /Chrome/i.test(navigator.userAgent),
		isMobile = !!("ontouchstart" in window),
		isAndroid = /Android/i.test(navigator.userAgent),
		isIE = document.documentMode;

	/******************
    	Redirection
    ******************/

	if (isMobile && isAndroid && !isChrome) {
		alert("Although Velocity.js works on all mobile browsers, this 3D demo is for iOS devices or Android devices running Chrome only. Redirecting you to Velocity's documentation.");
		window.location = "index.html";
	}

	/***************
    	Helpers
    ***************/

	/* Randomly generate an integer between two numbers. */
	function r (min, max) {
	    return Math.floor(Math.random() * (max - min + 1)) + min;
	}

	/* Override the default easing type with something a bit more jazzy. */
	$.Velocity.defaults.easing = "easeInOutsine";

	/*******************
        Dot Creation
    *******************/

    /* Differentiate dot counts based on roughly-guestimated device and browser capabilities. */ 
	var dotsCount,
		dotsHtml = "",
		$count = $("#count"),
		$dots;

	if (window.location.hash) {
		dotsCount = window.location.hash.slice(1);
	} else {
		dotsCount = isMobile ? (isAndroid ? 40 : 60) : (isChrome ? 175 : 125);
	}

	for (var i = 0; i < dotsCount; i++) {
		dotsHtml += "<div class='dot'></div>";
	}

	$dots = $(dotsHtml);

	$count.html(dotsCount);

	/*************
        Setup
    *************/

	var $container = $("#dots-container"),
		$browserWidthNotice = $("#browserWidthNotice"),
		$welcome = $("#welcome");

	var screenWidth = window.screen.availWidth,
		screenHeight = window.screen.availHeight,
		chromeHeight = screenHeight - (document.documentElement.clientHeight || screenHeight);

	var translateZMin = -725,
		translateZMax = 600;

	var containerAnimationMap = {
			perspective: [ 215, 50 ],
			opacity: [ 0.90, 0.55 ]
		};

	/* IE10+ produce odd glitching issues when you rotateZ on a parent element subjected to 3D transforms. */
	if (!isIE) {
		containerAnimationMap.rotateZ = [ 5, 0 ];
	}

	/* Ensure the user is full-screened; this demo's translations are relative to screen width, not window width. */
	if ((document.documentElement.clientWidth / screenWidth) < 0.80) {
		$browserWidthNotice.show();
	}

	/*****************
        Animation
    *****************/

    /* Fade out the welcome message. */
//	$welcome.velocity({ opacity: [ 0, 0.65 ] }, { display: "none", delay: 3500, duration: 1100 });

	/* Animate the dots' container. */
	$container
		.css("perspective-origin", screenWidth/2 + "px " + ((screenHeight * 0.45) - chromeHeight) + "px")
		.velocity(containerAnimationMap, { duration: 800, loop: 1, delay: 3250 });

	/* Special visual enhancement for WebKit browsers, which are faster at box-shadow manipulation. */
	if (isWebkit) {
		$dots.css("boxShadow", "0px 0px 4px 0px #4bc2f1");
	}

	/* Animate the dots. */
	$dots
		.velocity({ 
			translateX: [ 
				function() { return "+=" + r(-screenWidth/2.5, screenWidth/2.5) },
				function() { return r(0, screenWidth) }
			],
			translateY: [
				function() { return "+=" + r(-screenHeight/2.75, screenHeight/2.75) },
				function() { return r(0, screenHeight) }
			],
			translateZ: [
				function() { return "+=" + r(translateZMin, translateZMax) },
				function() { return r(translateZMin, translateZMax) }
			],
			opacity: [ 
				function() { return Math.random() },
				function() { return Math.random() + 0.1 }
			]
		}, { duration: 6000, loop: true })
		.velocity("reverse", { easing: "easeOutQuad" }).appendTo($container);