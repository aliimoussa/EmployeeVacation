/* datatables global function to load data from server */
function create_datatable(table_id, url, columns){
    $('#'+table_id).DataTable({
    "processing": true,
    "dataSrc": "data",
    "ajax": {
    "url": url,
    "dataType": "json",
    },
    "columns": columns
    });
    }
    
     {% if request.user.is_superuser %}
    /********************************* for admin */
    create_datatable('vacation_table', "/api/vacation-list/?format=json", [
    {"data": "owner"},
    {"data": "type_vacation"},
    {"data": "date_vacation",render:function(data){
        return moment(data).format("YYYY-MM-DD");
    
    }},
    {"data": "start_date",render:function(data){
        return moment(data).format("YYYY-MM-DD");}},
    {"data": "end_date",render:function(data){
        return moment(data).format("YYYY-MM-DD");}},
    {"data": "comments"},
    {"data":"status",render:function(data,type,full){
        var is_approved=(full.status=='Approved')
        var is_Pending=(full.status=='Pending')
        var is_denied=(full.status=='Denied')
        if (is_approved)
            return '<span class="btn btn btn-success far fa-thumbs-up fa-2x text-300" title="Approved" "></span>';
        else if (is_Pending)
            return '<span class="btn btn btn-primary far fa-hand-point-up text-300" title="Pending" "></span>';
        return '<span class="btn btn btn-danger far fa-thumbs-down  fa-2x text-300" title="Denied" "></span>';
    }},
    {"data" : "command",render: function(data, type, full) {
        var approve_link = "{%url 'approve-vacation' id=123456 %}".replace('123456', full.id);
        var deny_link = "{%url 'deny-vacation' id=123456 %}".replace('123456', full.id);
        
        var is_disabled = (full.status == 'Approved' || full.status == 'Denied');
    
        is_disabled ? approve_link = '#!' : '';
        is_disabled ? deny_link = '#!' : '';
    
        return '<a class="btn btn btn-'+(is_disabled ? 'secondary disabled' : 'danger')+' fa fa-thumbs-down"\
       title="Deny" href="' + deny_link + '"></a>&nbsp;'
             +'<a class="btn btn-'+(is_disabled ? 'secondary disabled' : 'success')+' fa fa-thumbs-up"\
             title="Approve" href="' + approve_link + '"></a>';
    }}
    
    
    ]);
    {%else%}
    /********************************* for employee edit here */ 
    create_datatable('vacation_table', "/api/vacation-user-api/?format=json", [
    {"data": "type_vacation"},
    {"data": "date_vacation",render:function(data){
        return moment(data).format("YYYY-MM-DD");}},
    {"data": "start_date",render:function(data){
        return moment(data).format("YYYY-MM-DD");}},
    {"data": "end_date",render:function(data){
        return moment(data).format("YYYY-MM-DD");}},
    {"data": "comments"},
    {"data" : "status",render:function(data,type,full){
        var is_approved=(full.status=='Approved')
        var is_Pending=(full.status=='Pending')
        var is_denied=(full.status=='Denied')
        if (is_approved)
            return '<span class="btn btn btn-success far fa-thumbs-up fa-2x text-300" title="Approved" "></span>';
        else if (is_Pending)
            return '<span class="btn btn btn-primary far fa-hand-point-up text-300" title="Pending" "></span>';
        return '<span class="btn btn btn-danger far fa-thumbs-down  fa-2x text-300" title="Denied" "></span>';
    }},
    {"data" : "command",render: function(data, type, full) {
    
    var todayDate =  '{% now "Y-m-d" %}'; // from tempalte
    var recordDate = new Date(full.end_date); // full.end_time
    recordDate = moment(recordDate).format("YYYY-MM-DD");
    var isOldDate = (!moment(recordDate).isAfter(todayDate) || (recordDate == todayDate));
    // console.log(todayDate);
    // console.log(recordDate);
    // console.log(isOldDate);
    var is_disabled = (full.status == 'Approved' || full.status == 'Denied');
    
    if(isOldDate || is_disabled ){
    return '';
    }
    else{
    var delete_link = "{%url 'delete-vacation' id=123456 %}".replace('123456', full.id);
    var edit_link = "{%url 'edit-vacation' id=123456 %}".replace('123456', full.id);
    return '<a title="Edit" class="btn btn-primary far fa-edit"  href="'+edit_link+'"></a>&nbsp;'
    +'<a   title="Delete" class="btn btn-danger far fa-trash-alt" href="'+delete_link+'"></a>';
    }
    
    
    }
    }
    ]);
    
    {% endif %}
    
    
    
    
    /* init event for select on change status send the new value to the server with the vacation id */
    $(document).on('change', '.vacation_status', function(event){
    event.stopPropagation();
    var vacation_id = $(this).data('id'); 
    var new_status = $(this).val(); 
    simple_post_request('/api/update-vacation/', {
    'vacation_id': vacation_id,
    'status': new_status,
    }, function(result){//on_update
    
    });
    });
    
    function simple_post_request(url, obj, callback){
    $.post(url, obj, function(res){
    callback(res);
    });
    }  