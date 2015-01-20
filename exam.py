import yaml
import jinja2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="The file that should be parsed to create the exam")
parser.add_argument("--answers", help="Output the answers of the exam", action="store_true")
parser.add_argument("--output", help="The target output file, not yet implemented")
args = parser.parse_args()

env = jinja2.Environment(
    "%<", ">%", # Block Delimiter
    "<<", ">>", # Variable Delimiter
    "[[", "]]", # I don't remember
    loader=jinja2.FileSystemLoader(".")
)



class exam:
    def __init__(self, filename=None):
        self.template = env.get_template('exam.template')
        return

sample = []
sample.append(yaml.load("""
    Catalog: THEA334
    Topic: Prep
    Question: What is the difference between a assistant designer and an associate designer?
    Answer: An associate designer has the ability to speak for the designer and make design decisions in his absence, an assistant designer has no ability to make design decisions and acts primarilly as an information funnel to the designer along with maintaining paperwork.
"""))

f = open(args.filename)
questions = yaml.load_all(f)

doc = exam()
if args.answers:
    print (doc.template.render(name="Introduction to Theater Sound Design", catalog="THEA334", instructor="Thomas Vecchione", questions= questions, answers='answers', filename=args.filename))
else:
    print (doc.template.render(name="Introduction to Theater Sound Design", catalog="THEA334", instructor="Thomas Vecchione", questions= questions, answers='noanswers', filename=args.filename))

