import React from 'react'
import ReactDom from 'react-dom'
import {Button} from "antd-mobile"

import {Provider} from 'react-redux'
import store from './redux/store'
import {HashRouter,Switch,Route} from 'react-router-dom'
import Register from './containers/register/register'
import Login from "./containers/login/login"
import Main from "./containers/main/main"

ReactDom.render((
    <Provider store={store}>
    <HashRouter>
        <Switch>
            <Route path="/register" component={Register}/>
            <Route path="/login" component={Login}></Route>
            <Route component={Main}></Route>
        </Switch>
    </HashRouter>
    </Provider>
    ),
    document.getElementById("root")
)