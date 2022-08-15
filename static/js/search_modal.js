$('#Bing').on('click',function(e){
	e.preventDefault();
	$('#Bing_modal').on('shown.bs.modal',function() {
		$(this).find('iframe').attr('src','https://www.bing.com/search?q='+$('#target').val())
	})
	$('#Bing_modal').modal({show:true})
	$('iframe').load(function() {
		$('.loading').hide();
	});
});