from collections import Counter

def hasCycle(head):
  slow, fast = head, head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      return True
  
  return False

if __name__ == '__main__':
  head = [3,2,0,-4], pos = 1
  print(hasCycle(head))