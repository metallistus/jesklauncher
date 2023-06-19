
const borderBottomElements = document.querySelectorAll('[style*="border-bottom: 1px solid rgb(20,20,20,.3)"]')
const borderRightElements = document.querySelectorAll('[style*="border-right: 1px solid rgb(20,20,20,.3)"]')
const borderLeftElements = document.querySelectorAll('[style*="border-left: 1px solid rgb(20,20,20,.3)"]')
const borderElements = document.querySelectorAll('[style*="border: 1px solid rgb(20,20,20,.3)"]')

// elements 
const inputElements = document.querySelectorAll('input')
const aElements = document.querySelectorAll('a')

// panel
const accountsElements = document.querySelectorAll('.accounts')


console.log(borderRightElements)

// event listener
document.getElementById('theme').addEventListener('click', () => {
   if (document.body.style.color == 'ghostwhite') {
      // ____________ white theme ______________

      document.body.style.color = '#202020'
      document.body.style.backgroundColor = 'ghostwhite'

      changeStyle('1px solid rgb(0,0,0,.3)',borderBottomElements, 'borderBottom')
      changeStyle('1px solid rgb(0,0,0,.3)',borderRightElements, 'borderRight')
      changeStyle('1px solid rgb(0,0,0,.3)',borderLeftElements, 'borderLeft')
      changeStyle('1px solid rgb(0,0,0,.3)',borderElements, 'border')

      changeStyle('#202020',inputElements, 'color')
      changeStyle('#202020',aElements, 'color')

      changeStyle('ghostwhite',accountsElements, 'backgroundColor')

   } else {
      // ____________ black theme ___________

      document.body.style.color = 'ghostwhite'
      document.body.style.backgroundColor = '#202020'

      changeStyle('1px solid rgb(248, 248, 255, .3)',borderBottomElements, 'borderBottom')
      changeStyle('1px solid rgb(248, 248, 255, .3)',borderRightElements, 'borderRight')
      changeStyle('1px solid rgb(248, 248, 255, .3)',borderLeftElements, 'borderLeft')
      changeStyle('1px solid rgb(248, 248, 255, .3)',borderElements, 'border')

      changeStyle('ghostwhite',inputElements, 'color')
      changeStyle('ghostwhite',aElements, 'color')

      changeStyle('#202020',accountsElements, 'backgroundColor')
   }
})

// Change style
function changeStyle(
   color = 'rgb(20,20,20,.3)', 
   elements = [],
   option = null
) {
   for (let element of elements) {
      if (option) {
         element.style[option] = color
      }
   }
}