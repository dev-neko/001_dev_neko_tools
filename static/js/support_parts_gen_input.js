// ------------------------------

function onButtonClick() {
	const ky = {name:		'Kyash',
							title:	'Kyash',
							desc:		document.forms.id_form1.Kyash_desc.value,
							color:	document.forms.id_form1.Kyash_color.value}
	const pr = {name:		'pring',
							title:	'pring',
							desc:		document.forms.id_form1.pring_desc.value,
							color:	document.forms.id_form1.pring_color.value}
	const aw = {name:		'Amazon_wish',
							title:	'Amazonほしい物リスト',
							desc:		document.forms.id_form1.Amazon_wish_desc.value,
							color:	document.forms.id_form1.Amazon_wish_color.value}
	const ag = {name:		'Amazon_gift',
							title:	'Amazonギフト券',
							desc:		document.forms.id_form1.Amazon_gift_desc.value,
							color:	document.forms.id_form1.Amazon_gift_color.value}
	const py = {name:		'PayPay',
							title:	'PayPay',
							desc:		document.forms.id_form1.PayPay_desc.value,
							color:	document.forms.id_form1.PayPay_color.value}
	const rp = {name:		'rakutenpay',
							title:	'楽天ペイ',
							desc:		document.forms.id_form1.rakutenpay_desc.value,
							color:	document.forms.id_form1.rakutenpay_color.value}
	const pp = {name:		'paypal',
							title:	'PayPal',
							desc:		document.forms.id_form1.paypal_desc.value,
							color:	document.forms.id_form1.paypal_color.value}
	const rg = {name:		'rgram',
							title:	'6gram',
							desc:		document.forms.id_form1.rgram_desc.value,
							color:	document.forms.id_form1.rgram_color.value}
	const ap = {name:		'aupay',
							title:	'auPAY',
							desc:		document.forms.id_form1.aupay_desc.value,
							color:	document.forms.id_form1.aupay_color.value}
	const db = {name:		'dbarai',
							title:	'd払い',
							desc:		document.forms.id_form1.dbarai_desc.value,
							color:	document.forms.id_form1.dbarai_color.value}
	const mp = {name:		'merpay',
							title:	'メルペイ',
							desc:		document.forms.id_form1.merpay_desc.value,
							color:	document.forms.id_form1.merpay_color.value}
	const qp = {name:		'quopay',
							title:	'QUOPay',
							desc:		document.forms.id_form1.quopay_desc.value,
							color:	document.forms.id_form1.quopay_color.value}
	document.getElementById("copyTarget").innerHTML = '<div class="support-parts">\n'+
	 tag`${ rg }` +"\n"+
	 tag`${ ky }` +"\n"+
	 tag`${ ag }` +"\n"+
	 tag`${ aw }` +"\n"+
	 tag`${ py }` +"\n"+
	 tag`${ pp }` +"\n"+
	 tag`${ rp }` +"\n"+
	 tag`${ db }` +"\n"+
	 tag`${ qp }` +"\n"+
	 tag`${ ap }` +"\n"+
	 tag`${ pr }` +"\n"+
	 tag`${ mp }` +"\n"+
	 "</div>";
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
