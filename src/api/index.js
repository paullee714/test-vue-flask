import axios from 'axios';

const instance = axios.create({
    baseURL: 'http://localhost:5000',
});

function registerUser(userData) {
    return instance.post('signup', userData);
}

export { registerUser };