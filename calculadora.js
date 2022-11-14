const section_fr = document.querySelector("section-fr")
const input_cal = document.getElementById("input-cal")

const calculo = () =>{     

    const input_vel = +(document.getElementById("input-vel")).value 
    const input_cabal = +(document.getElementById("input-cabal")).value 
    const input_fren = +(document.getElementById("input-fren")).value 
  
  

    let calc = 0 - input_vel
    let tie = calc / input_fren
    let dist = 0 + input_vel * tie + 0.5 * input_fren * (tie * tie)
    let c = input_vel + (1 / 2) * (0 - input_vel) 
    let c2 = input_cabal / c
    let acel = (0 - input_vel) / c2
    let dist2 = input_cabal - dist

    if (dist > input_cabal){
        
        let resNAc ='El objeto 1 necesitaba frenar a' + acel +'m/s2 para no chocar y lo choco en' + tie + 'segundos'
        respuesta(resNAc)
        console.log(resNAc)
        
        

    } 
    else if (dist <= input_cabal) {
        
        let resNAc ='Lo choco en'+ tie +'segundos y necesitaba frenar a'+ dist2 + 'm/s2 para no chocar' 
        respuesta(resNAc)
        console.log(resNAc)
    }
    
}
const respuesta = (res) => {
    clearRespuesta();
    let contenedor_res = document.querySelector(".contenedor-res") 
    let respuestaDiv = document.createElement("div");
    respuestaDiv.innerHTML = `<h4>Respuesta</h4>
    <p>${res}</p>`;
contenedor_res.appendChild(respuestaDiv); 
}

const clearRespuesta = () =>{ 
    const respuesta = document.querySelector("#idRespuesta");
    while (respuesta.firstChild) {
        respuesta.removeChild(respuesta.firstChild);
    }
}

const show = (input) =>{ 
    input.style.display = "flex"
}

const dontShow = (input) =>{
    input.style.display = "none"
}

input_cal.addEventListener("click", (e) =>{ 
    e.preventDefault();
    calculo();
})