class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")
        stack = []
        for apath in split_path:
            if not apath or apath == ".":
                continue
            elif apath == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(apath)
        return "/" + "/".join(stack)