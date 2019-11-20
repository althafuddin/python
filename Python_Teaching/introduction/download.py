import requests 
file_url = "https://us-west-1.console.aws.amazon.com/?Action=DescribeAutoScalingGroups&AutoScalingGroupNames.member.1=nodes.io-engage-prod.k8s.local"
  
r = requests.get(file_url) 

print(r.text)
# with open("python.pdf","wb") as pdf: 
#     for chunk in r.iter_content(chunk_size=1024): 
  
#          # writing one chunk at a time to pdf file 
#          if chunk: 
#              pdf.write(chunk) 