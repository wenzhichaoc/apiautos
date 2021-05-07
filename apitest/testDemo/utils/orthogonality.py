from allpairspy import AllPairs


class Orthogonality():

    def orthogonality_do(self, reqbody):
        res = []
        for i in AllPairs(reqbody):
            res.append(i)

        return res


if __name__ == '__main__':
    username = ['admin', 123, 'null']
    password = ['password', 123, 'notnull']
    nickname = ['nick', 123, 'notnull']

    reqbody = []
    reqbody.append(username)
    reqbody.append(password)
    reqbody.append(nickname)

    res = Orthogonality().orthogonality_do(reqbody)
    print(len(res))