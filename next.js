// Save text and date
// Make it accessble at later dates
let items = [];

const storageKey = "items";

function saveItem(items) {
    const stringItems = JSON.stringify(items);
    localStorage.setItem(storageKey, stringItems);
}
function loadItems(items, storageKey) {
    const oldItems = localStorage.getItem(storageKey)
    if (oldItems) items = JSON.parse(oldItems)
    renderItems()
}