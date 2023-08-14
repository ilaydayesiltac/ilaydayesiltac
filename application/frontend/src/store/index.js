import { createStore } from 'vuex';
import homeStore from './home-store';

export default createStore({
  state: {
    email: '',
    password: '',
  },
  getters: {
    email: (state) => state.email,
    password: (state) => state.password,
  },
  mutations: {
    email: (state, payload) => {
      state.email = payload;
    },

  },
  actions: {
    test({ commit }) {
      commit('email', 'test@gmail.com');
    },

  },
  modules: {
    homeStore,
  },
});
