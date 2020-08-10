1. AWS upload file to S3 by python api
	--> S3_demo

2. connect with line chat bot 
	--> app.py

3. create AWS configure by Amazon CLI
	--> Download AWS CLI:
		[LINK](https://aws.amazon.com/tw/cli/)

4. Introduction of Permissions of AWS S3	
	Method A. permission to public (single file)
	Method B. bucket policy 

	Method A. 
		=> upload any file to S3
		=> check the url whether it can be permissioned (ANS: NO!); however it can be dowloaded in the console( on AWS conconsole)

		=> Using Method A. to make the single file be public 
		=> check the url whether it can be permissioned (ANS: YES!)		

	Method B. 
	Edit the Bucket Policy
		PATHWAYS: 
			a. enter selected bucket 
			b. click permission  
			c. click Bucket Policy 
				go check the official documentation 
				(Bucket Policy Example: https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html)

5. Setting S3 properties (Verisoning)
	PATHWAYS: 
		a. entry selected bucket
		b. click properties
		c. enable versioning
		d. back to overview
		e. click Show(versions)
		f. upload another file but exists on S3
		g. figuring out there are two versions of the same file and also enable to click






---

FULL tutorial:

	Web Page tutorial: https://www.qwiklabs.com/focuses/11776?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=6462137

