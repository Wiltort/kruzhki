
class Api {
    constructor(apiUrl) {
        this.apiUrl =  apiUrl;
    }
  getPurchases () {
    return fetch(`/purchases`, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then( e => {
          if(e.ok) {
              return e.json()
          }
          return Promise.reject(e.statusText)
      })
  }
  addPurchases (id) {
    return fetch(`/purchases`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        id: id
      })
    })
      .then( e => {
          if(e.ok) {
              return e.json()
          }
          return Promise.reject(e.statusText)
      })
  }
  removePurchases (id){
    return fetch(`/purchases/${id}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then( e => {
          if(e.ok) {
              return e.json()
          }
          return Promise.reject(e.statusText)
      })
  }
  addSubscriptions(id) {
    return fetch(`/subscriptions`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        id: id
      })
    })
      .then( e => {
          if(e.ok) {
              return e.json()
          }
          return Promise.reject(e.statusText)
      })
  }
  removeSubscriptions (id) {
    return fetch(`/subscriptions/${id}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then( e => {
          if(e.ok) {
              return e.json()
          }
          return Promise.reject(e.statusText)
      })
  }
  addFavorites (id)  {
    return fetch(`/favorites`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        id: id
      })
    })
        .then( e => {
            if(e.ok) {
                return e.json()
            }
            return Promise.reject(e.statusText)
        })
  }
  removeFavorites (id) {
    return fetch(`/favorites/${id}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      }
    })
        .then( e => {
            if(e.ok) {
                return e.json()
            }
            return Promise.reject(e.statusText)
        })
  }
    getIngredients  (text)  {
        return fetch(`/ingredients?query=${text}`, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then( e => {
                if(e.ok) {
                    return e.json()
                }
                return Promise.reject(e.statusText)
            })
    }
}


Для решения этой задачи, необходимо модифицировать предыдущий скрипт, добавив в него функционал для вывода элементов выбранных рубрик и обработчик выбора рубрик.

При выборе рубрики, будем отправлять запрос к API с id выбранной рубрики. В ответ на этот запрос, мы получим список элементов, относящихся к этой рубрике. Затем выведем эти элементы на страницу.

const API_ENDPOINT_CATEGORIES = ‘https://example.com/api/v1/categories’;
const API_ENDPOINT_ITEMS = ‘https://example.com/api/v1/items’;

// Функция для получения списка категорий
function getCategories() {
fetch(API_ENDPOINT_CATEGORIES)
.then(response => response.json())
.then(({ data }) => {
data.forEach(category => {
const checkbox = document.createElement(‘input’);
checkbox.type = ‘checkbox’;
checkbox.value = category.id;
document.getElementById(‘checkboxes’).appendChild(checkbox);

            // Добавляем обработчик изменения состояния чекбокса
            checkbox.addEventListener('change', handleCheckboxChange);
        });
    })
    .
Продолжи   
catch(err => console.log(err));
}

// Обработчик выбора рубрики
function handleCheckboxChange() {
const checkboxValues = […document.querySelectorAll(‘input[type=“checkbox”]:checked’)]
.map(checkbox => checkbox.value);

if (checkboxValues.length) {
    // Отправляем запрос к API для получения элементов выбранной рубрики
    fetch(`https://example.com/api/v1/items?category=${checkboxValues[0]}`)
        .then(response => response.json())
        .then((data) => {
            console.log(data);
            // Выводим элементы выбранной рубрики на страницу
            data.forEach((item) => {
                const element = document.createElement('div');
                element.innerHTML = item.name;
                document.getElementById('items').appendChild(element);
            });
        })
        .catch(err => console.log(err));
} else {
    // Если ни одна рубрика не выбрана, удаляем все элементы с экрана
    while (document.getElementById('items')) {
        document.getElementById('items').
Продолжи   
remove();
}
}
}

getCategories();
