const inputElements = document.querySelectorAll('.inp');
const createButton = document.querySelector('.crt-btn');

createButton.addEventListener('click', () => {
    const inputDict = Object.fromEntries(
        Array.from(inputElements)
            .filter(iE => iE.id)
            .map(iE => [iE.id, iE.value])
    );

    // Send Data to API
    // Retreive Result Code
    // Show Message if error
    
})