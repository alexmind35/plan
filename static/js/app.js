/* Слайдер */

let tabs = document.querySelector('.section__slider');
let btns = tabs.querySelectorAll('.slider__dots-item');
let items = tabs.querySelectorAll('.slider__list-item');

function change(arr, i) {
	arr.forEach(item => {
		item.forEach(i => {
			i.classList.remove('active')
		})
		item[i].classList.add('active')
	})
}

for (let i = 0; i < btns.length; i++) {
	btns[i].addEventListener('click', () => {
		change([btns, items], i)
	})
}

/* Прокрутка по нажатию кнопки Заказать */

/* function scrollTo(element) {

	window.scroll({
		left: 0,
		top: element.offsetTop,
		behavior: 'smooth'
	})
	
}

let orderBtn = document.querySelector('.btn__link-order');
let orderId = document.querySelector('#order');

orderBtn.addEventListener('click', () => {
	scrollTo(orderId);
}) */

/* Конец Прокрутка по нажатию кнопки Заказать */


/* Еще один способ Прокрутка по нажатию кнопки Заказать */

let hiddenElement = document.getElementById("order");
let btn = document.querySelector('.btn__link-order');

function handleButtonClick() {
	hiddenElement.scrollIntoView({
		block: "end",
		behavior: "smooth"
	});
}

btn.addEventListener('click', handleButtonClick);