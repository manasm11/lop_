$(function(){
  $("#search").click(function(){
    paper = getPaperData()
    $.get("http://localhost:5000", paper)
      .always(function(){
        alert("SUCCESS")
      })
  })
})

function getPaperData(){
  authors = parseCSV($("#author").val())
  keywords = parseCSV($("#keywords").val())
  return {
    authors: authors,
    title: $("#title").val(),
    keywords: keywords,
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
