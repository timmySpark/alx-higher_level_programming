// Adds a <li> element to a list when a user clicks on DIV#add_item tag

$('div#add_item').click(function () {
  const element = '<li>Item</li>';
  $('ul.my_list').append(element);
});
