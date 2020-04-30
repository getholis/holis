import apiClient from '../../services/api'
console.log(apiClient)
const state = {
  list: []
}

const mutations = {
  setList(state, list) {
    state.list = list
  }
}

const actions = {
  async getList({ commit }) {
    const {data} = await apiClient.announcements.getList()
    console.log(data)
    commit('setList', data)
  }
}

export default {
  state,
  mutations,
  actions
}
