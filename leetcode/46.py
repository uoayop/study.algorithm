def permute(nums) :
    results = []
    prev_elements = []
    
    def dfs(elements):
        #elements: [1,2,3]
        
        #리프 노드이면 결과 추가
        if len(elements)==0:  
            results.append(prev_elements[:])
            print("[results]:",results)
        
        #순열 생성 재귀 호출
        for e in elements:
            print("[e]:",e,"[elements]:",elements)
            #next_elements에 elements 모두 복사해주고
            next_elements = elements[:]
            print("[next_elements_before_remove]:",next_elements)
            next_elements.remove(e)
            print("[next_elements_after_remove]:",next_elements)
                
            
            prev_elements.append(e)
            print("[prev_elements_append_e]:",prev_elements)
            print("[dfs_next_elements]:",next_elements)
            print("---------dfs-------------")
            dfs(next_elements)
            prev_elements.pop()
            print("[prev_elements_pop]:",prev_elements)
            
    dfs(nums)
    return results

print(permute([1,2,3]))