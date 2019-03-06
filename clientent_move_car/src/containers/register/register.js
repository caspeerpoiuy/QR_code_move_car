import React, {Component} from 'react'
import {
    NavBar,
    WingBlank,
    List,
    InputItem,
    WhiteSpace,
    Radio,
    Button
} from 'antd-mobile'

import {connect} from 'react-redux'
import {Redirect} from 'react-router-dom'
import Logo from '../../components/logo/logo'
import {register} from '../../redux/actions'
import '../../common/css/index.less'

class Register extends Component{
    state = {
        username: '',
        password: '',
        password2: '',
    }

    handleChange = (name, value) => {
        this.setState({[name]: value})
    }

    toLogin = () => {
        this.props.history.replace('/login')
    }

    register = () => {
        this.props.register(this.state)
    }
    render(){
        const {redirecto,msg} = this.state
        if (redirecto){
            return <redirecto to={redirecto} />
        }
        return(
            <div>
                <NavBar>扫码挪车</NavBar>
                <Logo/>
                <WingBlank>
                    {msg ? <p className='error-msg'>{msg}</p> : null}
                    <List>
                        <InputItem placeholder='输入用户名' onChange={val => this.handleChange('username', val)}>用户名:</InputItem>
                        <WhiteSpace/>
                        <InputItem type='password' placeholder='输入密码' onChange={val => this.handleChange('password', val)}>密&nbsp;&nbsp;&nbsp;码:</InputItem>
                        <WhiteSpace/>
                        <InputItem type='password' placeholder='输入确认密码' onChange={val => this.handleChange('password2', val)}>确认密码:</InputItem>
                        <WhiteSpace/>
                        <WhiteSpace/>
                        <Button type='primary' onClick={this.register}>注&nbsp;&nbsp;&nbsp;册</Button>
                        <WhiteSpace/>
                        <Button onClick={this.toLogin}>已经有账号</Button>
                    </List>
                </WingBlank>
            </div>
        )
    }
}

export default connect(
    state => state.user,
    {register}
)(Register)