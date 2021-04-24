class GitManager():
    '''
    A simple demo Git Operations.
    '''

    current_commit = 0

    def __init__(self, my_list = [], my_dict = {}, count = 0):
        self.my_list = my_list
        self.my_dict = my_dict
        self.count = count


    def git_commit_message(self, new_commit):
        '''
        This will store something in the Git with auto generated ID.
        '''

        self.count += 1
        GitManager.current_commit = 0
        key = str(self.count)
        self.my_list.insert(0, key)
        self.my_dict[key] = new_commit


    def git_show_commit(self):
        '''
        This will print the current commit.
        '''

        key = self.my_list[GitManager.current_commit]
        print("user@user:~$ | Current commit message: {}".format(self.my_dict[key]))


    def git_show_all_commit(self):
        '''
        This will print all the commits according to serial.
        '''

        for i in self.my_list:
            print('user@user:~$ | {} : {}'.format(i,self.my_dict[i]))


    def git_delete_sequence(self, commit_key):
        '''
        This will delete a target Git commit.
        '''

        key = str(commit_key)
        self.my_list.remove(key)
        self.my_dict.pop(key)


    def git_forward_commit(self):
        '''
        This will incress the commit ID by one
        '''

        if GitManager.current_commit < len(self.my_list):
            GitManager.current_commit += 1
        else:
            print('user@user:~$ | Current commit is the last commit.')


    def git_backward_commit(self):
        '''
        This will decrease the commit ID by one
        '''

        if GitManager.current_commit > 0:
            GitManager.current_commit -= 1
        else:
            print('user@user:~$ | Current commit is the latest commit.')


    def git_update_message(self, updated_message):
        '''
        This method will update the current git message.
        '''

        key = self.my_list[GitManager.current_commit]
        self.my_dict.update({key: updated_message})



    def git_jump_commit(self, commit_key):
        '''
        This will jump into a commit ID and make that current commit.
        '''

        GitManager.current_commit = self.my_list.index(str(commit_key))


    def git_pull_commit(self, commit_key):
        '''
        This will select a commit ID and insert at the top, also make that the current commit.
        '''

        key = str(commit_key)
        self.my_list.remove(key)
        self.my_list.insert(0, key)



if __name__ == '__main__':
    my_git = GitManager()
    count_main = 0

    # my_git.git_commit_message('hello')
    # my_git.git_commit_message('hello 2')
    # my_git.git_commit_message("hello3")
    # my_git.git_commit_message('hello 4')
    # my_git.git_show_all_commit()
    # print('a')
    # my_git.git_show_commit()
    # print('b')
    # my_git.git_delete_sequence(3)
    # my_git.git_show_all_commit()
    # print('c')
    # my_git.git_forward_commit()
    # my_git.git_show_commit()
    # print('d')
    # my_git.git_backward_commit()
    # my_git.git_show_commit()
    # print('e')
    # my_git.git_pull_commit(2)
    # my_git.git_show_all_commit()
    # print('f')
    # my_git.git_jump_commit(4)
    # my_git.git_show_commit()
    # print('g')
    # my_git.git_update_message('new hello')
    # my_git.git_show_all_commit()

    while True:
        input_val = input('user@user:~$ | ')
        input_val = input_val.split()
        input_val = " ".join(input_val)

        if input_val == "git init":
            print("user@user:~$ | Git active.")

            while True:
                val_new = input('user@user:~$ | ')
                val_new = val_new.split("'")
                val_new = " ".join(val_new)
                val_new = val_new.split('"')
                val_new = " ".join(val_new)
                val_new = val_new.split()

                if val_new[0] == 'git' and val_new[1] == 'commit':
                    temp = []
                    for i in range (2,len(val_new)):
                        temp.append(val_new[i])

                    temp = " ".join(temp)
                    my_git.git_commit_message(temp)

                elif val_new[0] == 'git' and val_new[1] == 'show'  and val_new[2] == 'commit':
                    my_git.git_show_commit()

                elif val_new[0] == 'git' and val_new[1] == 'show' and val_new[2] == 'all' and val_new[3] == 'commit':
                    my_git.git_show_all_commit()

                elif val_new[0] == 'git' and val_new[1] == 'delete':
                    my_git.git_delete_sequence(val_new[2])

                elif val_new[0] == 'git' and val_new[1] == 'forward-commit':
                    my_git.git_forward_commit()

                elif val_new[0] == 'git' and val_new[1] == 'backward-commit':
                    my_git.git_backward_commit()

                elif val_new[0] == 'git' and val_new[1] == 'update':
                    temp = []
                    for i in range(2, len(val_new)):
                        temp.append(val_new[i])

                    temp = " ".join(temp)
                    my_git.git_update_message(temp)

                elif val_new[0] == 'git' and val_new[1] == 'jump':
                    my_git.git_jump_commit(val_new[2])

                elif val_new[0] == 'git' and val_new[1] == 'pull':
                    my_git.git_pull_commit(val_new[2])

                elif val_new[0] == 'exit':
                    print('user@user:~$ | Git Deactivate.')
                    break

                else:
                    print('user@user:~$ | Invalid input.')

        else:
            print('user@user:~$ | Invalid input.')


