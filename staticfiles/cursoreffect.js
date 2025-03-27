var main=document.querySelector(".dabba ");
var cursor = document.querySelector("#cursor");

main.addEventListener("mousemove",function(dets){
   gsap.to(cursor,{
    opacity:1,
    x:dets.x,
    y:dets.y,
    duration:1,
    ease:"back.out"
   })
})
main.addEventListener("mouseleave",function(dets){
    gsap.to(cursor,{
        opacity:0
    })
})
    