/* Adds LI element to a list when DIV#add_item clicked */
$('#add_item').click(() => {
  $('ul.my_list').append($('<li>Item</li>'));
});
