import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Loader from 'react-loader-spinner'


class App extends Component {
  state = {
    image: null,
    image1: null,
    image2: null,
    image3: null,
    image4: null,
    image5: null,
    received: false,
    value: "",
    loading: false,
    data: null
  }

 handleChange = (event) => {
    console.log(event.target.value);
    this.setState({value: event.target.value})
  }

  sendImage = () => {
    const baseUrl ='http://localhost:8001';
		// const headers = new Headers();
    // headers.append('Content-Type', 'application/json');
    this.setState({
      loading: true,
      received: false
    })
		fetch(baseUrl + '/image', {
				method: 'POST',
				// headers,
				body: JSON.stringify({
					img: this.state.value,
				})
		}).then((response) => {
			response.json().then(json => {
        console.log((json))
        if(json === null){
          console.log("É null")
        }
        this.setState({
          data: json,
          received: true,
          loading: false
        })
        // this.setState({loading: false})

      })
		})
    console.log("sent")
  }

 

  render() {
    const styleLoading = {Border: "16px solid #f3f3f3"}
      return (
        <div className="App">
            <h2>Image Search Engine</h2>
            <br></br>
            <input
              type='text'
              onChange={ this.handleChange }
              value={this.state.value}
            >
             
             </input>
            <br></br>          
            <button onClick={this.sendImage}>Search</button>
            <br></br>
            <div className="container">
            <br></br>
            {this.state.loading?<Loader 
              type="Watch"
              color="#00BFFF"
              height="100"	
              width="100"
            /> : null}
            {this.state.received ? 
            <div>
              {this.state.data.map(obj => {
                // console.log(obj)
                return (<img src={"data:image/jpg;base64, " + obj.slice(2, obj.length -1)}/>)
              })}
            </div>
            : null}
            </div>
            {/* <img src={"data:image/jpg;base64, " + this.state.image1.slice(1, image1.length)} width="100%" height="100%"/> */}
        </div>
  
      );
  }
}

export default App;
