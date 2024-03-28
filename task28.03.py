#1

def concat_array(nums):
    return nums + nums
nums1 = [1, 2, 1]
print(concat_array(nums1)) 

nums2 = [1, 3, 2, 1]
print(concat_array(nums2)) 


#2
    
def permutation(nums):
    n = len(nums)
    ans = [0] * n
    
    for i in range(n):
        ans[i] = nums[nums[i]]
    
    return ans
nums1 = [0, 2, 1, 5, 3, 4]
print(permutation(nums1)) 

nums2 = [5, 0, 1, 2, 3, 4]
print(permutation(nums2))  



#3

def temperature_conversion(celsius):
    kelvin = round(celsius + 273.15, 5)
    fahrenheit = round(celsius * 1.8 + 32.0, 5)
    return [kelvin, fahrenheit]

celsius1 = 36.50
print(temperature_conversion(celsius1))

celsius2 = 122.11
print(temperature_conversion(celsius2))
