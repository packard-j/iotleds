(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{136:function(e,t,n){e.exports=n(342)},141:function(e,t,n){},170:function(e,t){},173:function(e,t,n){},340:function(e,t,n){},341:function(e,t,n){},342:function(e,t,n){"use strict";n.r(t);var a=n(0),c=n.n(a),r=n(131),o=n.n(r),l=(n(141),n(30)),i=n(21),s=n(26),u=n(132),m=n(346),b=n(133),h=n.n(b),p=n(345),d=(n(173),function(e){var t=e.label,n=e.isOn,a=e.handleToggle;return c.a.createElement(c.a.Fragment,null,c.a.createElement("input",{checked:n,onChange:a,className:"react-switch-checkbox",id:"react-switch-new",type:"checkbox"}),c.a.createElement("label",{style:{background:n&&"#06D6A0"},className:"react-switch-label",htmlFor:"react-switch-new"},c.a.createElement("label",{className:"checkbox-label",htmlFor:"react-switch-checkbox"},t),c.a.createElement("span",{className:"react-switch-button"})))}),f=n(36);n(78);function g(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}var E=new m.a,v=h()(),O=function(e,t){v.emit("color",function(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?g(n,!0).forEach((function(t){Object(u.a)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):g(n).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}({},e,{cascade:t}))};var w=function(){var e=Object(a.useState)(!1),t=Object(s.a)(e,2),n=t[0],r=t[1];return Object(a.useEffect)((function(){var e=E.pipe(Object(p.a)(50)).subscribe((function(e){return O(e,n)}));return function(){return e.unsubscribe()}}),[n]),c.a.createElement("div",{className:"centered-container"},c.a.createElement("div",{className:"settings"},c.a.createElement("button",{className:"btn btn-rainbow",onClick:function(){fetch("/rainbow",{method:"GET"}).then((function(e){return console.log(e)}))}},"Rainbow"),c.a.createElement(d,{label:"Cascade",isOn:n,handleToggle:function(){return r(!n)}})),c.a.createElement(f.SketchPicker,{onChange:function(e){return E.next(e.rgb)}}),c.a.createElement(l.b,{className:"link-btn",to:"/pattern"},c.a.createElement("button",{className:"btn btn-nav"},"Pattern")))},k=(n(340),function(e){return"rgba(".concat(e.r,",").concat(e.g,",").concat(e.b,",1)")});var j=function(e){var t=e.min,n=e.max,a=e.step,r=e.onChange,o=e.value,l=150,i=150,s=150,u=6,m=214,b=160,h=n-t,p=k({r:l+(o-t)*Math.round((u-l)/h),g:i+(o-t)*Math.round((m-i)/h),b:s+(o-t)*Math.round((b-s)/h)});return c.a.createElement("div",{className:"slider"},c.a.createElement("input",{type:"range",style:{backgroundColor:p},value:o,onChange:function(e){return r(e.target.value)},min:t,max:n,step:a}))},y=(n(341),function(e){return"rgba(".concat(e.r,",").concat(e.g,",").concat(e.b,",1)")}),N=function(){var e=Object(a.useState)({r:36,g:240,b:232}),t=Object(s.a)(e,2),n=t[0],r=t[1],o=Object(a.useState)({r:218,g:8,b:191}),i=Object(s.a)(o,2),u=i[0],m=i[1],b=Object(a.useState)(5),h=Object(s.a)(b,2),p=h[0],d=h[1],g=Object(a.useState)(2),E=Object(s.a)(g,2),v=E[0],O=E[1];return c.a.createElement("div",{className:"pattern-container"},c.a.createElement("div",{className:"grid"},c.a.createElement("div",{className:"picker-container"},c.a.createElement("p",null,"First Color"),c.a.createElement(f.ChromePicker,{color:n,onChange:function(e){return r(e.rgb)},disableAlpha:!0})),c.a.createElement("div",{className:"picker-container"},c.a.createElement("p",null,"Second Color"),c.a.createElement(f.ChromePicker,{color:u,onChange:function(e){return m(e.rgb)},disableAlpha:!0})),c.a.createElement("div",null,c.a.createElement("p",null,"Repetitions ",p),c.a.createElement(j,{value:p,min:1,max:25,step:1,onChange:d})),c.a.createElement("div",null,c.a.createElement("p",null,"Speed: ",v),c.a.createElement(j,{value:v,min:1,max:10,step:1,onChange:O}))),c.a.createElement("div",{className:"actions"},c.a.createElement("button",{className:"btn btn-nav btn-gradient",style:{background:"linear-gradient(to right, ".concat(y(n),",").concat(y(u),")")},onClick:function(){fetch("/pattern",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({c1:n,c2:u,n:p,speed:v})}).then((function(e){return console.log(e)}))}},"Go!"),c.a.createElement(l.b,{to:"/",className:"link-btn"},c.a.createElement("button",{className:"btn btn-nav"},"Back"))))};var C=function(){return c.a.createElement(l.a,null,c.a.createElement("div",{className:"container"},c.a.createElement(i.c,null,c.a.createElement(i.a,{exact:!0,path:"/"},c.a.createElement(w,null)),c.a.createElement(i.a,{path:"/pattern"},c.a.createElement(N,null)))))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));o.a.render(c.a.createElement(C,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))},78:function(e,t,n){}},[[136,1,2]]]);
//# sourceMappingURL=main.ab5e5052.chunk.js.map