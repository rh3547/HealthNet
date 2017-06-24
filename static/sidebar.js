var open = false;

function sidebarToggle() {
  if (!open) {
    sidebarOpen();
  }
  else {
    sidebarClose();
  }
}

function sidebarOpen() {
  // Animate the width of the sidebar header
  $("#sidebar-header").animate({
    left: "0px"
  }, 400, function() {
  });
  // Animiate the width of the sidebar itself
  $("#sidebar").animate({
    left: "0px"
  }, 400, function() {
  });

  barsToX("bar1", "bar2", "bar3");

  open = true;
}

function sidebarClose() {
  // Animate the width of the sidebar header
  $("#sidebar-header").animate({
    left: "-230px"
  }, 400, function() {
  });
  // Animiate the width of the sidebar itself
  $("#sidebar").animate({
    left: "-230px"
  }, 400, function() {
  });

  xToBars("bar1", "bar2", "bar3");

  open = false;
}

function barsToX(bar1, bar2, bar3) {
  $("#" + bar1).removeClass('rotate-minus-45');
  $("#" + bar2).removeClass('rotate-minus-45');
  $("#" + bar3).removeClass('rotate-45');

  $("#" + bar1).removeClass('rotate-0');
  $("#" + bar2).removeClass('rotate-0');
  $("#" + bar3).removeClass('rotate-0');

  $("#" + bar1).animate({
    top: "30px"
  }, 200, function() {
  });
  $("#" + bar2).animate({
    top: "30px"
  }, 200, function() {
  });
  $("#" + bar3).animate({
    top: "30px"
  }, 200, function() {
    $("#" + bar1).addClass('rotate-45');
    $("#" + bar2).addClass('rotate-45');
    $("#" + bar3).addClass('rotate-minus-45');
    if(navigator.userAgent.match("Chrome")){
      document.getElementById(bar1).style.WebkitTransform = "rotate(45deg)";
    } else if(navigator.userAgent.match("Firefox")){
      document.getElementById(bar1).style.MozTransform = "rotate(45deg)";
    } else if(navigator.userAgent.match("MSIE")){
      document.getElementById(bar1).style.msTransform = "rotate(45deg)";
    } else if(navigator.userAgent.match("Opera")){
      document.getElementById(bar1).style.OTransform = "rotate(45deg)";
    } else {
      document.getElementById(bar1).style.transform = "rotate(45deg)";
    }
    if(navigator.userAgent.match("Chrome")){
      document.getElementById(bar2).style.WebkitTransform = "rotate(45deg)";
    } else if(navigator.userAgent.match("Firefox")){
      document.getElementById(bar2).style.MozTransform = "rotate(45deg)";
    } else if(navigator.userAgent.match("MSIE")){
      document.getElementById(bar2).style.msTransform = "rotate(45deg)";
    } else if(navigator.userAgent.match("Opera")){
      document.getElementById(bar2).style.OTransform = "rotate(45deg)";
    } else {
      document.getElementById(bar2).style.transform = "rotate(45deg)";
    }
    if(navigator.userAgent.match("Chrome")){
      document.getElementById(bar3).style.WebkitTransform = "rotate(-45deg)";
    } else if(navigator.userAgent.match("Firefox")){
      document.getElementById(bar3).style.MozTransform = "rotate(-45deg)";
    } else if(navigator.userAgent.match("MSIE")){
      document.getElementById(bar3).style.msTransform = "rotate(-45deg)";
    } else if(navigator.userAgent.match("Opera")){
      document.getElementById(bar3).style.OTransform = "rotate(-45deg)";
    } else {
      document.getElementById(bar3).style.transform = "rotate(-45deg)";
    }
  });
}

function xToBars(bar1, bar2, bar3) {
  $("#" + bar1).removeClass('rotate-45');
  $("#" + bar2).removeClass('rotate-45');
  $("#" + bar3).removeClass('rotate-minus-45');

  $("#" + bar1).addClass('rotate-0');
  $("#" + bar2).addClass('rotate-0');
  $("#" + bar3).addClass('rotate-0');

  $("#" + bar1).animate({
    top: "20px"
  }, 200, function() {
  });
  $("#" + bar2).animate({
    top: "30px"
  }, 200, function() {
  });
  $("#" + bar3).animate({
    top: "40px"
  }, 200, function() {
    if(navigator.userAgent.match("Chrome")){
      document.getElementById(bar1).style.WebkitTransform = "rotate(0deg)";
    } else if(navigator.userAgent.match("Firefox")){
      document.getElementById(bar1).style.MozTransform = "rotate(0deg)";
    } else if(navigator.userAgent.match("MSIE")){
      document.getElementById(bar1).style.msTransform = "rotate(0deg)";
    } else if(navigator.userAgent.match("Opera")){
      document.getElementById(bar1).style.OTransform = "rotate(0deg)";
    } else {
      document.getElementById(bar1).style.transform = "rotate(0deg)";
    }
    if(navigator.userAgent.match("Chrome")){
      document.getElementById(bar2).style.WebkitTransform = "rotate(0deg)";
    } else if(navigator.userAgent.match("Firefox")){
      document.getElementById(bar2).style.MozTransform = "rotate(0deg)";
    } else if(navigator.userAgent.match("MSIE")){
      document.getElementById(bar2).style.msTransform = "rotate(0deg)";
    } else if(navigator.userAgent.match("Opera")){
      document.getElementById(bar2).style.OTransform = "rotate(0deg)";
    } else {
      document.getElementById(bar2).style.transform = "rotate(0deg)";
    }
    if(navigator.userAgent.match("Chrome")){
      document.getElementById(bar3).style.WebkitTransform = "rotate(0deg)";
    } else if(navigator.userAgent.match("Firefox")){
      document.getElementById(bar3).style.MozTransform = "rotate(0deg)";
    } else if(navigator.userAgent.match("MSIE")){
      document.getElementById(bar3).style.msTransform = "rotate(0deg)";
    } else if(navigator.userAgent.match("Opera")){
      document.getElementById(bar3).style.OTransform = "rotate(0deg)";
    } else {
      document.getElementById(bar3).style.transform = "rotate(0deg)";
    }
  });
}

function topbarToggle() {
  if (!open) {
    topbarOpen();
  }
  else {
    topbarClose();
  }
}

function topbarOpen() {
  $("#topbar").animate({
    height: "100%"
  }, 400, function() {
  });

  barsToX("topbar-bar1", "topbar-bar2", "topbar-bar3");

  open = true;
}

function topbarClose() {
  $("#topbar").animate({
    height: "0"
  }, 400, function() {
  });

  xToBars("topbar-bar1", "topbar-bar2", "topbar-bar3");

  open = false;
}
