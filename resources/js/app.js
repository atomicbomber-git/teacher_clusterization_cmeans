import 'bootstrap'
import Vue from 'vue'
import Cookies from 'js-cookie'

window.$ = require('jquery')

// Axios setup
window.axios = require('axios');
window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

let token = Cookies.get('csrftoken')
if (token) {
    window.axios.defaults.headers.common['X-CSRFToken'] = token;
}
else {
    console.log("CSRF token not found.")
}

// Vue setup
import DosenIndex from './components/DosenIndex.vue'

const app = new Vue({
    el: '#dosen-index',
    render: h => h(DosenIndex)
})




