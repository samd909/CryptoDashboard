let currentDivIndex = 0;
const divs = [document.getElementById('trending-div'), document.getElementById('highest-coins-div')];
const switchInterval = 5000; // 5 seconds

function switchDivs() {
    // Remove classes from the current div
    divs[currentDivIndex].classList.remove('slide-in');
    divs[currentDivIndex].classList.add('slide-out');

    // Toggle to the next div
    currentDivIndex = (currentDivIndex + 1) % divs.length;

    // Add classes to the next div
    divs[currentDivIndex].classList.remove('slide-out');
    divs[currentDivIndex].classList.add('slide-in');
}

// Initial call to show the first div
setTimeout(() => divs[0].classList.add('slide-in'), 0);

// Switch divs every 5 seconds
setInterval(switchDivs, switchInterval);