const titleInput = document.querySelector('input[name=series]');
const slugInput = document.querySelector('input[name=number]');

const slugify = (val) => {

    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')         // Replace & with 'and'
        .replace(/[\s\W-]+/g, '-')      // Replace spaces, non-word characters and dashes with a single dash (-)

};

titleInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(titleInput.value));
});

 $(function () {
    $("#id_expiration_date").datepicker({
      format: 'yyyy-mm-dd',
    });
  });

   $(function () {
    $("#id_date_of_use").datepicker({
      format: 'yyyy-mm-dd',
    });
  });
