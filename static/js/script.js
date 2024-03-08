// フォームの少々お待ちくださいボタン
function OnButtonClick() {
    target = document.getElementById("js_wait_btn_output");
    target.innerHTML = "<br><h3>実行中〜少々お待ちください</h3>";
}
// 下記のようなコードが必要
/* <form method="post" action="/" enctype="multipart/form-data">
    <button type="submit" class="btn" onclick="OnButtonClick();" style="margin-top: 30px;">設定</button>
</form>
<div id="js_wait_btn_output"></div> */


function copyToClipboard() {
    const textToCopy = document.querySelector('.display-text');
    const tempInput = document.createElement('textarea');
    tempInput.value = textToCopy.innerText;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    document.body.removeChild(tempInput);
    target = document.getElementById("copyMessage");
    target.innerText = "Copied!";
}



