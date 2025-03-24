const responses = [
    "Yes, absolutely!",
    "No, not today.",
    "Yeah i guess",
    "Are you crazy?",
    "Definitely.....not.",
    "Dumb question, yes.",
    "Ugh, no.",
    "Yeah do whatever :P",
    "No idea but you look kinda cute :3",
    "In a forever growing universe filled with millions of planets and possible life forms, does this really matter?"
];

function getRandomResponse() {
    const randomIndex = Math.floor(Math.random() * responses.length);  // Generate a random index
    const randomResponse = responses[randomIndex];  // Get the response from the list

    // Display the response in the paragraph element
    document.getElementById("response").innerText = randomResponse;
}