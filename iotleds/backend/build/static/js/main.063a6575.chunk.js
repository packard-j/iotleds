(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{138:function(e,t,n){e.exports=n(344)},143:function(e,t,n){},310:function(e,t,n){},311:function(e,t,n){},312:function(e,t,n){},341:function(e,t){},344:function(e,t,n){"use strict";n.r(t);var a=n(0),c=n.n(a),r=n(132),l=n.n(r),o=(n(143),n(18)),i=n(22),s=n(346),u=n(345),m=n(347),b=n(25),E=(n(74),new s.a),d=new s.a;var h=function(e){var t=e.socket;return Object(a.useEffect)((function(){var e=E.pipe(Object(u.a)(50)).subscribe((function(e){return t.emit("color",e)}));return function(){return e.unsubscribe()}}),[t]),Object(a.useEffect)((function(){var e=d.pipe(Object(m.a)(2e3,null,5)).subscribe((function(e){5===e.length&&fetch("/secret",{method:"GET"}).then((function(e){return console.log(e)}))}));return function(){return e.unsubscribe()}}),[]),c.a.createElement("div",{className:"centered-container"},c.a.createElement(b.SketchPicker,{onChange:function(e){return E.next(e.rgb)}}),c.a.createElement("div",{className:"btn-group"},c.a.createElement("div",null,c.a.createElement(o.b,{className:"link-btn",to:"/pattern"},c.a.createElement("button",{className:"btn btn-nav"},"Pattern"))),c.a.createElement("div",null,c.a.createElement("button",{className:"btn btn-rainbow",onClick:function(e){d.next(e),fetch("/rainbow",{method:"GET"}).then((function(e){return console.log(e)}))}},"Rainbow")),c.a.createElement("div",null,c.a.createElement(o.b,{className:"link-btn",to:"/cascade"},c.a.createElement("button",{className:"btn btn-nav"},"Cascade")))))},f=n(28),p=(n(310),function(e){return"rgba(".concat(e.r,",").concat(e.g,",").concat(e.b,",1)")});var g=function(e){var t=e.min,n=e.max,a=e.step,r=e.onChange,l=e.value,o=150,i=150,s=150,u=6,m=214,b=160,E=n-t,d=p({r:o+(l-t)*Math.round((u-o)/E),g:i+(l-t)*Math.round((m-i)/E),b:s+(l-t)*Math.round((b-s)/E)});return c.a.createElement("div",{className:"slider"},c.a.createElement("input",{type:"range",style:{backgroundColor:d},value:l,onChange:function(e){return r(e.target.value)},min:t,max:n,step:a}))},v=(n(311),function(e){return"rgba(".concat(e.r,",").concat(e.g,",").concat(e.b,",1)")}),k=function(){var e=Object(a.useState)({r:36,g:240,b:232}),t=Object(f.a)(e,2),n=t[0],r=t[1],l=Object(a.useState)({r:218,g:8,b:191}),i=Object(f.a)(l,2),s=i[0],u=i[1],m=Object(a.useState)(5),E=Object(f.a)(m,2),d=E[0],h=E[1],p=Object(a.useState)(2),k=Object(f.a)(p,2),N=k[0],w=k[1];return c.a.createElement("div",{className:"pattern-container"},c.a.createElement("div",{className:"grid"},c.a.createElement("div",{className:"picker-container"},c.a.createElement("p",null,"First Color"),c.a.createElement(b.ChromePicker,{color:n,onChange:function(e){return r(e.rgb)},disableAlpha:!0})),c.a.createElement("div",{className:"picker-container"},c.a.createElement("p",null,"Second Color"),c.a.createElement(b.ChromePicker,{color:s,onChange:function(e){return u(e.rgb)},disableAlpha:!0})),c.a.createElement("div",null,c.a.createElement("p",null,"Repetitions ",d),c.a.createElement(g,{value:d,min:1,max:25,step:1,onChange:h})),c.a.createElement("div",null,c.a.createElement("p",null,"Speed: ",N),c.a.createElement(g,{value:N,min:1,max:10,step:1,onChange:w}))),c.a.createElement("div",{className:"actions"},c.a.createElement("button",{className:"btn btn-nav btn-gradient",style:{background:"linear-gradient(to right, ".concat(v(n),",").concat(v(s),")")},onClick:function(){fetch("/pattern",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({c1:n,c2:s,n:d,speed:N})}).then((function(e){return console.log(e)}))}},"Go!"),c.a.createElement("div",{className:"btn-group"},c.a.createElement("div",null,c.a.createElement(o.b,{to:"/",className:"link-btn"},c.a.createElement("button",{className:"btn btn-nav"},"Back"))))))},N=(n(312),function(e){var t=e.label,n=e.isOn,a=e.handleToggle;return c.a.createElement(c.a.Fragment,null,c.a.createElement("input",{checked:n,onChange:a,className:"react-switch-checkbox",id:"react-switch-new",type:"checkbox"}),c.a.createElement("label",{style:{background:n&&"#06D6A0"},className:"react-switch-label",htmlFor:"react-switch-new"},c.a.createElement("label",{className:"checkbox-label",htmlFor:"react-switch-checkbox"},t),c.a.createElement("span",{className:"react-switch-button"})))}),w=new s.a;var O=function(e){var t=e.socket,n=Object(a.useState)(!1),r=Object(f.a)(n,2),l=r[0],i=r[1];return Object(a.useEffect)((function(){var e=w.pipe(Object(u.a)(50)).subscribe((function(e){return t.emit("cascade",{color:e,loop:l})}));return function(){return e.unsubscribe()}}),[t,l]),c.a.createElement("div",{className:"centered-container"},c.a.createElement("div",{className:"settings"},c.a.createElement(N,{isOn:l,handleToggle:function(){t.emit("cascade",{loop:!l}),i((function(e){return!e}))}}),c.a.createElement("span",{className:"label"},"Loop")),c.a.createElement(b.SketchPicker,{onChange:function(e){return w.next(e.rgb)}}),c.a.createElement("div",{className:"btn-group"},c.a.createElement(o.b,{className:"link-btn wide",to:"/"},c.a.createElement("button",{className:"btn btn-nav"},"Back"))))},C=n(135),j=n.n(C)()();var x=function(){return c.a.createElement(o.a,null,c.a.createElement("div",{className:"container"},c.a.createElement(i.c,null,c.a.createElement(i.a,{exact:!0,path:"/"},c.a.createElement(h,{socket:j})),c.a.createElement(i.a,{path:"/pattern"},c.a.createElement(k,null)),c.a.createElement(i.a,{path:"/cascade"},c.a.createElement(O,{socket:j})))))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));l.a.render(c.a.createElement(x,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))},74:function(e,t,n){}},[[138,1,2]]]);
//# sourceMappingURL=main.063a6575.chunk.js.map