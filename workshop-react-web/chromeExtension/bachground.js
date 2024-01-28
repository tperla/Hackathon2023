chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    const textToTranslate = request.text;
    // Call the translation API here and get the translated text
    const translatedText = 'This is the translated text'; // Replace this with the actual translation
    sendResponse({ translation: translatedText });
});
