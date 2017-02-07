def printMinMax(list):
    print max(list);
    print min(list);

def printFirstLast(list):
    first = list[0];
    last = list[len(list)-1];
    newList = [first, last];
    print newList;

def newList(list):
    newList = [];
    list.sort();
    newList.append(list[0]);
    newList.append(list[1]);
    list.pop(0);
    list.pop(0);
    list.insert(0,newList);
    print newList;
    print list;

str = "If monkeys like bananas, then I must be a monkey!";
searchString = "monkey";
str2 = "alligator";
print str.find(searchString);
print str.find(searchString, 4);
print str.replace("monkey", "alligator");
printMinMax([2,43,-2,45,-32,234]);
printFirstLast([2,43,-2,45,-32,234]);
newList([19,2,54,-2,7,12,98,32,10,-3,6]);
