class BaseTest():

    def validate_json_response(results_content, expected_result):
        assertion = False
        possible_results = len(expected_result)
        fails = 0
        for result in results_content:
            it = 0
            assertion = False
            while it < possible_results:
                if expected_result[it] in result:
                    assertion = True
                    break
                it += 1
            if assertion == False:
                fails += 1  
        return fails
                