netscape.security.PrivilegeManager.enablePrivilege("UniversalBrowserRead");
netscape.security.PrivilegeManager.enablePrivilege("UniversalBrowserWrite");

let data = "Simple Test";

function SaveButton(event) {
    var file = document.getElementById('fileItem').files[0];

    loadAsText(file);
  }

function loadAsText(theFile) {
    var reader = new FileReader();

    reader.onload = function(loadedEvent) {
        // result contains loaded file.
        console.log(loadedEvent.target.result);
    }
    reader.readAsText(theFile);
}
