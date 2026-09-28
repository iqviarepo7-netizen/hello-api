document.addEventListener('DOMContentLoaded', function () {
    var runBtn = document.getElementById('runPipelineBtn');
    if (runBtn) {
        runBtn.addEventListener('click', function () {
            var modalEl = document.getElementById('welcomeModal');
            var modal = new bootstrap.Modal(modalEl);
            modal.show();
        });
    }
});
