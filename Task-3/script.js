const display = document.getElementById('display');
const buttons = document.querySelectorAll('button');
const toggle = document.getElementById('toggle-theme');

// Toggle light mode
toggle.addEventListener('change', () => {
  document.body.classList.toggle('light-mode');
});

// Button click handling
buttons.forEach(button => {
  button.addEventListener('click', () => {
    const value = button.textContent;

    switch (value) {
      case 'AC':
        display.value = '';
        break;
      case 'C':
        display.value = display.value.slice(0, -1);
        break;
      case '=':
        try {
          display.value = Function('"use strict";return (' + display.value + ')')();
        } catch {
          display.value = 'Error';
        }
        break;
      default:
        display.value += value;
    }
  });
});
