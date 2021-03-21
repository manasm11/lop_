$(function(){
  $("#search").click(function(){
    paper = getPaperData()
    chrome.tabs.query({active:true, currentWindow: true}, function(tabs){
      chrome.tabs.sendMessage(tabs[0].id, {todo: "search", paper})
    })
  })
})

function getPaperData(){
  authors = parseCSV($("#author").val())
  keywords = parseCSV($("#keywords").val())
  return {
    authors,
    // authors: authors,
    title: $("#title").val(),
    keywords,
    // keywords: keywords,
    conference: $("#conference").val(),
    year_start: $("#year_start").val(),
    year_end: $("#year_end").val(),
  }
}

function parseCSV(csv_string) {
  array = csv_string.split(',')
  array = array.map(item => item.trim())
  return array
}