function loadMsrank() {
    console.log("fix1")
    d3.json("/api/ms_rank").then((data) => {
        console.log("fix2");
        
        // data.forEach((row)) => {
        //     var listGroup = d3.select("#row");
        //     var listItem = listGroup.append("li");
        //     listItem.text(row.game);
        //     listItem.attr("class","list-group")
        // }
    })
}

loadMsrank();