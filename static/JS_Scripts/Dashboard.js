const chart = document.querySelector("#chart").getContext('2d');
const chart1 = document.querySelector("#myChart").getContext('2d');
//create a new chart instance

var xValues = ["Music", "France", "Spain", "USA", "Argentina"];
var yValues = [55, 49, 44, 2, 15];
var barColors = [
  "#b91d47",
  "#00aba9",
  "#2b5797",
  "#e8c3b9",
  "#1e7145"
];

new Chart(chart1, {
  type: "pie",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    title: {
      display: true,
      text: "World Wide Wine Production 2018"
    }
  }
});

new Chart(chart,{
    type:'line',
    data:{
        labels:['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec1'],
        datasets: [
            {
                label:'Credit',
                data:[64,6,464,64,646,6,564,465,46,4,6,564],
                borderColor: 'red',
                borderWidth:2
            },
            {
                label:'Debit',
                data:[65,6,464,84,64,6,464,465,486,4,86,64],
                borderColor: 'blue',
                borderWidth:2
            },
        ]
    },
    options:{
        responsive:true
    }
})


//show or hide navbar

const menuBtn = document.querySelector('#menu-btn');
const closeBtn = document.querySelector('#close-btn');
const sidebar = document.querySelector('aside');

menuBtn.addEventListener('click',()=>{
    sidebar.style.display='block';
})

closeBtn.addEventListener('click',()=>{
    sidebar.style.display='none';
})

//change theme
const themeBtn= document.querySelector('.theme-btn');

themeBtn.addEventListener('click',()=>{
    document.body.classList.toggle('dark-theme');
    themeBtn.querySelector('span:first-child').classList.toggle('active');
    themeBtn.querySelector('span:last-child').classList.toggle('active');
})