import React from 'react';

class CreateManufacturerForm extends React.Component {
    
    state = {
        name: ''
    };

    handleSubmitChange = async (event) => {
        event.preventDefault();
        const data = {...this.state};
    
        const locationUrl = 'http://localhost:8100/api/manufacturers/';
        const fetchConfig = {
          method: "POST",
          body: JSON.stringify(data),
          headers: {
              'Content-Type': 'application/json',
          },
        };
        const response = await fetch(locationUrl, fetchConfig);
        if (response.ok) {
          const newLocation = await response.json();
        
          const cleared = {
            name: ''
          };
          this.setState(cleared);
        }    
    }

    handleNameChange = (event) => {
        const value = event.target.value;
        this.setState({name: value})
    }

    render() {
        return (
            <div className="row">
            <div className="offset-3 col-6">
              <div className="shadow p-4 mt-4">
                <h1>Create A Manufacturer</h1>
                <form onSubmit={this.handleSubmitChange} id="create-manufacturer-form">
                  <div className="form-floating mb-3">
                    <input onChange={this.handleNameChange} value={this.state.name} placeholder="Name" required type="text" name="name" id="name" className="form-control" />
                    <label htmlFor="name">Name</label>
                  </div>
                  <button className="btn btn-primary">Create</button>
                </form>
              </div>
            </div>
          </div>
        );
    }
}
export default CreateManufacturerForm