import React,{Component} from "react"
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
import {login} from '../../redux/actions'
import '../../common/css/index.less'

class Login extends Component{
    state = {
        username:'',
        password:''
    }

    handleChange = (name,value) => {
        this.setState({[name]:value})
    }

    tologin = () => {
        this.props.history.replace('/register')
    }

    login = () => {
        this.props.login(this.state)
    }

    render(){
        const {redirectTo,msg} = this.props
        if (redirectTo) {
            return <redirectTo to={redirectTo}/>}
        return(
            <div>
                <NavBar>扫码挪车</NavBar>
                <Logo/>
                <WingBlank>
                    {msg ? <p className='error-msg'>{msg}</p> : null}
                    <List>
                        <InputItem placeholder="输入用户名" onChange={val => this.handleChange("username",val)}>用户名:</InputItem>
                        <WhiteSpace/>
                        <InputItem placeholder="输入密码" onChange={val => this.handleChange("password",val)}>密&nbsp;码:</InputItem>
                        <WhiteSpace/>
                        <WhiteSpace/>
                        <Button type='primary' onClick={this.login}>登&nbsp;&nbsp;&nbsp;录</Button>
                        <WhiteSpace/>
                        <WhiteSpace/>
                        <Button type='primary' onClick={this.tologin}>注&nbsp;&nbsp;&nbsp;册</Button>
                    </List>
                </WingBlank>
            </div>
        )
    }
}

export default connect(
    state => state.user,
    {login}
)(Login)