import os

class Coder():
    def __init__(self,project_name):
        self.project_name = project_name
        file_path = os.path.abspath(__file__)
        files_dir = os.path.dirname(file_path)
        self.mk_folder = os.path.join(files_dir,self.project_name)
        if not os.path.isdir(self.mk_folder):
            os.mkdir(self.mk_folder)
    
    def create_package (self, package_name):
        os.chdir(self.mk_folder)
        self.package_name = package_name
        self.package = os.path.join(self.mk_folder,self.package_name)
        if not os.path.isdir(self.package):
            os.mkdir(self.package)

    def change_directory (self, name_project):
        self.name_project = name_project
        if self.package_name==self.name_project:
            os.chdir(self.name_project)
        else:
            os.chdir(self.mk_folder)
        return os.getcwd()
    
    def print_working_directory (self):
        return os.getcwd()

    def create_file (self, file_name):
        self.file_name = file_name
        self.file = os.path.join(os.getcwd(),self.file_name)
        open(self.file,'w') 
    
    def write_code (self, for_write_file, code):
        self.for_write_file = for_write_file
        self.code = code
        if self.file_name == self.for_write_file:
            with open (self.file_name,'w') as f:
                f.write(code)

    def run_code (self, for_run_file):
        self.for_run_file = for_run_file
        os.system(f"python {self.for_run_file}")

    


coder = Coder('task')
coder.create_package('files')
print(coder.change_directory('files'))
print(coder.print_working_directory())
coder.create_file('new.py')
coder.write_code('new.py',"print('Salam')")
coder.run_code('new.py')