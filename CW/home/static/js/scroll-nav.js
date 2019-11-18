var pc = window.pageYOffset;
    window.onscroll = function () {
      var c = window.pageYOffset;
      if (pc > c) {
        document.getElementById("navbar").style.top = "0";
      } else {
        document.getElementById("navbar").style.top = "-100px"
      }

      pc = c;
    }