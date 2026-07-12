class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Stack stores pairs of (node, current_depth)
        stack = [(root, 1)]
        max_depth = 0
        
        while stack:
            node, current_depth = stack.pop()
            
            # Update the maximum depth encountered so far
            max_depth = max(max_depth, current_depth)
            
            # Push children onto the stack with incremented depth
            if node.right:
                stack.append((node.right, current_depth + 1))
            if node.left:
                stack.append((node.left, current_depth + 1))
                
        return max_depth