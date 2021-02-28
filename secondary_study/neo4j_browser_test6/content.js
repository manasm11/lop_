url = 'http://localhost:5000/';
chrome.runtime.sendMessage({ todo: 'showPageAction' });

$(function(){
  $("input[data-testid='password']").focus();
})

chrome.runtime.onMessage.addListener(function (req, sender, senderRequest) {
  if (req.todo == 'search') {
    if (!is_logged_in()) {
      alert('Please login for search');
      return;
    }
    searchPaper(req.paper);
  }
});

function is_logged_in() {
  return !($('h3').text() == 'Connect to Neo4j');
}

function searchPaper(paper) {
  query = generateQuery(paper);
  typeQuery(query);
}

function generateQuery(paper) {
  return 'match (n) return n';
}
function typeQuery(query) {
  // $("div[data-testid='editor-wrapper']").focus()
  $.get(url + 'execute/', {query: query}).fail(function(){
    alert("Failed !!!")
  })
}
