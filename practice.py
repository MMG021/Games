from operator import le
from re import I

# num = int(input('How many numbers: '))
# total_sum = 0
# for n in range(num):
#     numbers = float(input('Enter number : '))
#     total_sum += numbers
# avg = total_sum/num
# print('Average of ', num, ' numbers is :', avg)

story = """education is a process of learning through which we acquire knowledge. 
It enlightens, empowers, and creates a positive development. 
education gives an individual the knowledge and skills to work with virtue. 
it aids the all-round mental, physical, and intellectual growth and development of an individual. 
there are three distinct types of Education- Formal Education, Non-Formal Education, and Informal Education. 
Education aims to change the way of one’s thinking. Academic knowledge provides one leaning on a global scale, while Practical knowledge is acquired for life on the whole. 
Education is imparted to all, at various research and academic institutions, imparted by teachers, professors, and trainers.These institutions conduct various curricular activities that aid the overall growth and development of students.
Education boosts and develops the commercial scenario as well as benefits the overall economy of the country. Higher the level of education, the better are the chances of development. Therefore, it is highly important to educate the children and youth to live a productive life and help in the development of society and the nation."""

print(story.capitalize())
print(story.endswith("economy"))
print(len(story))
print("Number of 'a' in story",story.count("a"))
print(story. )