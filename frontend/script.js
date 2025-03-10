// Auto update timestamp dạng ISO 8601 mỗi giây
function getCurrentTimestamp() {
    return new Date().toISOString().split('.')[0] + 'Z';
  }
  
  // Gọi khi load và mỗi 1 giây cập nhật lại
  getCurrentTimestamp();
  setInterval(getCurrentTimestamp, 1000);
  
  // Hàm sort object theo key
  function sortObject(obj) {
    return Object.keys(obj).sort().reduce((acc, key) => {
      acc[key] = obj[key];
      return acc;
    }, {});
  }
  
  // Hàm tạo chữ ký
  function generateSignature() {
    const secretKey = document.getElementById('secret_key').value.trim();
    const timestamp = getCurrentTimestamp();
    const bodyInput = document.getElementById('body_json').value.trim();
  
    let bodyObj;
    try {
      bodyObj = JSON.parse(bodyInput);
    } catch (e) {
      alert('❌ Invalid JSON Body!');
      return;
    }
  
    const sortedBody = sortObject(bodyObj);
    const payload = JSON.stringify(sortedBody); // Body chuẩn JSON sau khi sort
  
    const signatureString = timestamp + payload; // Ghép timestamp + body để ký
  
    const signature = CryptoJS.HmacSHA256(signatureString, secretKey).toString(CryptoJS.enc.Hex);
  
    document.getElementById('signature_result').innerText = 'Signature: ' + signature;
  }
  
  // Hàm kiểm tra chữ ký
  function validateSignature() {
    const secretKey = document.getElementById('secret_key').value.trim();
    const timestamp = getCurrentTimestamp();
    const bodyInput = document.getElementById('body_json').value.trim();
    const requestSignature = document.getElementById('request_signature').value.trim();
  
    let bodyObj;
    try {
      bodyObj = JSON.parse(bodyInput);
    } catch (e) {
      alert('❌ Invalid JSON Body!');
      return;
    }
  
    const sortedBody = sortObject(bodyObj);
    const payload = JSON.stringify(sortedBody);
  
    const signatureString = timestamp + payload;
  
    const generatedSignature = CryptoJS.HmacSHA256(signatureString, secretKey).toString(CryptoJS.enc.Hex);
  
    const result = (generatedSignature === requestSignature) ? "✅ Signature is VALID!" : "❌ Signature is INVALID!";
    document.getElementById('validate_result').innerText = 'Validation: ' + result;
  }
  