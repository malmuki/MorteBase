from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify
from main.models.skill import Skill
import csv

class Command(BaseCommand):
  help = "import the skills from skill.tsv"

  def handle(self, *args, **options):
    skills = list(csv.reader(open("Skills.tsv"), delimiter="\t"))
    for row in skills:
      Skill.objects.get_or_create(
        name=row[0],
        slug=slugify(row[0]),
        description=row[1],
      )
      self.stdout.write(" imported " + row[0])
      self.stdout.flush()