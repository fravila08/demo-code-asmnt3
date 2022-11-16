console.log("im connected")

const addItemToCart=(id)=>{
    axios.post(`/addItemToCart/${id}`).then((response)=>{
        console.log(response.data)
    })
} 