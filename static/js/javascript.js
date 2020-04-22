// ------------------------------

// ペーストするボタン

// ペーストボタン
const btn_paste = document.querySelector('#js-paste');
// ペースト対象となるテキストエリア
const paste_target = document.querySelector('#target');

btn_paste.addEventListener('click', () => {
	const result = pasteText((text) => {
		document.getElementById('target').focus();
		paste_target.value = document.getElementById("target").value + text;
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

/*

これ追加すると他のボタンも機能しなくなる

// クリアしてペーストするボタン

// ペーストボタン
const btn_paste = document.getElementsByName('rstpst');
// ペースト対象となるテキストエリア
const paste_target = document.querySelector('#target');

btn_paste.addEventListener('click', () => {
	const result = pasteText((text) => {
		document.getElementById('target').focus();
		paste_target.value = document.getElementById("target").value + text;
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

*/

// ------------------------------

