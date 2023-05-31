<script lang="ts">

    export let img;
    export let id;

    console.log(id)


</script>

<!-- The button to open modal -->
<label for={id} class="btn btn-xs">Image</label>

<!-- Put this part before </body> tag -->
<input type="checkbox" id={id} class="modal-toggle" />
<label for={id} class="modal cursor-pointer">
  <label class="modal-box relative" for="">
    <div class="flex justify-center">
        <img src={`http://localhost:8090/api/files/receipts/${id}/${img}`} alt="">
    </div>
  </label>
</label>