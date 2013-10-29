enquest
=======

Simple text quest engine (for Encounter games).

Working version (Russian): http://endead.me
Testing: http://test.endead.me

Example for quest in Encounter engine:
```
<script>
    var quest_hash = "809a781426e275841dc25aaba2a2d6d3";
    var backend_site = "http://test.endead.me/"
    function quest(hash) {
        $('#data').html('&nbsp;').load(backend_site+ 'q/' + hash);
    }
    function main() {
        quest(quest_hash);
    }
    $(document).ready(main);
</script>
<div id='data'></div>
```
