/*

*/

// ------------------------------

// ペーストボタン
// これはなぜか関数にすると入力内容が初期化されずに正常に動作しなかった
const btn_paste = document.querySelector('#js-paste');
// ペースト対象となるテキストエリア
const paste_target = document.querySelector('#target');

btn_paste.addEventListener('click', () => {
	const result = pasteText((text) => {
		paste_target.focus();
		paste_target.value = paste_target.value + text;
	});
});

const pasteText = (callback) => {
	// 閲覧しているブラウザが「navigator.clipboard」に対応しているか確認
	if(navigator.clipboard){
		// クリップボードにあるテキストを読み込み
		navigator.clipboard.readText().then((text) => {
			// 読み込んだテキストを操作
			callback(text);
	});
	return true;
	} else {
	return false;
	}
}

// ------------------------------

//フォーカスを合わせる

function clfc(){
	document.getElementById('target').focus();
}

// ------------------------------

// クリアしてペーストするボタン
function clear_paste_btn(){
	// ペーストボタン
	const btn_paste = document.querySelector('#rstpst');
	// ペースト対象となるテキストエリア
	const paste_target = document.querySelector('#target');

	btn_paste.addEventListener('click', () => {
		const result = pasteText((text) => {
			paste_target.focus();
			// paste_target.value + を消せばクリポの内容だけを入力可能
			paste_target.value = text;
		});
	});

	const pasteText = (callback) => {
		// 閲覧しているブラウザが「navigator.clipboard」に対応しているか確認
		if(navigator.clipboard){
			// クリップボードにあるテキストを読み込み
			navigator.clipboard.readText().then((text) => {
				// 読み込んだテキストを操作
				callback(text);
		});
		return true;
		} else {
		return false;
		}
	}
}

// ------------------------------

//BootstrapのPopperを使用するためのJS
(function() {
	window.addEventListener("load", function () {
		$('[data-toggle="popover"]').popover();
	});
})();

// ------------------------------

// サジェスト機能
$(function() {
	$('#target').autocomplete({
		source: function(request, response) {
			$.ajax({
				url: "https://www.google.com/complete/search",
				data: {hl:'ja', client:'firefox', q: request.term},
				dataType: "jsonp",
				type: "GET",
				success :function(data) {response(data[1]);
				}
			});
		},
		autoFocus: false,
		delay: 200,
		minLength: 1,
	});
});

// ------------------------------
