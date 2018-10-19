import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  state = {
    image: null,
    image1: null,
    image2: null,
    image3: null,
    image4: null,
    image5: null,
    received: false
  }

 handleChange = (event) => {
    console.log(event);
    if (event.target.files && event.target.files[0]) {
      let reader = new FileReader();
      reader.onload = (e) => {
          this.setState({image: e.target.result});
      };
      reader.readAsDataURL(event.target.files[0]);
    }
  }

  sendImage = () => {
    const baseUrl ='http://localhost:8001';
		// const headers = new Headers();
		// headers.append('Content-Type', 'application/json');
		fetch(baseUrl + '/image', {
				method: 'POST',
				// headers,
				body: JSON.stringify({
					img: this.state.image,
				})
		}).then((response) => {
			response.json().then(json => {
        console.log((json))
        this.setState({
          image1: json["0"].slice(2, json["0"].length -1),
          image2: json["1"].slice(2, json["1"].length -1),
          image3: json["2"].slice(2, json["2"].length -1),
          image4: json["3"].slice(2, json["3"].length -1),
          image5: json["4"].slice(2, json["4"].length -1),
          received: true
        })

      })
		})
    console.log("sent")
  }

  render() {
    return (
      <div className="App">
          <h2>Image Search Engine</h2>
          <br></br>
          <input 
            type={"file"} 
            onChange={ (e) => this.handleChange(e) }
          >
          </input>

          {/* <img src={this.state.image}/> */}
          <button onClick={this.sendImage}>Search</button>
          <br></br>
          <div className="container">
          {this.state.received ? 
          <div>
          <img src={"data:image/jpg;base64, " + this.state.image1}/>
          <img src={"data:image/jpg;base64, " + this.state.image2} />
          <img src={"data:image/jpg;base64, " + this.state.image3}/>
          <img src={"data:image/jpg;base64, " + this.state.image4} />
          <img src={"data:image/jpg;base64, " + this.state.image5} />
          </div>
          : null}
          </div>
          {/* <img src={"data:image/jpg;base64, " + this.state.image1.slice(1, image1.length)} width="100%" height="100%"/> */}
      </div>

    );
  }
}

export default App;
