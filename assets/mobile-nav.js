/**
 * @type {HTMLElement | null | undefined}
 */
var mobileNav = null;
var arrowIcon = null;
/**
 * @type {boolean}
 */
var isOpen = false;

if (typeof attachEventToDash !== 'undefined') {
    attachEventToDash('mobile-menu-btn', 'click', function () {
        if (mobileNav === null) {
            mobileNav = document.getElementById('nav-section')
            if (!mobileNav) {
                return;
            }
        }
        if (arrowIcon === null) {
           arrowIcon = document.getElementById('menu-arrow');
           if (!arrowIcon) {
               return;
           }
       }
        // Toggle display of the mobile navigation
        mobileNav.style.display = isOpen ? 'none' : 'inline-block';
        // Rotate the arrow icon
        arrowIcon.innerHTML = isOpen ? '▼' : '▲'; // Swaps the down arrow with an up arrow
        // Toggle the open state
        isOpen = !isOpen;
    }, false)
}

// Event delegation to handle clicks on navigation links
document.addEventListener('click', function(event) {
   var target = event.target;
   if (target.tagName === 'A' && target.closest('#mobile-navigation-items')) {
       if (mobileNav) {
           mobileNav.style.display = 'none';
           isOpen = false;
           if (arrowIcon) {
               arrowIcon.innerHTML = '▼';
           }
       }
   }
});

function debounce(func, time) {
    var timer;
    return function (event) {
        if (timer) clearTimeout(timer);
        timer = setTimeout(func, time, event);
    };
}

// Handle resizing to ensure the menu and icon state reset appropriately
window.addEventListener(
    "resize",
    debounce(function () {
        if (mobileNav) {
            var mq = window.matchMedia("(min-width: 992px)");
            if (mq.matches) {
                isOpen = false;
                mobileNav.style.display = 'none';
                if (arrowIcon) {
                   arrowIcon.innerHTML = '▼';
                }
            }
        }
    }, 150)
);
