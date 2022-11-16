console.log("im connected")
console.log("hello")
const addItemToCart=(id)=>{
    axios.post(`/addItemToCart/${id}`).then((response)=>{
        console.log(response.data)
    })
} 



