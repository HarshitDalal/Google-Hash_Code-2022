from collections import namedtuple as nt
def read_files(filename):
    f = open(filename)
    emp,proj = map(int,f.readline().split())

    # Employess Details
    emps = []
    em = nt('em',['name','skill'])
    for _ in range(emp):
        name,skno = f.readline().split()
        skno = int(skno)
        skil = {}
        for i in range(skno):
            skname,level = f.readline().split()
            skil |= {skname:int(level)}
        emps.append(em(name,skil))
    
    # Projects Details
    projs = []
    pr = nt('pr',['name','day','score','best','cont','skill'])
    for _ in range(proj):
        name,day,score,best,cont = f.readline().split()
        day,score,best,cont = int(day),int(score),int(best),int(cont)
        skill = {}
        for i in range(cont):
            sk,lev = f.readline().split()
            skill |= {sk:int(lev)}
        projs.append(pr(name,day,score,best,cont,skill))

    f.close()
    return emps,projs

def write_files(filename,res):
    f = open(filename,'w')
    l = len(res)
    f.write(f'{l}\n')
    for i in range(l):
        for j in range(len(res[i])):
            data = ' '.join(res[i][j]) if type(res[i][j]) == list else res[i][j]
            f.write(f'{data}\n')
    f.close()
    



def project(em,pro):
    pr = pro.copy()
    lpr = len(pr)
    i = 0
    done = []
    while i != lpr:
        l = len(pr)
        for j in range(l):
            names = []
            ss = []
            p = ''
            for k in pr[j].skill:
                na ,s= employee(em,k,pr[j].skill[k])
                if na != '':
                    if na not in names:
                        names.append(na)
                        ss.append(s)
                        p = pr[j].name
            if len(names) == pr[j].cont :
                done.append((p,names))
                for x,y in zip(names,ss):
                    for e in em:
                        if x == e.name:
                            e.skill[y]+=1           
                pr.pop(j)
                break
        i+=1
    return done

def employee(emp,skill,level):
    ename,s = '' , ''
    for i in emp:
        if skill in i.skill:
            if level <= i.skill[skill]:
                ename = i.name
                s = skill
                break
    return ename,s


if __name__ == '__main__':
    filename = 'a_an_example'
    # filename = 'b_better_start_small'
    em,pr = read_files(f'{filename}.in.txt')
    ff = open("heel.txt",'w')
    for i in em:
        ff.writelines(f'{i}\n')
    ff.close()
    ans = project(em,pr)
    ff = open("hel.txt",'w')
    for i in em:
        ff.writelines(f'{i}\n')
    ff.close()
    
    write_files(f'{filename}.out.txt',ans)
    
