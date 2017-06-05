# coding=utf-8

class FictionTool:



    def __init__(self, fiction_path):
        self.full_content = ''
        self.chapter_list = []
        self.chapter_2_content = {}
        self.__preProcess(fiction_path)

    def __preProcess(self, fiction_path):
        f = open(fiction_path)
        self.full_content = f.read().decode('utf-8')
        line_list = self.full_content.split('\n')
        chapter = None
        cont = ''
        for line in line_list:

            if not line.strip():
                continue
            if not line.startswith(' '):
                if chapter is None:
                    chapter = line.strip()
                else:
                    self.chapter_list.append(chapter)

                    self.chapter_2_content[chapter] = cont
                    cont = ''
                    chapter = line.strip()
            else:                cont += line + '\n'
        self.chapter_list.append(chapter)
        self.chapter_2_content[chapter] = cont

    def get_content_list(self, start=None, end=None):
        """
        返回指定的章节内容和标题
        :param start:
        :param end:
        :return:
        """
        if start is None:
            start = 0
        if end is None:
            end = self.chapter_list.__len__()
        content_list = []
        chapter_list = []
        for i in range(start, end+1):
            chapter_list.append(self.chapter_list[i])
            content_list.append(self.chapter_2_content[self.chapter_list[i]])
        return chapter_list, content_list

if __name__ == '__main__':
    shz = FictionTool('data/水浒传.txt')
    a,b = shz.get_content_list(1, 15)
    print '\n'.join(a)
    print b[2]