var mainModel = {
	BASE_URL : "http://192.168.1.106:8080/solr/select/",
	search : function(content, onSuccess, onErorr){
		var url;

		//url = 'http://localhost:8085/?content='
		url = 'extract?content='
		url = url + encodeURIComponent(content);
		console.debug(url);
		$.ajax({
			  url: url,
			  dataType: 'text',
			  success: function(data) {
			    console.debug(data);
			    onSuccess(data);
			  },
			  
			  error: function(xhr_data,strError){
				console.debug(xhr_data);
				console.debug();
				onErorr(xhr_data);
			  }
		});
	}
	
};
