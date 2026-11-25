class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build(values):              # [1,2,3] -> 1→2→3
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head

def to_list(head):              # 1→2→3 -> [1,2,3]
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def reverse_list(head):
    prev=None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt 

    return prev




for vals in [[1,2,3,4,5], [1,2], [], [7]]:
    print(vals, to_list(reverse_list(build(vals))))


