from DisjointSet import *

def main():
    ds = DisjointSet(1, 2, 3, 'a', 'b', 'c')
    print(ds)
    ds.connect(1, 'b')
    print(ds)
    ds.connect('b', 'c')
    print(ds)
    ds.connect(2, 3)
    ds.connect('a', 2)
    ds.connect('a', 'c')
    print(ds)
    print(ds.isConnected('c', 2))


if __name__ == "__main__":
    main()
