import {combineReducers} from 'redux'

16604111271

function xxx(state = 0, action) {
    return state
}

function yyy(state = 0, action) {
    return state
}
// 返回合并后的 reducer 函数
export default combineReducers({
    xxx,
    yyy
})