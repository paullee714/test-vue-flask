import axios from 'axios';

const instance = axios.create({
    baseURL: 'http://localhost:5050',
});

function registerUser(userData) {
    return instance.post('signup', userData);
}

function loginUser(userData) {
    return instance.post('login', userData);
}

export { registerUser, loginUser };
