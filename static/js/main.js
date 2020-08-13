// $(document).ready(function(){
//     var myArray = [
//     ]
//   function buildtable(data){
//     var table = document.getElementById("mytable")
//     for(var i = 0; i < data.length; i++){
//       var row =`<tr>
//                             <td>${i+1}</td>
//                             <td>${data[i].name}</td>
//                             <td>${"attend"}</td>
              
//                       </tr>`
  
//       table.innerHTML += row
//     }
//   }
//   $.ajax({
//     url:'{% url "attendance"%}',
//     type:'GET',
//     data:{'data':data },
//     dataType: 'json',
//     success:function(response){
//       alert("Got data!");
//       myResponse = JSON.parse(response)
//       myArray = myResponse.data
//       console.log(myArray)
//     }
  
//   });
//   });