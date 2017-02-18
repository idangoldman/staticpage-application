// var api = (function API() {
//     var instance = null;
//
//     return function() {
//         if ( ! instance ) {
//             instance = init();
//         }
//         return instance;
//     };
//
//     function init() {
//         return {
//             element: function( selector, parameters ) {
//                 console.log( selector, parameters );
//             }
//         };
//     }
// })();

function api() {
    this.blah = 'foo';

    return this;
}

console.log(api());


element('.title').then(( view, model, component, style ) => {
    this.on('click', component.edit);
    this.element('.sub').then(() =>{

    });
    return render_template( view, model );
});

element('.title').update({ 'model': jsonPath, 'style': 'body { color: black; }' });
element('.title .sub').remove([ 'style' ])
element('.title').on()
element('.title').off()
element('.title').trigger()


// api.create('count-down:id', { 'id': 'foobar' });
// api.create('.count-down', { 'id': 'foobar' });

// api.element('.count-down').then( model, view => {
//     this.view = view || 'templates/count-down'; // support html, jinja
//     this.model = model || 'stubs/count-down'; // support json
//
//     return render_template( this.view, this.model );
// });
//
// api.put('count-down/datetime/', { 'timestamp': 14222 }).then( timestamp => {
//
//     this.view;
//     this.model;
//     this.style;
// }).catch(( message ) => {
//     console.log( message );
//
//     api.get('count-down', {
//         model: 'stubs/something',
//         view: 'template/other'
//     });
// });
//
// api.remove('count-down');
