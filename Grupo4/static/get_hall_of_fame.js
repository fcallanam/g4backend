/*
    Script que faz um request à API REST, obtém os dados do top10 leaderboard e expõe no HTML
*/

fetch("http://127.0.0.1:8000/backend/halloffame/").then((data)=>{
    //console.log(data);
    return data.json();
}).then((top_users_array)=>{
    // console.log(top_users_array)
    // console.log(Object.keys(top_users_array))

    let data = "";
    let user_data = "";
    let t1 = "";
    let t2 = "";
    let t3 = "";


    Object.keys(top_users_array).map((place)=>{


        if(place == 1){
            t1 += `<div>${top_users_array[place].nome}</div>`;
        }else if(place == 2){
            t2 += `<div>${top_users_array[place].nome}</div>`;
        }else if(place == 3){
            t3 += `<div>${top_users_array[place].nome}</div>`;
        }

        if(place != 'user_place'){
            data += `<li>
            <h2>${top_users_array[place].nome} ${top_users_array[place].nr_respostas_corretas}</h2>
            </li>`
        }  
        else{
            user_data += `<p>#${top_users_array[place].place}</p>`
        }

    })

    document.getElementById("leaderboard").innerHTML = data;
    document.getElementById("rectangle-4").innerHTML = t3;
    document.getElementById("rectangle-5").innerHTML = t1;
    document.getElementById("rectangle-6").innerHTML = t2;
    document.getElementById("user_place").innerHTML = user_data;

}).catch((err)=>{
    console.log(err);
})