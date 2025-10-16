class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # chain from the first k elements this way you only visit every element once

        max_energy = float('-inf')

        for index in range(len(energy)-k,len(energy)):
            j = index
            running_energy = 0

            while j>=0:
                running_energy += energy[j] 
                j-=k

                max_energy = max(max_energy,running_energy)

        return max_energy

