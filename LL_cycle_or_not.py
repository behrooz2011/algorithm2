class Solution:
    def hasCycle(self, head) -> bool:
        if head is None:
            return False
        slow = head #turtle
        fast = head.next #rabbit
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next #turtle takes one step
            fast = fast.next.next #rabbit takes two steps
        return True # They eventually meet