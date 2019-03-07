import {
    AUTH_SUCCESS,
    ERROR_MSG
} from './action-types'
import {reqRegister} from '../api/index'
import {reqLogin} from '../api/index'
// 同步错误消息
const errorMsg = (msg) => ({type:ERROR_MSG, data: msg})
// 同步成功响应
const authSuccess = (user) => ({type: AUTH_SUCCESS, data: user})
/*异步注册
 */
export function register({username, password, confirm_password}) {
// 进行前台表单验证, 如果不合法返回一个同步 action 对象, 显示提示信息
    if (!username || !password) {
        return errorMsg('用户名密码必须输入')
    }
    if (password !== confirm_password) {
        return errorMsg('密码和确认密码不同')
    }
    return async dispatch => {
// 异步 ajax 请求, 得到响应
        const response = await reqRegister({username, password,confirm_password})
// 得到响应体数据
        const result = response.data
        console.log(result.data)
// 如果是正确的
        if (result.code === 0) {
// 分发成功的 action
            dispatch(authSuccess(result.data))
        } else {
// 分发提示错误的 action
            dispatch(errorMsg(result.msg))
        }
    }
}


export const login = ({username, password}) => {
    if (!username || !password) {
        return errorMsg('用户密码必须输入')
    }
    return async dispatch => {
        const response = await reqLogin({username, password})
        const result = response.data
        if (result.code === 0) {
            dispatch(authSuccess(result.data))
        } else {
            dispatch(errorMsg(result.msg))
        }
    }
}