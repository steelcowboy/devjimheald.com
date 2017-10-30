$(document).ready(function mobileCSS() {
    //var circles = $(".info-pane-child")
    //circles.css("width", circles.height());

    if ( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) )
    {
        var titleHeight = $("#title-block").height()
        var contMargin = parseInt($(".container").css('margin-top'), 10);
        var remainingHeight = $(window).height() - titleHeight - contMargin;

        $(".row").css("max-height", remainingHeight);

        $(".info-pane").click(function(event) {
            // First look for a double click
            if ( $(this).is(mobileCSS.selectedElement) )
            {
                return true;
            }

            // Now get rid of any old changes
            if (typeof mobileCSS.selectedElement == 'undefined')
            {
                mobileCSS.selectedElement = $(this);
            }
            else
            {
                toggleCircles(false, mobileCSS.selectedElement);
            }

            // Finally apply new changes
            mobileCSS.selectedElement = $(this);
            toggleCircles(true, $(this));
        });
    }
});

function toggleCircles(link, targ)
{
    var onElem;
    var offElem;
    
    onElem = link ? ".info-pane-overlay" : ".info-pane-content";
    offElem = link ? ".info-pane-content" : ".info-pane-overlay";

    targ.find(offElem).animate({
        opacity: 0
    }, 100, function() {});

    var overlay = targ.find(onElem);
    overlay.animate({
        opacity: 1
    }, 100, function() {
         overlay.css('pointer-events', 'auto');   
    });
}
