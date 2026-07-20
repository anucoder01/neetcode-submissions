class Solution:
    def mergeKLists(self, lists):

        if not lists:
            return None

        while len(lists) > 1:

            merged = []

            for i in range(0, len(lists), 2):

                list1 = lists[i]

                if i + 1 < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None

                merged.append(self.merge(list1, list2))

            lists = merged

        return lists[0]

    def merge(self, list1, list2):

        dummy = ListNode()
        tail = dummy

        while list1 and list2:

            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next