##CS 2302 Data Structures
##Instructor:Diego Aguirre
##TA: Anindita Nath
##Project 4 Option A
##Modified and submitted by Andres Ponce 80518680
##Date of last modification 11/11/2018
##Purpose: Create a hash table with a given file.
##The file contains word embeddings. Functions of
##the hash table are: insert, search, remove,
##calculate the load factor, and the average of comparisons
##Find the similarity of two words given by a file. 

import os
import random
import time
import re
import math

####################   Hash table    ######################
# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=600000):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
      
    # Inserts a new item into the hashtable.
    def insert(self, item, embed):
        # get the bucket list where this item will go.
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]
        pair=[item,embed]

        # insert the item to the end of the bucket list.
        bucket_list.append(pair)
         
    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for i in range (len(bucket_list)):
            if key in bucket_list[i][0]:
                return bucket_list[i]

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if key in bucket_list:
            bucket_list.remove(key)
      
    # Overloaded string conversion method to create a string
    # representation of the entire hash table. Each bucket is shown
    # as a pointer to a list object.
    def __str__(self):
        index = 0
        s =  "   --------\n"
        for bucket in self.table:
            s += "%2d:|   ---|-->%s\n" % (index, bucket)
            index += 1
        s += "   --------"
        return s

    def calcLoadFactor(self):
        count=0
        for bucket in self.table:
            if not bucket is None:
                count=count+len(bucket)
        lam=count/len(self.table)       
        return lam

    def calcAvg(self):
        lam = self.calcLoadFactor()
        avg = 1 + (lam/2)
        return avg
    
##formula (e_0 (dot product) e_1) / |e_0| (magnitude of e_0) * |e_1| (magnitude of e_1)
def calcEmbed(file, hashTable):
    for line in file:
        data=line.split()
        found1=hashTable.search(data[0])    
        found2=hashTable.search(data[1])
        e0=found1[1]
        e1=found2[1]
        top=0
        mag1=0
        mag2=0
        for i in range (len(e0)):
            top=top+(float(e0[i])*float(e1[i]))
        for i in range (len(e0)):
            mag1=mag1+(float(e0[i])*float(e0[i]))
            mag2=mag2+(float(e1[i])*float(e1[i]))
        mag1=math.sqrt(mag1)
        mag2=math.sqrt(mag2)
        down=mag1*mag2
        sim=top/down
        print(data[0],data[1],sim)

def createHashTable(file):
    chaining = ChainingHashTable()
    for line in file:
            data = line.split()
            word=data[0]
            if re.match("^[a-zA-Z]*$", word):
                embed=[]
                for i in range (1,len(data)):
                    embed.append(data[i])
                chaining.insert(word,embed)
    print ("Chaining: initial table:")
    #print (chaining)
    embedFile=open("embed.txt")
    print("Similarities: ")
    calcEmbed(embedFile,chaining)
    print('Load factor: ', chaining.calcLoadFactor())
    print('Avg of comparisons: ',chaining.calcAvg())
    return chaining

def main():
# Main program to test HashTable classes
    path=input("Enter path: ")
    path=path[2:]
    start_path = (r""+path+"")
    file=open(start_path,"r")
    createHashTable(file)

main()
