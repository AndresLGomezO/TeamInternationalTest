class BuildStats:
        def __init__(self, values):
            self.stats_values = values

        def less(self, bound):
            result=0
            resultItems=[]
            for item in self.stats_values:
                if item < bound:
                    resultItems.append(item)
                    result = result + 1
            
            print("There are " + str(result) + " items less than " + str(bound) + " !!")
            print("========ITEMS========")
            print(resultItems)
            print("=====================")
            return result, resultItems
        
        def greater(self, bound):
            result=0
            resultItems=[]
            for item in self.stats_values:
                if item > bound:
                    resultItems.append(item)
                    result = result + 1
            
            print("There are " + str(result) + " items greater than " + str(bound) + " !!")
            print("========ITEMS========")
            print(resultItems)
            print("=====================")
            return result, resultItems
        
        def between(self, lBound, uBound):
            result=0
            resultItems=[]
            for item in self.stats_values:
                if item < uBound and item > lBound:
                    resultItems.append(item)
                    result = result + 1
            
            print("There are " + str(result) + " items between " + str(lBound) + " and " + str(uBound) + " !!")
            print("========ITEMS========")
            print(resultItems)
            print("=====================")
            return result, resultItems


class DataCapture:
    def __init__(self, initialValues=[]):
        self.values = initialValues

    def add(self, item):
        self.values.append(item)

    def show_values(self):
        return self.values
    
    def build_stats(self):
        return BuildStats(self.values)


class DataCaptureAndStats:
    
    def __init__(self):
        initialValues=[1,2,3,4,5,6,7,8,9,0]
        self.data_capture=DataCapture(initialValues)
        
    def run(self):
        data_capture=self.data_capture
        data_capture.add(3)
        data_capture.add(1000)
        array_values=data_capture.show_values()
        print("Values: " + str(array_values))

        stats=data_capture.build_stats()

        stats.less(4)
        stats.greater(4)
        stats.between(1, 4)       


testProgram=DataCaptureAndStats()
testProgram.run()