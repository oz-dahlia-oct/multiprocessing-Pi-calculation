from picalculator import PiCalculator

if __name__ == '__main__':
    
    calculator = PiCalculator(notebook=False)
    calculator.calculate()                  # 直列的に7回処理を行う
    calculator.calculate_with_threads()     # 7つの Thread を作成し、並行処理を行う
    calculator.calculate_with_processes()   # 7つの Process を作成し、並列処理を行う
    