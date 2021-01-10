function loadMsrank() {
    d3.json("/api/ms_rank").then((data) => {
        console.log(data);
        data.forEach((game) => {
            var listGroup = d3.select('#games');
            var listItem = listGroup.append("li");
            listItem.text((task.description);

           listItem.attr("class", "list-group-item);
        });
        
    });
}

loadMsrank();
