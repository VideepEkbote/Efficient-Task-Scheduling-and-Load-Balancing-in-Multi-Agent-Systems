'''
    This file contains the class definition for the StrawHat class.
'''

import crewmate
import heap
import treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''

    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        yrr = []
        for i in range(m):
            yrr.append(crewmate.CrewMate())
        self.crewmates = heap.Heap(heap.crewcomparer, yrr)
        self.using = []
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''

        leastloadwaala = self.crewmates.extract()
        leastloadwaala.arr.append(treasure)
        if leastloadwaala.finalcompletiontime == 0:
            self.using.append(leastloadwaala)
        leastloadwaala.finalcompletiontime =max(leastloadwaala.finalcompletiontime,treasure.arrival_time)+treasure.size
        self.crewmates.insert(leastloadwaala)


    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        ans = []
        for crewmember in self.using:
            for h in crewmember.arr:
                h.remainingsize = h.size
            processingheap = heap.Heap(heap.treasurecomparer, [])
            if len(crewmember.arr) > 0:
                j = 0
                cur_time = 0
                while j < len(crewmember.arr):
                    if len(processingheap.arr) > 0:
                        while cur_time + processingheap.top().remainingsize <= crewmember.arr[j].arrival_time:
                            y = processingheap.extract()
                            y.completion_time = cur_time + y.remainingsize
                            cur_time = y.completion_time
                            ans.append(y)
                            if len(processingheap.arr) == 0: break
                        if len(processingheap.arr) > 0:
                            y = processingheap.extract()
                            y.remainingsize -= crewmember.arr[j].arrival_time - cur_time
                            processingheap.insert(y)
                            cur_time = crewmember.arr[j].arrival_time
                            processingheap.insert(crewmember.arr[j])
                        else:
                            processingheap.insert(crewmember.arr[j])
                            cur_time = crewmember.arr[j].arrival_time
                    else:
                        processingheap.insert(crewmember.arr[j])
                        cur_time = crewmember.arr[j].arrival_time
                    j+=1


                while len(processingheap.arr)>0:
                    y = processingheap.extract()
                    y.completion_time = cur_time + y.remainingsize
                    cur_time = y.completion_time
                    ans.append(y)


        ans.sort(key = lambda x: x.id)
        return ans















        # Write your code here
        pass

    # You can add more methods if required