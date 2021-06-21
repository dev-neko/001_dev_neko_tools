// ------------------------------

function onButtonClick() {
	const ky = {name:		'Kyash',
							title:	'Kyash',
							desc:		document.forms.id_form1.Kyash_desc.value,
							color:	document.forms.id_form1.Kyash_color.value,
							}
	const pr = {name:		'pring',
							title:	'pring',
							desc:		document.forms.id_form1.pring_desc.value,
							color:	document.forms.id_form1.pring_color.value,
							}
	const aw = {name:		'Amazon_wish',
							title:	'Amazonほしい物リスト',
							desc:		document.forms.id_form1.Amazon_wish_desc.value,
							color:	document.forms.id_form1.Amazon_wish_color.value,
							}
	const ag = {name:		'Amazon_gift',
							title:	'Amazonギフト券',
							desc:		document.forms.id_form1.Amazon_gift_desc.value,
							color:	document.forms.id_form1.Amazon_gift_color.value,
							}
	const py = {name:		'PayPay',
							title:	'PayPay',
							desc:		document.forms.id_form1.PayPay_desc.value,
							color:	document.forms.id_form1.PayPay_color.value,
							}
	const rp = {name:		'rakutenpay',
							title:	'楽天ペイ',
							desc:		document.forms.id_form1.rakutenpay_desc.value,
							color:	document.forms.id_form1.rakutenpay_color.value,
							}
	document.getElementById("copyTarget").innerHTML = '<div class="support-parts">\n'+ tag`${ ky }` +"\n"+ tag`${ pr }` +"\n"+ tag`${ ag }` +"\n"+ tag`${ aw }` +"\n"+ tag`${ py }` +"\n"+ tag`${ rp }` +"\n</div>";
}

// ------------------------------

function tag(strings,way){
	return  html = `	<!-- モーダルに紐づくボタン ${ way.title } -->
	<button type="button" class="btn btn-${ way.color }" data-toggle="modal" data-target="#${ way.name }" title="${ way.title }">
		<span class="icon-text-color">
			<span class="d-flex align-items-center">
				<span class="kihuicon-${ way.name } fb-2x"></span>
			</span>
		</span>
	</button>
	<!-- モーダル本体 ${ way.title } -->
	<div class="modal fade" id="${ way.name }" tabindex="-1" role="dialog" aria-labelledby="${ way.name }_label1" aria-hidden="true">
		<div class="modal-dialog modal-dialog-centered" role="document">
			<div class="modal-content">
				<div class="modal-header">
					<h4 class="modal-title" id="${ way.name }_label2">${ way.title }で支援する</h4>
					<button type="button" class="close" data-dismiss="modal" aria-label="Close">
						<span aria-hidden="true">×</span>
					</button>
				</div>
				<div class="modal-body">
${ way.desc }
				</div>
			</div>
		</div>
	</div>`;
}

// ------------------------------

function copyToClipboard() {
	// コピー対象をJavaScript上で変数として定義する
	var copyTarget = document.getElementById("copyTarget");
	// コピー対象のテキストを選択する
	copyTarget.select();
	// 選択しているテキストをクリップボードにコピーする
	document.execCommand("Copy");
	// コピーをお知らせする
	alert("コピーできました！ : " + copyTarget.value);
}

// ------------------------------
