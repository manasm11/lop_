chrome.runtime.sendMessage({todo: "showPageAction"})

chrome.runtime.onMessage.addListener(function(req, sender, senderRequest){
  if(req.todo == "search"){
    if (!is_logged_in()){
      alert("Please login for search")
      return
    }
    searchPaper(req.paper)
  }
})

function is_logged_in(){
  return !($("h3").text() == "Connect to Neo4j")
}

function searchPaper(paper){
  query = generateQuery(paper)
  typeQuery(query)
}

function generateQuery(paper){
  console.log(paper)
  return "match (n) return n"
}
function typeQuery(query){
  $("pre.CodeMirror-line[role='presentation']").click()
  for(let i=0;i<query.length; i++){
    var e = jQuery.Event("keypress");
    console.log(e)
    e.which = KEY_CODES[query[i]];
    console.log(e)
    $("pre.CodeMirror-line[role='presentation']").trigger(e)
  }
}

KEY_CODES = {
  a   :"65",
  b   :"66",
  c   :"67",
  d   :"68",
  e   :"69",
  f   :"70",
  g   :"71",
  h   :"72",
  i   :"73",
  j   :"74",
  k   :"75",
  l   :"76",
  m   :"77",
  n   :"78",
  o   :"79",
  p   :"80",
  q   :"81",
  r   :"82",
  s   :"83",
  t   :"84",
  u   :"85",
  v   :"86",
  w   :"87",
  x   :"88",
  y   :"89",
  z   :"90",
}