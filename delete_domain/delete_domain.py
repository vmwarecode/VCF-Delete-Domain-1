#Delete a workload domain
import sys
import os
sys.path.append(os.path.abspath(__file__ + '/../../'))
from Utils.utils import Utils
import pprint

class DeleteDomain:
    def __init__(self):
        print('Delete Domain')
        self.utils = Utils(sys.argv)
        self.hostname = sys.argv[1]
        self.domain_id = sys.argv[4]

    def delete_domain(self):
        data = {"markForDeletion" : True}
        delete_domain_url = 'https://'+self.hostname+'/v1/domains/'+self.domain_id
        self.utils.patch_request(data,delete_domain_url)
        response = self.utils.delete_request({},delete_domain_url)
        print ("Deleting Domain ...")
        task_id = response['id']
        tasks_url = 'https://'+self.hostname+'/v1/tasks/'+task_id
        print ("Domain deletion Status:"+ self.utils.poll_on_id(tasks_url,True))

if __name__== "__main__":
    DeleteDomain().delete_domain()

