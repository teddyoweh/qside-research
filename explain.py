from dataclasses import dataclass
import openai
from utils import Utils
from datetime import datetime
@dataclass
class explain:
    gpt_key: str

    input_variablies:str = """
Input variables:

SERIALNO: Serial Number
SPORDER:
WGTP: ???
PWGTP: Integer weight of person
AGEP: Age
PUMA: Public use microdata area code
ST: State code based on 2010 Census definitions
SCH: School enrollment
SEX: ??? (I will Assume sex but there are unknown labels)
ESR: Recoded employment status
HISP: Hispanic origin
RAC1P: Race code
    """
    def age_data(self, data):
       
        eda_prompt = f"""
        Exploratory Data Analysis (EDA) of Age Distribution:

        In this EDA, we aim to visualize the distribution of ages within the dataset to gain insights into the demographic composition. 
        We achieve this by plotting a histogram with 20 bins, representing different age groups, and overlaying a kernel density estimate (KDE) curve for smoother visualization. 
        The plot is colored sky blue for better clarity.

        Data Points:
        Age Distribution: {data}

        Insight Explanation:
        Based on the provided age distribution plot, we observe that the majority of individuals in the dataset fall within certain age ranges, as indicated by the peaks in the histogram. 
        The KDE curve further smooths out the distribution, providing a clearer picture of the overall age distribution pattern. 
        This analysis helps us understand the age demographics of the dataset and identify any notable trends or patterns.
        
        
        Give a brief explanation of the age distribution plot.

        """
        return self.call_gpt(eda_prompt)
    def correlation_martix(self, data):
        prompt = f"Generate a brief explanation for the correlation matrix of integer columns and what they imply:{self.input_variablies}\n{data}"
        return self.call_gpt(prompt)  
    def age_distribution(self,df, column_name, bins=20):
            age_data = df[column_name]
            num_bins = bins
            prompt = f"Generate a brief explanation for the age distribution plot with {num_bins} bins:\n" \
                    f"The plot displays the distribution of ages in the dataset. " \
                    f"The x-axis represents age, while the y-axis represents frequency. " \
                    f"The data is divided into {num_bins} bins to visualize the distribution. " \
                    f"The plot shows how the ages are distributed across the dataset, " \
             f"with the highest frequency occurring in certain age ranges."

            return self.call_gpt(prompt)
        
    def call_gpt(self,prompt):
     
        openai.api_key=self.gpt_key
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}"},
        
        ]
)       
        stuff = response.choices[0].message['content']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logged_data = f"""{"="*200}\n\n{timestamp}: Generate a brief explanation for the correlation matrix of integer columns:\n\nprompt: {prompt}\nresponse: {stuff}
        """
        Utils.log(logged_data)
        return stuff