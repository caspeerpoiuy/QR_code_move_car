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
import Logo from '../../components/logo/logo'
export default class Login extends Component{
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

    render(){
        return(
            <div>
                <NavBar>扫码挪车</NavBar>
                <Logo/>
                <WingBlank>
                    <List>
                        <InputItem placeholder="输入用户名" onChange={val => this.handleChange("username",val)}>用户名:</InputItem>
                        <WhiteSpace/>
                        <InputItem placeholder="输入密码">密&nbsp;码:</InputItem>
                        <WhiteSpace/>
                        <WhiteSpace/>
                        <Button type='primary' onClick={this.register}>登&nbsp;&nbsp;&nbsp;录</Button>
                        <WhiteSpace/>
                        <WhiteSpace/>
                        <Button type='primary' onClick={this.tologin}>注&nbsp;&nbsp;&nbsp;册</Button>
                    </List>
                </WingBlank>
            </div>
        )
    }
}