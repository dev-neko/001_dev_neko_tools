/*

*/

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

function init() {
	//window.open( 'https://www.sejuku.net/blog/' );
	window.onmousedown = handleMouseDown;
}

function handleMouseDown(event) {
	event = event || window.event; // IE対応
	target = document.getElementsByName("Googleaaa");
	if (event.button == 0) {
		//target.innerHTML = "左ボタンが押されました。";
		window.location.replace( 'http://www.google.co.jp/' );
	}
	else if (event.button == 1) {
		//target.innerHTML = "中ボタンが押されました。";
		window.open( 'http://www.google.co.jp/' );
	}
	else if (event.button == 2) {
		target.innerHTML = "右ボタンが押されました。";
	}
}

function kakunin(){
  ret = prompt("ホームページのURLを入力", "http://www.google.co.jp/");
  if (ret != null){
    window.open(ret, "new");
  }
}