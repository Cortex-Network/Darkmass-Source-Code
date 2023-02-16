var toolbarOptions = [
    [{ 'header': [1, 2, 3, 4, 5, false] }],
    ['bold', 'italic'],        // toggled buttons

    [{ 'list': 'bullet' }]
];
var quill = new Quill('#editor', {
    modules: {
        toolbar: toolbarOptions
    },
    readOnly: false,
    theme: 'snow'
});