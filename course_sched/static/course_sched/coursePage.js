function toggleAddCourseForm() {
    $('#alertMessage').hide()
    $('#newCourse').toggle()
    $('#editCourse').hide()
}

function editCourse(id, name, crn, units, needs_computer, has_lab, lab_needs_computer) {
    $('#newCourse').hide()
    $('#alertMessage').hide()
    if (document.getElementById('idToEdit').innerHTML == id) {
        $('#editCourse').toggle()
    } else {
        $('#editCourse').show()
    }
    document.getElementById('editName').value = name
    document.getElementById('editCrn').value = crn
    document.getElementById('editUnits').value = units
    document.getElementById("edit_needs_computer").checked = needs_computer == 'True'
    document.getElementById("edit_has_lab").checked = has_lab == 'True'
    document.getElementById("edit_lab_needs_computer").checked = lab_needs_computer == 'True'
    $('#idToEdit').html(id)
}

$(document).ready(function () {
    $('#addForm').submit(function (event) {
        $.ajax({
            type: 'POST',
            url: '/course_sched/course_manager/add/',
            csrfmiddlewaretoken: '{{ csrf_token }}',
            data: $('#addForm').serialize(),
            dataType: 'json',
            success: function (data) {
                if (data.isCrnTaken) {
                    $('#alertMessage').html('A course with this crn already exists!')
                } else {
                    $('#alertMessage').html('Successfully added course!')
                    document.getElementById("addForm").reset()
                }
                $('#alertMessage').show()
                $('#courseTable').load(document.URL + ' #courseTable')
                $('#newCourse').hide()
            },
        });
        return false;
    });

    $('#editForm').submit(function (event) {
        $.ajax({
            type: 'POST',
            url: '/course_sched/course_manager/edit/',
            csrfmiddlewaretoken: '{{ csrf_token }}',
            data: $('#editForm').serialize() + '&id=' + document.getElementById('idToEdit').innerHTML,
            dataType: 'json',
            success: function (data) {
                if (data.isCrnTaken) {
                    $('#alertMessage').html('A course with this crn already exists!')
                } else {
                    $('#alertMessage').html('Successfully edited course!')
                    document.getElementById("editForm").reset();
                }
                $('#alertMessage').show()
                $('#courseTable').load(document.URL + ' #courseTable')
                $('#newCourse').hide()
                $('#editCourse').hide()
            },
        });
        return false;
    });
});

$(document).on("click", ".deleteForm", function (event) {
    $.ajax({
        type: 'POST',
        url: '/course_sched/course_manager/delete/',
        csrfmiddlewaretoken: '{{ csrf_token }}',
        data: 'id=' + document.getElementById('idToEdit').innerHTML,
        dataType: 'json',
        success: function (data) {
            if (data.courseExists) {
                $('#alertMessage').html('Course sucessfully deleted!')
                document.getElementById("editForm").reset();
            } else {
                $('#alertMessage').html('Error: Could not delete course!')
            }
            $('#alertMessage').show()
            $('#courseTable').load(document.URL + ' #courseTable')
            $('#newCourse').hide()
            $('#editCourse').hide()
        },
    });
    return false;
});