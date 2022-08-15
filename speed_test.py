from picalculator import calculate_serialy, calculate_with_threads, calculate_with_processes


if __name__ == '__main__':
    
    calculate_serialy()          # 直列的に7回処理を行う
    calculate_with_threads()     # 7つの Thread を作成し、並行処理を行う
    calculate_with_processes()   # 7つの Process を作成し、並列処理を行う
    