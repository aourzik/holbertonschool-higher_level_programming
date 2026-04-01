#!/bin/usr/node
const list = document.querySelector('.my_list');
const newItem = document.createElement('#add_item');

newItem.addEventListener('click', function () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  list.appendChild(li);
});
