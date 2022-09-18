//https://www.web-dev-qa-db-ja.com/ja/javascript/iframeをbootstrap-modalで読み込みます/1048168472/
$('#Bing').on('click',function(e){
	//これを入れないとモーダルを開いて別タブでも開いてしまう
	e.preventDefault();
	$('#Bing_modal').on('shown.bs.modal',function() {
		$(this).find('iframe').attr('src','https://www.bing.com/search?q='+$('#target').val())
	})
	$('#Bing_modal').modal({show:true})
	$('iframe').load(function() {
		$('.loading').hide();
	});
});