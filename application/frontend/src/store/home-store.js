const state = {
  email: '', password: '',
};

const getters = {
  email: (state) => state.email, password: (state) => state.password,
};

const mutations = {
  email: (state, payload) => {
    state.email = payload;
  },

};

const actions = {
  test({ commit }) {
    commit('email', 'test@gmail.com');
  },
};

export default {
  state, getters, mutations, actions,
};
