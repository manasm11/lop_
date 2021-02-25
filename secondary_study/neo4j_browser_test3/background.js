const allowed_url_regex = /https:\/\/www.google\.com\//
console.log('background.js executing')

chrome.tabs.onUpdated.addListener(tabId => {
    console.log('tab switched', tabId)
    // add_styles_and_foreground(tab.tabId)
    add_styles_and_foreground(tabId)
})
chrome.tabs.onActivated.addListener(tab => {
    console.log('tab switched', tab)
    // add_styles_and_foreground(tab.tabId)
    add_styles_and_foreground(tab.tabId)
})
function add_styles_and_foreground(tabId) {
    chrome.tabs.get(tabId, current_tab_info => {
        console.log(current_tab_info)
        if (allowed_url_regex.test(current_tab_info.url)) {
            chrome.tabs.insertCSS(null, { file: './styles.css' }, () => console.log('styles.css added'))
            chrome.tabs.executeScript(null, { file: './foreground.js' }, () => console.log('foreground.js executed'))
        }
    })
}

